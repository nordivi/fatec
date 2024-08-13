
async function encontra_cep(){
    const cep = document.getElementById('cep').value
    const res = await fetch(`https://viacep.com.br/ws/${cep}/json/`)
    const cepInfo = await res.json()

    
    const cepNumber = `CEP: ${cepInfo.cep} \n`
    const logradouro = `Logradouro: ${cepInfo.logradouro} \n`
    const uf = `Estado: ${cepInfo.uf} \n`
    const localidade = `Cidade: ${cepInfo.localidade} \n`
    const bairro = `Bairro: ${cepInfo.bairro} \n`

    document.getElementById('cep-info').textContent = cepNumber
    document.getElementById('uf-info').textContent = logradouro
    document.getElementById('rua-info').textContent = uf
    document.getElementById('city-info').textContent = localidade
    document.getElementById('bairro-info').textContent = bairro

}