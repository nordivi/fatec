import PromptSync = require("prompt-sync")

const prompt = PromptSync()
var numbers: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var userInput: string | null = prompt("Enter a number to add to the array: ");
var newNumber: number = parseInt(userInput ||  '0');

numbers.push(newNumber);

console.log("Array:", numbers);