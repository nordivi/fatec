"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const PromptSync = require("prompt-sync");
const prompt = PromptSync();
// 5
let x = Number(prompt("Enter n_1: "));
let y = Number(prompt("Enter n_2: "));
let z = Number(prompt("Enter n_3: "));
console.log(z > x && z < y
    ? `${z} está dentro do intervalo.`
    : `${z} não está dentro do intervalo.`);
// 6
let n = Number(prompt("Enter n_4: "));
console.log(n % 2 ? `${n} é impar.` : `${n} é par.`);
// 7
let year = Number(prompt("Enter birth year: "));
const year_now = 2024;
for (let i = year; i <= year_now; i++) {
    console.log(`Em ${year}, você fez/fará ${i - year} anos.`);
}
