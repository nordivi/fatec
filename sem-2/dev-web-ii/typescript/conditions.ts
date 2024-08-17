// 5

import PromptSync = require("prompt-sync")

const prompt = PromptSync()

let n_1 = Number(prompt("Enter n_1: "))
let n_2 = Number(prompt("Enter n_2: "))
let n_3 = Number(prompt("Enter n_3: "))

console.log(n_3 > n_1 && n_3 < n_2 
    ? `${n_3} está dentro do intervalo.` 
    : `${n_3} não está dentro do intervalo.`)

// 6

let n_4 = Number(prompt("Enter n_4: "))
console.log(n_4 % 2 ? `${n_4} é impar.` : `${n_4} é par.`)

// 7
let year = Number(prompt("Enter birth year: "))
const year_now = 2024

for (let i = year; i <= year_now; i++) {
    console.log(`Em ${year}, você fez/fará ${i - year} anos.`)
}

