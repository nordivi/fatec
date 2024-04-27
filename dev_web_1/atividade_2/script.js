
function getRandom(min, max){
    return Number(Math.floor(Math.random() * (max - min + 1)) + min)
}

function ex01(){
    const n1 = document.getElementById('n1').value
    const n2 = document.getElementById('n2').value
    document.getElementById('n1-label').innerText = (Number(n1) + Number(n2)) / 2
}

function ex02(){
    const n1 = Number(window.prompt('Digite o primeiro número'))
    const n2 = Number(window.prompt('Digite o segundo número'))
    console.log(`${n1} elevado a ${n2} resulta em ${Math.pow(n1, n2)}`)
    alert("Confira o resultado no console!")
}


function ex03(){
    lista_numeros = [getRandom(0, 1000), getRandom(0, 1000), getRandom(0, 1000)]
    menor_numero = Math.min(lista_numeros)
    console.log(menor_numero)
    // Não está comentando de que forma deve ser mostrado. Utilizarei um alert
    alert(`O menor número da lista ${lista_numeros} é ${Math.min(...lista_numeros)}`)
}

function ex04(){
    const X = [15,25]
    const Y = [12,15,23,43]
    for (let i = 0; i < X.length; i++ ){
        X[i]*=5
    }
    console.log(`Array X resultante: ${X}`)
}

function ex05(){
    // Como não fala a forma que recebe as notas, irei receber por meio de um input.
    const n1 = document.getElementById('n1-5').value
    const n2 = document.getElementById('n2-5').value
    const soma_notas = Number(n1) + Number(n2)
    document.getElementById('n1-5-label').innerText = (Number(n1)*0.3 + Number(n2)*0.7)
}

function ex06(){
    const horas_convencionais = 40
    const horas_totais = 62
    const horas_extras = horas_totais - horas_convencionais
    const valor_desc_refeicao = 1.5
    // Quantas refeições o funcionário teve nessas horas?
    // Qual o valor pago pela hora convencional?
    // Não fala que temos que pegar esses valores, vou pegar num window.prompt
    // Também não explica como mostrar, mostrarei num alert
    const qttd_refeicoes = Number(window.prompt('Digite a quantidade de refeições'))
    const valor_convencional = Number(window.prompt('Digite o valor ganho por hora convencional'))

    const salario_bruto = valor_convencional*horas_convencionais + (valor_convencional*3)*horas_extras
    const desconto_refeicao = qttd_refeicoes*valor_desc_refeicao
    const salario_liquido = salario_bruto - desconto_refeicao
    alert(`Salário bruto: ${salario_bruto} | Desconto refeição: ${desconto_refeicao} | Salário líquido: ${salario_liquido}`)
}

function ex07(){
    const n1 = getRandom(-10000, 10000)
    if (n1 % 2) {
        alert(`O número randômico ${n1} é ímpar`)
    } else {
        alert(`O número randômico ${n1} é par`)
    }
}

function ex08(){
    const valor = Number(document.getElementById('produto').value)
    const quantidade = Number(document.getElementById('quantidade').value)
    const desconto = 0
    const valor_bruto = valor*quantidade
    if (valor_bruto >= 1000){
        desconto += 0.1*valor_bruto
    }

    const forma_pagamento = document.querySelector('input[name="pagamento"]:checked').value
    const desconto_pagamento = document.querySelector('input[name="pagamento"]:checked').value
}