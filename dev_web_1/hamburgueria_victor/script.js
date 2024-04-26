function calcular(isRecibo = false){
    let valor_final = 0

    const combo = document.getElementById('combo').value
    valor_final += Number(combo)
    valor_final += calcularAdicionais()
    valor_final += calcularFrete()
    if (!isRecibo) {
        document.getElementById('total').innerText = `O valor da sua compra ficou R$ ${valor_final}!`
    }
    
    return valor_final
}

function calcularAdicionais(){
    adicional = 0;
    let selecionados;
    selecionados = document.querySelectorAll("input[name='adicional']");
    let qtd = selecionados.length;
    for (i=0; i< qtd; i++){
        if (selecionados[i].checked){
            adicional += Number(selecionados[i].value);
        }       
    }
    return adicional
}

function calcularFrete(){
    const togo = document.getElementById('togo').checked
    valor_frete = 0
    if (togo) {
        valor_frete += Number(document.getElementById('togo').value)
    }

    return valor_frete
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
    document.getElementById('desc').innerHTML = ''
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

    selecionados = document.querySelectorAll("input[name='adicional']");
    let qtd = selecionados.length;
    for (i=0; i< qtd; i++){
        if (selecionados[i].checked){
            resposta += `Adicional de ${selecionados[i].id} (+R$ ${selecionados[i].value},00) \n`
        }       
    }
    

    if (document.getElementById('togo').checked) {
        resposta += 'Entrega: Para viagem (+R$10,00) \n'
    } else if (document.getElementById('balcao').checked) {
        resposta += 'Entrega: Balcão \n'
    }

    resposta+=`Valor final: R$ ${calcular(true)}`

    document.getElementById('desc').innerHTML = resposta


}