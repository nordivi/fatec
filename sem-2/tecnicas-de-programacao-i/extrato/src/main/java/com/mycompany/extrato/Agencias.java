/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.extrato;

/**
 *
 * @author Alunos
 */
public class Agencias {
    private String num_agencia;
    private String nome;
    private String endereco;
    private String numero;
    private String complemento;
    private String bairro;
    private String cidade;
    private String UF;
    private String CEP;
    private String CNPJ;
    private String gerente;
    
    public Agencias(String num_agencia, String nome, String endereco, String numero, String complemento, String bairro, String cidade, String UF, String CEP, String CNPJ, String gerente) {
        this.num_agencia = num_agencia;
        this.nome = nome;
        this.endereco = endereco;
        this.numero = numero;
        this.complemento = complemento;
        this.bairro = bairro;
        this.cidade = cidade;
        this.UF = UF;
        this.CEP = CEP;
        this.CNPJ = CNPJ;
        this.gerente = gerente;   
    }
    
    public String getNumAgencia() {
        return num_agencia;
    }

    public void setNumAgencia(String num_agencia) {
        this.num_agencia = num_agencia;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        if (nome == null || nome.length() < 5){
            System.out.println("Nome inválido!");
            return;
        }
        this.nome = nome;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public String getComplemento() {
        return complemento;
    }

    public void setComplemento(String complemento) {
        this.complemento = complemento;
    }

    public String getBairro() {
        return bairro;
    }

    public void setBairro(String bairro) {
        this.bairro = bairro;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
        this.cidade = cidade;
    }

    public String getUF() {
        return UF;
    }

    public void setUF(String UF) {
        this.UF = UF;
    }

    public String getCEP() {
        return CEP;
    }

    public void setCEP(String CEP) {
        this.CEP = CEP;
    }

    public String getCNPJ() {
        return CNPJ;
    }

    public void setCNPJ(String CNPJ) {
        this.CNPJ = CNPJ;
    }

    public String getGerente() {
        return gerente;
    }

    public void setGerente(String gerente) {
        this.gerente = gerente;
    }
    
    public boolean isValidNome() {
        return (this.nome == null || this.nome.length() > 5);
    }

    public boolean isValidNumAgencia() {
        return this.num_agencia != null && this.num_agencia.length() == 4 && this.num_agencia.matches("\\d+");
    }

    public boolean isValidEndereco() {
        return this.endereco.length() >= 10; 
    }

    public boolean isValidNumero() {
        return this.numero != null && this.numero.length() >= 1 && this.numero.length() <= 5;
    }

    public boolean isValidComplemento() {
        return this.complemento.length() <= 20;
    }

    public boolean isValidBairro() {
        return this.bairro != null && this.bairro.length() >= 3;
    }

    public boolean isValidCidade() {
        return this.cidade != null && this.cidade.length() >= 3;
    }

    public boolean isValidUF() {
        return this.UF != null && this.UF.length() == 2;
    }

    public boolean isValidCEP() {
        return this.CEP != null && this.CEP.length() == 8;
    }

    public boolean isValidCNPJ() {
        return this.CNPJ != null && this.CNPJ.length() == 14; 
    }

    public boolean isValidGerente() {
        return this.gerente.length() >= 3;
    }

    public boolean isValid() {
        return isValidNome() && isValidNumAgencia() && isValidEndereco() && isValidNumero() && isValidComplemento() && isValidBairro() && isValidCidade() && isValidUF() && isValidCEP() && isValidCNPJ() && isValidGerente();
    }
}
