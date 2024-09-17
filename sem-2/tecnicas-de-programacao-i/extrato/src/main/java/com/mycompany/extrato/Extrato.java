/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.extrato;
import java.math.BigDecimal;
import java.time.LocalDateTime;
/**
 *
 * @author Alunos
 */
public class Extrato {

    public static void main(String[] args) {
        Clientes cliente = new Clientes(
                123456789,     
                "João Silva",  
                "12345678901",
                "Rua A, 123",   
                "123",        
                "Apt 45",     
                "Centro",   
                "Cidade Exemplo", 
                "SP",        
                "12345678",    
                "joao.silva@example.com",
                true,         
                "(11) 98765-4321", 
                "12345678901234", 
                'M'         
        );

        System.out.println("Cliente Details:");
        System.out.println("ID: " + cliente.getIdCli());
        System.out.println("Nome: " + cliente.getNome());
        System.out.println("CPF: " + cliente.getCPF());
        System.out.println("Endereço: " + cliente.getEndereco());
        System.out.println("Número: " + cliente.getNumero());
        System.out.println("Complemento: " + cliente.getComplemento());
        System.out.println("Bairro: " + cliente.getBairro());
        System.out.println("Cidade: " + cliente.getCidade());
        System.out.println("UF: " + cliente.getUF());
        System.out.println("CEP: " + cliente.getCEP());
        System.out.println("Email: " + cliente.getEmail());
        System.out.println("Status: " + cliente.isStatus());
        System.out.println("Telefone: " + cliente.getTelefone());
        System.out.println("CNPJ: " + cliente.getCNPJ());
        System.out.println("Sexo: " + cliente.getSexo());

        ContaCorrente contaCorrente = new ContaCorrente(
                "123456789012", 
                "000001",    
                123456789,  
                1000.23
        );

        System.out.println("\nConta Corrente Details:");
        System.out.println("Número da Conta: " + contaCorrente.getNumConta());
        System.out.println("Número da Agência: " + contaCorrente.getNumAgencia());
        System.out.println("ID Cliente: " + contaCorrente.getIdCli());
        System.out.println("Saldo: " + contaCorrente.getSaldo());
        
        Historicos historico = new Historicos(
                1234,         
                "Transferência"  
        );

        System.out.println("\nHistórico Details:");
        System.out.println("ID Histórico: " + historico.getIdHis());
        System.out.println("Histórico: " + historico.getHistorico());

        ExtratoMovimentacao extratoMovimentacao = new ExtratoMovimentacao(
                "123456789012",               
                "000001",                    
                "000001",                  
                LocalDateTime.now(),       
                'C',                          
                "Transferência",        
                new BigDecimal("500.00"),    
                new BigDecimal("1500.00")     
        );

        System.out.println("\nExtrato Movimentação Details:");
        System.out.println("Número da Conta: " + extratoMovimentacao.getNumConta());
        System.out.println("Número da Agência: " + extratoMovimentacao.getNumAgencia());
        System.out.println("Documento: " + extratoMovimentacao.getDocumento());
        System.out.println("Data da Movimentação: " + extratoMovimentacao.getDataMovimentacao());
        System.out.println("Crédito ou Débito: " + extratoMovimentacao.getCreditoOuDebito());
        System.out.println("ID Histórico: " + extratoMovimentacao.getIdHis());
        System.out.println("Valor: " + extratoMovimentacao.getValor());
        System.out.println("Saldo: " + extratoMovimentacao.getSaldo());
    }
}