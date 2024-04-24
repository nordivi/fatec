function calcular(){
    let valor_final = 0

    const combo = document.getElementById('combo').value
    valor_final += Number(combo)

    const bacon = document.getElementById('bacon').checked
    const cheddar = document.getElementById('cheddar').checked
    const picles = document.getElementById('picles').checked
    const alface = document.getElementById('alface').checked
    if (bacon) {
        valor_final += 2
    }

    if (cheddar) {
        valor_final += 2
    }

    if (picles) {
        valor_final += 3
    }

    if (alface) {
        valor_final += 1
    }

    const togo = document.getElementById('togo').checked

    if (togo) {
        valor_final += 10
    }

    document.getElementById('total').innerText = `O valor da sua compra ficou R$ ${valor_final}!`

}

function novoPedido() {
    document.getElementById('bacon').checked = false
    document.getElementById('cheddar').checked = false
    document.getElementById('picles').checked = false
    document.getElementById('alface').checked = false
    document.getElementById('total').innerText = ''
    document.getElementById('telefone-input').value = ''
    document.getElementById('nome-input').value = ''
    document.getElementById('togo').checked = false
    document.getElementById('balcao').checked = false
}

function resumo() {
    resposta = ''
    nome = document.getElementById('nome-input').value
    telefone = document.getElementById('telefone-input').value
    resposta += `Nome: ${nome} | Telefone: ${telefone} \n`
    valor = document.getElementById('combo').value

    if (valor === '20') {
        resposta += 'Combo pedido: '.concat('X-Salada (R$ 20,00)\n')
    }
    else if (valor === '25') {
        resposta += 'Combo pedido: '.concat('X-Bacon (R$ 25,00)\n')
    }
    else if (valor === '35') {
        resposta += 'Combo pedido: '.concat('X-Tudo (R$ 35,00)\n')
    }
    if (document.getElementById('bacon').checked) {
        resposta += 'Adicional de Bacon (+R$2,00) \n'
    } else if (document.getElementById('cheddar').checked) {
        resposta += 'Adicional de Cheddar (+R$2,00) \n'
    } else if (document.getElementById('picles').checked) {
        resposta += 'Adicional de Picles (+R$3,00) \n'
    } else if (document.getElementById('alface').checked) {
        resposta += 'Adicional de Alface (+R$1,00) \n'
    }

    if (document.getElementById('togo').checked) {
        resposta += 'Entrega: Para viagem (+R$10,00) \n'
    } else if (document.getElementById('balcao').checked) {
        resposta += 'Entrega: Balcão \n'
    }

    document.getElementById('desc').innerHTML = resposta


}