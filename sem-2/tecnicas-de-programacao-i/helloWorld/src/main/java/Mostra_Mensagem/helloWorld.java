package Mostra_Mensagem;

import java.util.Scanner;  

public class helloWorld
{
    public static void main(String[] args)
    {
        Scanner myObj = new Scanner(System.in);
        System.out.printf("Escolha um numero: ");
        System.out.printf("Hello, World! %d%n", myObj.nextInt());
        
        System.out.printf("Escolha o primeiro numero para calcular: ");
        float x = myObj.nextFloat();
        System.out.printf("Escolha o segundo numero para calcular: ");
        float y = myObj.nextFloat();
        System.out.printf("%f + %f = %f%n", x, y, x+y);
        System.out.printf("%f - %f = %f%n", x, y, x-y);
        System.out.printf("%f * %f = %f%n", x, y, x*y);
        System.out.printf("%f ^ %f = %f%n", x, y, Math.pow(x,y));
        if (y == 0) {
            System.out.printf("Nao e possivel dividir nem racionalizar por 0!");
            return;
        }
        System.out.printf("%f / %f = %f%n", x, y, x/y);
        System.out.printf("%f SQRT %f = %f%n", x, y, Math.pow(x,1/y));
    }
}