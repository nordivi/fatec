import PromptSync = require("prompt-sync")

const prompt = PromptSync()

// 5
let x: number = Number(prompt("Enter n_1: "))
let y: number = Number(prompt("Enter n_2: "))
let z: number = Number(prompt("Enter n_3: "))

console.log(z > x && z < y 
    ? `${z} está dentro do intervalo.` 
    : `${z} não está dentro do intervalo.`)

// 6
let n: number = Number(prompt("Enter n_4: "))
console.log(n % 2 ? `${n} é impar.` : `${n} é par.`)

// 7
let year: number = Number(prompt("Enter birth year: "))
const year_now: number = 2024

for (let i = year; i <= year_now; i++) {
    console.log(`Em ${year}, você fez/fará ${i - year} anos.`)
}


