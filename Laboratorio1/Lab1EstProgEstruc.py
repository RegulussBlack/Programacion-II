# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 16:00:55 2025

@author: Fabricio
"""

import math

def promedio(numeros):
    return sum(numeros) / len(numeros)

def desviacion(numeros, media):
    return math.sqrt(sum((x - media) ** 2 for x in numeros) / (len(numeros) - 1))

# Metemos los datos
numeros = list(map(float, input("Ingrese 10 números: ").split()))

media = promedio(numeros)
desv = desviacion(numeros, media)

print(f"El promedio es {media:.2f}")
print(f"La desviación estándar es {desv:.5f}")
