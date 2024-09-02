package com.mycompany.classeteste;
import java.util.Scanner;

public class ClasseTeste {

    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        System.out.printf("Escolha um numero: ");
        int n1 = myObj.nextInt();
        Classe_Teste_X test1 = new Classe_Teste_X(n1);
        
        System.out.printf("Escolha um numero: ");
        int n2 = myObj.nextInt();
        Classe_Teste_X test2 = new Classe_Teste_X(n1, n2);
        
        System.out.println("N1: " + test1.getNumero()); 
        
        test1.setResultado(test1.getNumero() * 3);
        System.out.println("N1*3: " + test1.getResultado()); 
        
        System.out.println("N2*2: " + test2.getDobro());
        
        System.out.println("N1*N2: " + test2.getMultiplica()); 
    }
}
