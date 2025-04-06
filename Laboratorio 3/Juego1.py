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
        self.numeroAAdivinar = random.randint(0, 10)
    
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        
        while True:
            numero = int(input("Adivina un número entre 0 y 10: "))
            
            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                return
            else:
                if not self.quitaVida():
                    return
                
                if self.quitaVida():
                    if numero < self.numeroAAdivinar:
                        print("El número a adivinar es mayor")
                    else:
                        print("El número a adivinar es menor")

# Clase Aplicacion
class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()

# Ejecutar
if __name__ == "__main__":
    Aplicacion.main()