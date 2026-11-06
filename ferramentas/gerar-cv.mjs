// Gera o CV em PDF a partir de ferramentas/curriculo.html: node ferramentas/gerar-cv.mjs
// Usa o Chrome pelo Playwright da pd-plataforma. A fonte é a Calibri do Windows.
import { chromium } from "file:///C:/Users/Thunas/Desktop/pd-plataforma/node_modules/playwright/index.mjs";
import { dirname, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const aqui = dirname(fileURLToPath(import.meta.url));
const saida = resolve(aqui, "../Portfolio-Rafael-Pessoa/CV_RafaelPessoa_AnalistaDadosSenior.pdf");

const nav = await chromium.launch({ channel: "chrome" });
const p = await nav.newPage();
await p.goto(pathToFileURL(resolve(aqui, "curriculo.html")).href, { waitUntil: "load" });
await p.evaluate(() => document.fonts.ready);
await p.pdf({ path: saida, preferCSSPageSize: true, printBackground: true, tagged: true });
await nav.close();
console.log("gerado", saida);
