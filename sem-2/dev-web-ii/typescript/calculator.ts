import PromptSync = require("prompt-sync")

const prompt = PromptSync()

// 3
const calculate = (x: number, y: number): void => {
    console.log(`${x} + ${y} = ${x+y}`)
    console.log(`${x} - ${y} = ${x-y}`)
    console.log(`${x} / ${y} = ${x/y}`)
    console.log(`${x} * ${y} = ${x*y}`)
}


let x: number = Number(prompt("Enter n_1: "))
let y: number = Number(prompt("Enter n_2: "))
calculate(x,y)