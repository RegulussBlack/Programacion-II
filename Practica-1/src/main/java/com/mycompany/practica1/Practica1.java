/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.practica1;

/**
 *
 * @author Fabricio
 */
public class Practica1 {

    public static void main(String[] args) {
        Punto p = new Punto(3, 4);
        System.out.println(p); 
        System.out.println("Coordenadas Cartesianas: " + p.coordCartesianas());
        System.out.println("Coordenadas Polares: " + p.coordPolares()); 
        
        Circulo c = new Circulo(p, 5f);
        System.out.println(c.toString());
        c.dibujaCirculo();
    }
}
