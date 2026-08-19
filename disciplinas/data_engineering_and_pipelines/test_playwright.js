const { chromium } = require('/home/afonsolelis/Repos/aulas/node_modules/playwright');

(async () => {
  const browser = await chromium.launch();
  console.log("Playwright is working");
  await browser.close();
})();
