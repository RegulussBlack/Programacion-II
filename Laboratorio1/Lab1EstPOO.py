# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 16:01:56 2025

@author: Fabricio
"""

import math

class Estadisticas:
    def __init__(self, numeros):
        self.numeros = numeros

    def promedio(self):
        return sum(self.numeros) / len(self.numeros)

    def desviacion(self):
        media = self.promedio()
        return math.sqrt(sum((x - media) ** 2 for x in self.numeros) / (len(self.numeros) - 1))

    def mostrar_resultados(self):
        print(f"El promedio es {self.promedio():.2f}")
        print(f"La desviación estándar es {self.desviacion():.5f}")

# Metemos datos
numeros = list(map(float, input("Ingrese 10 números: ").split()))
estadisticas = Estadisticas(numeros)
estadisticas.mostrar_resultados()
