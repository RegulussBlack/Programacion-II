/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.practica1;

/**
 *
 * @author Fabricio
 */
public class Punto {
    
    public float x;
    public float y;

 
    public Punto(float x, float y) {
        this.x = x;
        this.y = y;
    }

   
    public String coordCartesianas() {
        return "(" + this.x + ", " + this.y + ")";
    }

   
    private double potencia(double base, int exponente) {
        double resultado = 1;
        for (int i = 0; i < exponente; i++) {
            resultado *= base;
        }
        return resultado;
    }

   
    private double raizCuadrada(double numero) {
        double aproximacion = numero;
        double precision = 1e-7; // Precisión deseada
        while (Math.abs(aproximacion * aproximacion - numero) > precision) {
            aproximacion = (aproximacion + numero / aproximacion) / 2;
        }
        return aproximacion;
    }

 
    private double atan2(double y, double x) {
        if (x > 0) {
            return Math.atan(y / x);
        } else if (x < 0 && y >= 0) {
            return Math.atan(y / x) + Math.PI;
        } else if (x < 0 && y < 0) {
            return Math.atan(y / x) - Math.PI;
        } else if (x == 0 && y > 0) {
            return Math.PI / 2;
        } else if (x == 0 && y < 0) {
            return -Math.PI / 2;
        } else {
            throw new IllegalArgumentException("Indefinido para (0, 0)");
        }
    }

    
    public String coordPolares() {
        double r = raizCuadrada(potencia(this.x, 2) + potencia(this.y, 2)); 
        double theta = atan2(this.y, this.x); 
        double thetaGrados = theta * (180 / Math.PI); 
        return "(" + r + ", " + thetaGrados + ")";
    }


    @Override
    public String toString() {
        return "Punto(" + this.x + ", " + this.y + ")";
    }
    
}
