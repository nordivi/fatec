package com.mycompany.classeteste;

public class Classe_Teste_X {

    private int numero;
    private int numero2;
    private int resultado; 

    public Classe_Teste_X(int numero){
        super();
        this.numero = numero;
    }
    
    public Classe_Teste_X(int numero, int numero2){
        super();
        this.numero = numero;
        this.numero2 = numero2;
    }
    
    public int getNumero(){
        return numero;
    }
   
    public void setNumero(int numero){
        this.numero = numero;
    }
    
    public int getNumero2(){
        return numero2;
    }
   
    public void setNumero2(int numero2){
        this.numero2 = numero2;
    }
    
    public int getResultado() {
        return resultado;
    }

    public void setResultado(int resultado) {
        this.resultado = resultado;
    }

    public int getDobro(){
        resultado = getNumero() * 2;
        return resultado;
    }

    public int getMultiplica() {
        resultado = getNumero() * getNumero2();
        return resultado;
    }
}
