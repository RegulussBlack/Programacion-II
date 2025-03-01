# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 11:33:52 2025

@author: Fabricio
"""

class Pila:
    def __init__(self, n):
        self.arreglo = [0] * n 
        self.top = -1           
        self.n = n            

    # Método: push (apilar)
    def push(self, e: int) -> None:
        if not self.isFull():
            self.top += 1
            self.arreglo[self.top] = e
        else:
            print("La pila está llena, no se puede apilar.")

    # Método: pop (desapilar)
    def pop(self) -> int:
        if not self.isEmpty():
            elemento = self.arreglo[self.top]
            self.top -= 1
            return elemento
        else:
            print("La pila está vacía, no se puede desapilar.")
            return -1  # Valor de retorno por defecto en caso de pila vacía

    # Método: peek (ver tope)
    def peek(self) -> int:
        if not self.isEmpty():
            return self.arreglo[self.top]
        else:
            print("La pila está vacía, no hay tope.")
            return -1  # Valor de retorno por defecto en caso de pila vacía

    # Método: isEmpty (verificar si está vacía)
    def isEmpty(self) -> bool:
        return self.top == -1

    # Método: isFull (verificar si está llena)
    def isFull(self) -> bool:
        return self.top == self.n - 1