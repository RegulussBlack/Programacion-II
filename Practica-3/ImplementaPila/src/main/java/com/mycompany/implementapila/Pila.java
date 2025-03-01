/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.implementapila;

/**
 *
 * @author Fabricio
 */
public class Pila {
    private long[] arreglo; 
    private int top;       
    private int n;         

    // Constructor
    public Pila(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.top = -1; 
    }

    // Método: push (apilar)
    public void push(long e) {
        if (!isFull()) {
            top++;
            arreglo[top] = e;
        } else {
            System.out.println("La pila está llena, no se puede apilar.");
        }
    }

    // Método: pop (desapilar)
    public long pop() {
        if (!isEmpty()) {
            long elemento = arreglo[top];
            top--;
            return elemento;
        } else {
            System.out.println("La pila está vacía, no se puede desapilar.");
            return -1; 
        }
    }

    // Método: peek (ver tope)
    public long peek() {
        if (!isEmpty()) {
            return arreglo[top];
        } else {
            System.out.println("La pila está vacía, no hay tope.");
            return -1; 
        }
    }

    // Método: isEmpty (verificar si está vacía)
    public boolean isEmpty() {
        return top == -1;
    }

    // Método: isFull (verificar si está llena)
    public boolean isFull() {
        return top == n - 1;
    }
}
    

