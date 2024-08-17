"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var PromptSync = require("prompt-sync");
var prompt = PromptSync();
// 3
var calculate = function (x, y) {
    console.log("".concat(x, " + ").concat(y, " = ").concat(x + y));
    console.log("".concat(x, " - ").concat(y, " = ").concat(x - y));
    console.log("".concat(x, " * ").concat(y, " = ").concat(x * y));
    console.log("".concat(x, " / ").concat(y, " = ").concat(x / y));
};
var x = Number(prompt("Enter n_1: "));
var y = Number(prompt("Enter n_2: "));
calculate(x, y);
