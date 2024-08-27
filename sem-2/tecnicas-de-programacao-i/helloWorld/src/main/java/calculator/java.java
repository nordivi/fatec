package calculator;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class java {
     public static void main(String[] args)
    {
        List<Float> numbers = new ArrayList<>();
        int qtt;
        Scanner myObj = new Scanner(System.in);
        
        System.out.printf("Quantos numeros deseja digitar? ");
        qtt = myObj.nextInt();
        for (int i=0; i < qtt; i++){
            float n;
            System.out.printf("Digite o %d numero: ", i + 1);
            n = myObj.nextFloat();
            numbers.add(n);
        }
        System.out.printf("Qual operacao deseja realizar?\n");
        System.out.printf("Opcoes: (+, -, *, /, ^, radiciacao)");
        myObj.nextLine();
        String operacao = myObj.nextLine();
        float resultado = numbers.get(0);
        if (operacao != null)
            switch (operacao) {
             case "+" -> {
                 for (int i = 1; i < qtt; i++){
                     resultado = resultado + numbers.get(i);
                 }
                System.out.printf("Resultado: %f%n", resultado);
            }
             case "-" -> {
                 for (int i = 1; i < qtt; i++){
                     resultado = resultado - numbers.get(i);
                 }
                System.out.printf("Resultado: %f%n", resultado);
            }
             case "*" -> {
                 for (int i = 1; i < qtt; i++){
                     resultado = resultado * numbers.get(i);
                 }
                System.out.printf("Resultado: %f%n", resultado);
            }
             case "/" -> {
                 for (int i = 1; i < qtt; i++){
                     if (numbers.get(i) == 0){
                        System.out.printf("Impossível dividir por 0 nos numeros reais.");
                         return;
                     }
                     resultado = resultado / numbers.get(i);
                 }
                System.out.printf("Resultado: %f%n", resultado);
            }
             case "^" -> {
                 for (int i = 1; i < qtt; i++){
                     resultado = (float) Math.pow(resultado, numbers.get(i));
                 }
                System.out.printf("Resultado: %f%n", resultado);
            }
             case "radiciacao" -> {
                 for (int i = 1; i < qtt; i++){
                     if (numbers.get(i) == 0){
                        System.out.printf("Impossível racionalizar por 0 nos numeros reais.");
                         return;
                     }
                     resultado = (float) Math.pow(resultado, 1/numbers.get(i));
                 }
                    System.out.printf("Resultado: %f%n", resultado);
             }
             default -> {
                 System.out.printf("Operação não concluída.");
            }
         }
    }
}
