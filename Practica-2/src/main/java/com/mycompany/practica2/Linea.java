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
public class Linea {
    public Punto p1;
    public Punto p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    public void dibujaLinea(Graphics g) {
        g.setColor(Color.BLUE);
        g.drawLine((int) p1.x, (int) p1.y, (int) p2.x, (int) p2.y);
    }

    public String toString() {
        return "Línea de " + p1 + " a " + p2;
    }
    
}
