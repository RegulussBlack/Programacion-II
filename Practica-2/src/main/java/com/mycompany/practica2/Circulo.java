/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.practica2;
import javax.swing.*;
import java.awt.*;
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

    public void dibujaCirculo(Graphics g) {
        g.setColor(Color.RED);
        int diametro = (int) (2 * radio);
        g.drawOval((int) (centro.x - radio), (int) (centro.y - radio), diametro, diametro);
    }

    public String toString() {
        return "Círculo con centro en " + centro + " y radio " + radio;
    }
}
