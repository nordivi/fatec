/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.extrato;

/**
 *
 * @author Alunos
 */
import java.time.LocalDateTime; 
import java.math.BigDecimal;   

public class ExtratoMovimentacao {
    private String num_conta;      
    private String num_agencia;      
    private String documento;       
    private LocalDateTime data_movimentacao; 
    private char credito_ou_debito;   
    private String id_his;       
    private BigDecimal valor;         
    private BigDecimal saldo;          

    // Constructor
    public ExtratoMovimentacao(String num_conta, String num_agencia, String documento,
                               LocalDateTime data_movimentacao, char credito_ou_debito,
                               String id_his, BigDecimal valor, BigDecimal saldo) {
        this.num_conta = num_conta;
        this.num_agencia = num_agencia;
        this.documento = documento;
        this.data_movimentacao = data_movimentacao;
        this.credito_ou_debito = credito_ou_debito;
        this.id_his = id_his;
        this.valor = valor;
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

    public String getDocumento() {
        return documento;
    }

    public void setDocumento(String documento) {
        this.documento = documento;
    }

    public LocalDateTime getDataMovimentacao() {
        return data_movimentacao;
    }

    public void setDataMovimentacao(LocalDateTime data_movimentacao) {
        this.data_movimentacao = data_movimentacao;
    }

    public char getCreditoOuDebito() {
        return credito_ou_debito;
    }

    public void setCreditoOuDebito(char credito_ou_debito) {
        this.credito_ou_debito = credito_ou_debito;
    }

    public String getIdHis() {
        return id_his;
    }

    public void setIdHis(String id_his) {
        this.id_his = id_his;
    }

    public BigDecimal getValor() {
        return valor;
    }

    public void setValor(BigDecimal valor) {
        this.valor = valor;
    }

    public BigDecimal getSaldo() {
        return saldo;
    }

    public void setSaldo(BigDecimal saldo) {
        this.saldo = saldo;
    }
}
