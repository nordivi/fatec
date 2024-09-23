/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.extrato;

/**
 *
 * @author Alunos
 */
public class Clientes {
    private int id_cli;        
    private String nome;        
    private String CPF;       
    private String endereco;  
    private String numero;        
    private String complemento; 
    private String bairro;        
    private String cidade;         
    private String UF;            
    private String CEP;           
    private String email;      
    private boolean status;       
    private String telefone;       
    private String CNPJ;           
    private char sexo;             

    public Clientes(int id_cli, String nome, String CPF, String endereco, String numero, 
                   String complemento, String bairro, String cidade, String UF, 
                   String CEP, String email, boolean status, String telefone, 
                   String CNPJ, char sexo) {
        this.id_cli = id_cli;
        this.nome = nome;
        this.CPF = CPF;
        this.endereco = endereco;
        this.numero = numero;
        this.complemento = complemento;
        this.bairro = bairro;
        this.cidade = cidade;
        this.UF = UF;
        this.CEP = CEP;
        this.email = email;
        this.status = status;
        this.telefone = telefone;
        this.CNPJ = CNPJ;
        this.sexo = sexo;
    }

    public int getIdCli() {
        return id_cli;
    }

    public void setIdCli(int id_cli) {
        this.id_cli = id_cli;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        if (nome == null){
            System.out.println("Nome inválido!");
            return;
        }
        this.nome = nome;
    }

    public String getCPF() {
        return CPF;
    }

    public void setCPF(String CPF) {
    String cpf; 
    cpf = CPF.replace(".", "");
    cpf = cpf.replace("-", "");
    
    try{
      Long.parseLong(cpf);
    } catch(NumberFormatException e){
        System.out.println("CPF Inválido!");
      return;
    }

    int d1, d2;
    int digito1, digito2, resto;
    int digitoCPF;
    String nDigResult;

    d1 = d2 = 0;
    digito1 = digito2 = resto = 0;

    for (int nCount = 1; nCount < cpf.length() - 1; nCount++) {
      digitoCPF = Integer.valueOf(cpf.substring(nCount - 1, nCount)).intValue();

      d1 = d1 + (11 - nCount) * digitoCPF;

      d2 = d2 + (12 - nCount) * digitoCPF;
    };

    resto = (d1 % 11);

    if (resto < 2)
      digito1 = 0;
    else
      digito1 = 11 - resto;

    d2 += 2 * digito1;

    resto = (d2 % 11);

    if (resto < 2)
      digito2 = 0;
    else
      digito2 = 11 - resto;

    String nDigVerific = cpf.substring(cpf.length() - 2, cpf.length());
    nDigResult = String.valueOf(digito1) + String.valueOf(digito2);
    boolean isValid =  nDigVerific.equals(nDigResult);
    if (!isValid){
        System.out.println("CPF Inválido!");
    return;
    }
        this.CPF = CPF;
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

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public boolean isStatus() {
        return status;
    }

    public void setStatus(boolean status) {
        this.status = status;
    }

    public String getTelefone() {
        return telefone;
    }

    public void setTelefone(String telefone) {
        this.telefone = telefone;
    }

    public String getCNPJ() {
        return CNPJ;
    }

    public void setCNPJ(String CNPJ) {
        this.CNPJ = CNPJ;
    }

    public char getSexo() {
        return sexo;
    }

    public void setSexo(char sexo) {
        this.sexo = sexo;
    }
    
    public boolean isValidName(String nome){
        return nome == null;
    }
}
