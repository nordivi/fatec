/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.extrato;

/**
 *
 * @author Alunos
 */
public class ContaCorrente {
    private String num_conta; 
    private String num_agencia; 
    private int id_cli;         
    private double saldo;       

    public ContaCorrente(String num_conta, String num_agencia, int id_cli, double saldo) {
        this.num_conta = num_conta;
        this.num_agencia = num_agencia;
        this.id_cli = id_cli;
        this.saldo = saldo;
    }

    public String getNumConta() {
        return num_conta;
    }

    public void setNumConta(String num_conta) {
        this.num_conta = num_conta;
    }

    public String getNumAgencia() {
        return num_agencia;
    }

    public void setNumAgencia(String num_agencia) {
        this.num_agencia = num_agencia;
    }

    public int getIdCli() {
        return id_cli;
    }

    public void setIdCli(int id_cli) {
        this.id_cli = id_cli;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }
}