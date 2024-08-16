"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const PromptSync = require("prompt-sync");
const prompt = PromptSync();
var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var userInput = prompt("Enter a number to add to the array: ");
var newNumber = parseInt(userInput || '0');
numbers.push(newNumber);
console.log("Array:", numbers);
