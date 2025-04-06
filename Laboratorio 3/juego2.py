# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 12:33:06 2025

@author: Fabricio
"""


import random

class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
    
    def reiniciaPartida(self):
        self.numeroDeVidas = 3
    
    def actualizaRecord(self):
        self.record += 1
    
    def quitaVida(self):
        if self.numeroDeVidas > 0:
            self.numeroDeVidas -= 1
            return True
        return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0
    
    def validaNumero(self, numero):
        return 0 <= numero <= 10
    
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        
        while True:
            try:
                numero = int(input("Adivina un número entre 0 y 10: "))
                
                if not self.validaNumero(numero):
                    print("Error: El número debe estar entre 0 y 10")
                    continue
                    
                if numero == self.numeroAAdivinar:
                    print("Acertaste!!")
                    self.actualizaRecord()
                    return
                else:
                    if not self.quitaVida():
                        print("¡Game Over!")
                        return
                    
                    if numero < self.numeroAAdivinar:
                        print("El número a adivinar es mayor")
                    else:
                        print("El número a adivinar es menor")
            except ValueError:
                print("Error: Debes ingresar un número entero")

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if not super().validaNumero(numero):
            return False
        if numero % 2 == 0:
            return True
        else:
            print("Error: El número debe ser par")
            return False

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if not super().validaNumero(numero):
            return False
        if numero % 2 != 0:
            return True
        else:
            print("Error: El número debe ser impar")
            return False

class Aplicacion:
    @staticmethod
    def main():
        juegos = [
            JuegoAdivinaNumero(3),
            JuegoAdivinaPar(3),
            JuegoAdivinaImpar(3)
        ]
        
        for juego in juegos:
            print(f"\n--- Iniciando {juego.__class__.__name__} ---")
            juego.juega()

if __name__ == "__main__":
    Aplicacion.main()