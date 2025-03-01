/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.implementacola;

/**
 *
 * @author Fabricio
 */
public class Cola {
    private long[] anreglo; 
    private int inicio;     
    private int fin;        
    private int n;          

    // Constructor
    public Cola(int n) {
        this.n = n;
        this.anreglo = new long[n];
        this.inicio = -1; 
        this.fin = -1;
    }

    // Método: insert (insertar)
    public void insert(long e) {
        if (!isFull()) {
            if (isEmpty()) {
                inicio = 0; 
            }
            fin = (fin + 1) % n; 
            anreglo[fin] = e;
        } else {
            System.out.println("La cola está llena, no se puede insertar.");
        }
    }

    // Método: remove (remover)
    public long remove() {
        if (!isEmpty()) {
            long elemento = anreglo[inicio];
            if (inicio == fin) {
                inicio = -1; 
                fin = -1;
            } else {
                inicio = (inicio + 1) % n; 
            }
            return elemento;
        } else {
            System.out.println("La cola está vacía, no se puede remover.");
            return -1; 
        }
    }

    // Método: peek (ver el primer elemento)
    public long peek() {
        if (!isEmpty()) {
            return anreglo[inicio];
        } else {
            System.out.println("La cola está vacía, no hay elementos.");
            return -1; 
        }
    }

    // Método: isEmpty (verificar si está vacía)
    public boolean isEmpty() {
        return inicio == -1;
    }

    // Método: isFull (verificar si está llena)
    public boolean isFull() {
        return (fin + 1) % n == inicio;
    }

    // Método: size (tamaño actual de la cola)
    public int size() {
        if (isEmpty()) {
            return 0;
        }
        if (inicio <= fin) {
            return fin - inicio + 1;
        } else {
            return n - inicio + fin + 1;
        }
    }
}
    

