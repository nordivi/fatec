"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const PromptSync = require("prompt-sync");
const prompt = PromptSync();
// 3
const calculate = (x, y) => {
    console.log(`${x} + ${y} = ${x + y}`);
    console.log(`${x} - ${y} = ${x - y}`);
    console.log(`${x} / ${y} = ${x / y}`);
    console.log(`${x} * ${y} = ${x * y}`);
};
let x = Number(prompt("Enter n_1: "));
let y = Number(prompt("Enter n_2: "));
calculate(x, y);
