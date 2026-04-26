#!/usr/bin/env node
/**
 * calm-design / scripts/render-preview.js
 *
 * Playwright로 HTML 파일을 렌더링하여 데스크톱·모바일 PNG로 캡처.
 * Phase 1+ 셀프-크리틱 루프의 [2] Render+Capture 단계 핵심 도구.
 *
 * 사용법:
 *   node scripts/render-preview.js <input.html> [outputDir]
 *
 * 출력:
 *   {outputDir}/desktop.png      # 1440x900 viewport, fullPage
 *   {outputDir}/mobile.png       # 390x844 viewport (iPhone 14), fullPage
 *   {outputDir}/desktop-fold.png # 1440x900 (above-the-fold만, 첫 폴드 검증용)
 *   {outputDir}/meta.json        # 페이지 메타 (title, viewport sizes, render time)
 *
 * 의존성:
 *   npm install playwright
 *   npx playwright install chromium
 *
 * Exit codes:
 *   0 — 성공
 *   1 — 입력 파일 없음
 *   2 — Playwright 미설치
 *   3 — 렌더링 실패
 */

const fs = require("fs");
const path = require("path");

const VIEWPORTS = {
  desktop: { width: 1440, height: 900, name: "desktop" },
  mobile: { width: 390, height: 844, name: "mobile" }, // iPhone 14
};

async function renderPreview(htmlPath, outputDir) {
  // 의존성 체크
  let chromium;
  try {
    ({ chromium } = require("playwright"));
  } catch (e) {
    console.error(
      "❌ playwright 미설치. 다음 명령으로 설치:\n   npm install playwright\n   npx playwright install chromium"
    );
    process.exit(2);
  }

  // 입력 파일 검증
  const absHtmlPath = path.resolve(htmlPath);
  if (!fs.existsSync(absHtmlPath)) {
    console.error(`❌ 입력 파일 없음: ${absHtmlPath}`);
    process.exit(1);
  }

  // 출력 디렉토리 준비
  fs.mkdirSync(outputDir, { recursive: true });

  const fileUrl = `file://${absHtmlPath}`;
  const meta = {
    input: absHtmlPath,
    rendered_at: new Date().toISOString(),
    viewports: {},
  };

  const browser = await chromium.launch({ headless: true });

  try {
    // 데스크톱 풀 캡처
    const dCtx = await browser.newContext({ viewport: VIEWPORTS.desktop });
    const dPage = await dCtx.newPage();
    await dPage.goto(fileUrl, { waitUntil: "networkidle", timeout: 15000 });
    await dPage.waitForTimeout(500); // 모션 안정화

    const desktopPath = path.join(outputDir, "desktop.png");
    await dPage.screenshot({ path: desktopPath, fullPage: true });

    const desktopFoldPath = path.join(outputDir, "desktop-fold.png");
    await dPage.screenshot({ path: desktopFoldPath, fullPage: false });

    meta.viewports.desktop = {
      width: VIEWPORTS.desktop.width,
      height: VIEWPORTS.desktop.height,
      file: desktopPath,
      title: await dPage.title(),
      lang: await dPage.getAttribute("html", "lang"),
    };

    await dCtx.close();

    // 모바일 풀 캡처
    const mCtx = await browser.newContext({
      viewport: VIEWPORTS.mobile,
      isMobile: true,
      hasTouch: true,
    });
    const mPage = await mCtx.newPage();
    await mPage.goto(fileUrl, { waitUntil: "networkidle", timeout: 15000 });
    await mPage.waitForTimeout(500);

    const mobilePath = path.join(outputDir, "mobile.png");
    await mPage.screenshot({ path: mobilePath, fullPage: true });

    meta.viewports.mobile = {
      width: VIEWPORTS.mobile.width,
      height: VIEWPORTS.mobile.height,
      file: mobilePath,
    };

    await mCtx.close();

    // 메타 저장
    fs.writeFileSync(
      path.join(outputDir, "meta.json"),
      JSON.stringify(meta, null, 2)
    );

    console.log(`✅ 캡처 완료: ${outputDir}`);
    console.log(`   desktop.png      ${meta.viewports.desktop.width}x${meta.viewports.desktop.height} (full page)`);
    console.log(`   desktop-fold.png ${meta.viewports.desktop.width}x${meta.viewports.desktop.height} (above-the-fold)`);
    console.log(`   mobile.png       ${meta.viewports.mobile.width}x${meta.viewports.mobile.height} (full page)`);
    console.log(`   meta.json`);
    console.log(`   언어: ${meta.viewports.desktop.lang || "unspecified"}`);
  } catch (err) {
    console.error(`❌ 렌더링 실패: ${err.message}`);
    process.exit(3);
  } finally {
    await browser.close();
  }
}

// CLI 진입
if (require.main === module) {
  const args = process.argv.slice(2);
  if (args.length < 1) {
    console.error("사용법: node scripts/render-preview.js <input.html> [outputDir]");
    console.error("예시:   node scripts/render-preview.js examples/01-saas-dashboard-ko/index.html .calm-design/critique-shots");
    process.exit(1);
  }

  const [htmlPath, outputDir = ".calm-design/critique-shots"] = args;

  renderPreview(htmlPath, outputDir).catch((err) => {
    console.error("❌ 예외 발생:", err);
    process.exit(3);
  });
}

module.exports = { renderPreview, VIEWPORTS };
