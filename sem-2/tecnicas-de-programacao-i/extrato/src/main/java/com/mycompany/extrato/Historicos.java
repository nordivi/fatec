/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.extrato;

/**
 *
 * @author Alunos
 */
public class Historicos {
    private int id_his; 
    private String historico; 

    public Historicos(int id_his, String historico) {
        this.id_his = id_his;
        this.historico = historico;
    }

    public int getIdHis() {
        return id_his;
    }

    public void setIdHis(int id_his) {
        this.id_his = id_his;
    }

    public String getHistorico() {
        return historico;
    }

    public void setHistorico(String historico) {
        this.historico = historico;
    }
}