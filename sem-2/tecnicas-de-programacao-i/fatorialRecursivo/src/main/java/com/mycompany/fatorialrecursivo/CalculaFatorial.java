/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.fatorialrecursivo;

/**
 *
 * @author Alunos
 */
public class CalculaFatorial {
    public static int fatorial(int n){
        if (n==2){
            return 2;
        }
        return n*fatorial(n-1);
    }
}
