let lampada = document.getElementById('lampada');
 
function ligar(){
    lampada.setAttribute("src", "luzLigada.gif")    
   // lampada.style.display = "block";
    
}
 
function desligar(){
    lampada.setAttribute("src", "luzDesligada.gif")  
    lampada.hidden = false
}
 
function sumir(){
    lampada.hidden = true
}
 
function aparecer(){
    lampada.hidden = false
}
 
function piscar(){
    if (lampada.getAttribute("src") == "luzDesligada.gif") {   
        lampada.setAttribute("src", "luzLigada.gif");}    
    else {
        lampada.setAttribute("src", "luzDesligada.gif"); }
 
}
 
function magica(){
    ligar()
    desligar()
    ligar()
    desligar()
    setInterval(piscar, 500)
}