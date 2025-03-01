# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 11:42:42 2025

@author: Fabricio
"""

class Cola:
    def __init__(self, n):
        self.arreglo = [0] * n  
        self.inicio = -1        
        self.fin = -1           
        self.n = n              

    # Método: insert (insertar)
    def insert(self, e: int) -> None:
        if not self.isFull():
            if self.isEmpty():
                self.inicio = 0  
            self.fin = (self.fin + 1) % self.n  
            self.anreglo[self.fin] = e
        else:
            print("La cola está llena, no se puede insertar.")

    # Método: remove (remover)
    def remove(self) -> int:
        if not self.isEmpty():
            elemento = self.anreglo[self.inicio]
            if self.inicio == self.fin:
                self.inicio = -1  
                self.fin = -1
            else:
                self.inicio = (self.inicio + 1) % self.n  
            return elemento
        else:
            print("La cola está vacía, no se puede remover.")
            return -1 

    # Método: peek (ver el primer elemento)
    def peek(self) -> int:
        if not self.isEmpty():
            return self.anreglo[self.inicio]
        else:
            print("La cola está vacía, no hay elementos.")
            return -1  

    # Método: isEmpty (verificar si está vacía)
    def isEmpty(self) -> bool:
        return self.inicio == -1

    # Método: isFull (verificar si está llena)
    def isFull(self) -> bool:
        return (self.fin + 1) % self.n == self.inicio

    # Método: size (tamaño actual de la cola)
    def size(self) -> int:
        if self.isEmpty():
            return 0
        if self.inicio <= self.fin:
            return self.fin - self.inicio + 1
        else:
            return self.n - self.inicio + self.fin + 1