// Gera os CVs em PDF: curriculo.html (português) e curriculo-en.html (inglês, para o /en). node ferramentas/gerar-cv.mjs
// Usa o Chrome pelo Playwright da pd-plataforma. A fonte é a Calibri do Windows.
import { chromium } from "file:///C:/Users/Thunas/Desktop/pd-plataforma/node_modules/playwright/index.mjs";
import { dirname, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const aqui = dirname(fileURLToPath(import.meta.url));
const site = resolve(aqui, "../Portfolio-Rafael-Pessoa");
// o nome do PDF em português fica, porque o link do site e os envios antigos apontam para ele
const CVS = [["curriculo.html", "CV_RafaelPessoa_AnalistaDadosSenior.pdf"], ["curriculo-en.html", "CV_RafaelPessoa_SeniorDataAnalyst_EN.pdf"]];

const nav = await chromium.launch({ channel: "chrome" });
const p = await nav.newPage();
for (const [fonte, pdf] of CVS) {
  await p.goto(pathToFileURL(resolve(aqui, fonte)).href, { waitUntil: "load" });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: resolve(site, pdf), preferCSSPageSize: true, printBackground: true, tagged: true });
  console.log("gerado", pdf);
}
await nav.close();
