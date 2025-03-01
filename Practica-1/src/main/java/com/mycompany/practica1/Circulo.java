/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.practica1;

/**
 *
 * @author Fabricio
 */
public class Circulo {
    public Punto centro;
    public float radio;

    public Circulo(Punto centro, float radio) {
        this.centro = centro;
        this.radio = radio;
    }

    @Override
    public String toString() {
        return "Circulo{" + "centro=" + centro + ", radio=" + radio + '}';
    }
    
    public void dibujaCirculo(){
        System.out.println("Dibujando con centro en : " + this.centro.toString()+ " y radio : " + this.radio);
    }
    
}
