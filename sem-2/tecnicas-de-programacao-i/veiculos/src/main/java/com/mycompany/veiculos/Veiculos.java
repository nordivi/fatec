/*
* Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
*/
 
package com.mycompany.veiculos;
 
/**
*
* @author claud
*/
public class Veiculos {
 
    public static void main(String[] args) {
        //System.out.println("Hello World!");

// exibindo informações de apenas um atributo do veículo carro
 
        Veiculo carro = new CarroPasseio("ABC1234", "Toyota", "Corolla", "Prata", 2022, 2023, 5, 4);
        System.out.println("Numero do chassi do carro: "+carro.getChassi());
        System.out.println("Marca do carro: "+carro.getMarca());
        System.out.println("Modelo do carro: "+carro.getModelo());
        System.out.println("Cor do carro: "+carro.getCor());
        System.out.println("Ano de fabricacao do carro: "+carro.getAnoFabricacao());
        System.out.println("Ano de modelo do carro: "+carro.getAnoModelo());
        System.out.println("Tipo do carro: "+carro.getTipo()); 
// exibindo todas as informações dos atributos do veículo carro
        carro.exibirInformacoes();
        Veiculo caminhao = new Caminhao("DEF5678", "Scania", "R450", "Azul", 2021, 2022, 20.5, "Carreta");
        System.out.println("Numero do chassi do caminhao: "+caminhao.getChassi());
        System.out.println("Marca do caminhao: "+caminhao.getMarca());
        System.out.println("Modelo do caminhao: "+caminhao.getModelo());
        System.out.println("Cor do caminhao: "+caminhao.getCor());
        System.out.println("Ano de fabricacao do caminhao: "+caminhao.getAnoFabricacao());
        System.out.println("Ano de modelo do caminhao: "+caminhao.getAnoModelo());
        System.out.println("Tipo do caminhao: "+caminhao.getTipo()); 
// exibindo todas as informações dos atributos do veículo carro
        caminhao.exibirInformacoes();
        Veiculo onibus = new Onibus("GHI9012", "Mercedes", "O500", "Verde", 2020, 2021, 40, true);
        System.out.println("Numero do chassi do onibus: "+onibus.getChassi());
        System.out.println("Marca do onibus: "+onibus.getMarca());
        System.out.println("Modelo do onibus: "+onibus.getModelo());
        System.out.println("Cor do onibus: "+onibus.getCor());
        System.out.println("Ano de fabricacao do onibus: "+onibus.getAnoFabricacao());
        System.out.println("Ano de modelo do onibus: "+onibus.getAnoModelo());
        System.out.println("Tipo do onibus: "+onibus.getTipo()); 
// exibindo todas as informações dos atributos do veículo carro
        onibus.exibirInformacoes();
        // fazer a exibição de todas as informações de cada classe (carro, caminhao e onibus)
        // mostrando cada um dos atributos separados e depois mostrando todas as informações de cada veículo
 
        // criar os três objetos usando a herança (modelo acima) e mostrar somente
        // os atributos get que não apareceram nos objetos de Polimorfismo acima
        CarroPasseio carro2 = new CarroPasseio("ABC1234", "Toyota 2", "Corolla 2", "Prata 2", 2022, 2023, 5, 4);
        System.out.println("Numero de portas do carro: "+carro2.getNumeroPortas());
        System.out.println("Numero de portas do carro: "+carro2.getNumeroPassageiros());
 
        Caminhao caminhao2 = new Caminhao("DEF5678", "Scania", "R450", "Azul", 2021, 2022, 20.5, "Carreta");
        System.out.println("Capacidade de carga do Caminhao: "+caminhao2.getCapacidadeCarga());
        System.out.println("Tipo de carreta do Caminhao: "+caminhao2.getTipoCarreta());
 
        Onibus onibus2 = new Onibus("GHI9012", "Mercedes", "O500", "Verde", 2020, 2021, 40, true);
        System.out.println("Numero de passageiros do Onibus: "+onibus2.getNumeroPassageiros());
        System.out.println("Linha urbana para Onibus: "+onibus2.isLinhaUrbana());
 
    }
}