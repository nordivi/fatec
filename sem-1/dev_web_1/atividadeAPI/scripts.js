const API_OPEN_WEATHER_MAP_KEY = "77a52c683ff8dbcfa3b64da122612828";
const BD_IMAGE_UNSPLASH_URL = "https://api.unsplash.com/photos/?";
const UNSPLASH_API_KEY = "qkFHSmjjvYKzFX9VXIXWcI4mStg1cQNRpTor6K5ba8k";
const UNSPLASH_SECRET_KEY = "-MeA92UoUyICemZPWvpxGEp4HVcwWgSLGhfDo0IY-L0";
const FLAGS_API_URL = "https://flagsapi.com/"

async function ProcuraCEP(){
    const cep = document.getElementById('cep').value;
    const url = `https://viacep.com.br/ws/${cep}/json/`;
    const dados = await fetch(url);
    const endereco = await dados.json();
    console.log('Procurando...')
    if (endereco.erro){
        alert("CEP não encontrado")
        return;
    }

    let logradouro = endereco.logradouro;
    let bairro = endereco.bairro;
    let localidade = endereco.localidade;
    let uf = endereco.uf;

    document.getElementById('logradouro').value = `${logradouro}, ${bairro} - ${localidade}/${uf}`;

    const imgResponse = `${BD_IMAGE_UNSPLASH_URL}query=cidade${localidade}&client_id=${UNSPLASH_API_KEY}`;
    const imgJSON = await fetch(imgResponse);
    const img = await imgJSON.json();
    const imgURL = img[0].urls.full;
    console.log(imgURL)
    document.getElementById('imgCidade').setAttribute('src', imgURL);
}

const tempElement = document.getElementById('temperatura');
const vento = document.getElementById('vento');
const humidade = document.getElementById('humidade');
const tempo = document.getElementById('tempo');
const climaIconElement = document.getElementById('icone');
const dadosTemp = document.querySelector('.dadosTemperatura');
const dadosLog = document.querySelector('.dadosLogradouro');
const cidade = document.getElementById('cidade')

document.querySelector('#verificarClima').addEventListener('click', async () => {
    const res = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${cidade.value}&appid=${API_OPEN_WEATHER_MAP_KEY}&lang=pt_br&units=metric`);
    const data = await res.json();
    
    if (data.cod === 404){
        alert("Cidade não encontrada");
        return;
    }

    tempElement.innerText = parseFloat(data.main.temp) + "°";
    humidade.innerText = parseFloat(data.main.humidity) + "%";
    vento.innerText = parseFloat(data.wind.speed) + "km/h";
    tempo.innerText = data.weather[0].description;
    document.getElementById('imgPais').setAttribute('src', `${FLAGS_API_URL}${data.sys.country}/flat/16.png`);
    climaIconElement.src = `http://openweathermap.org/img/w/${data.weather[0].icon}.png`;

})

function LimparDados() {
    document.getElementById('logradouro').value = '';
    document.getElementById('cep').value = '';
    document.getElementById('temperatura').innerText = '';
    document.getElementById('vento').innerText = '';
    document.getElementById('humidade').innerText = '';
    document.getElementById('tempo').innerText = '';
    document.getElementById('imgCidade').setAttribute('src', '');
    document.getElementById('imgPais').setAttribute('src', '');
    document.getElementById('cidade').value = '';
    document.getElementById('cep').focus();
    climaIconElement.src=''

}