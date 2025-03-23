# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 15:57:26 2025

@author: Fabricio
"""
#Programacion Estructurada
import math

def get_discriminante(a, b, c):
    return b**2 - 4*a*c

def get_raiz1(a, b, discriminante):
    return (-b + math.sqrt(discriminante)) / (2 * a)

def get_raiz2(a, b, discriminante):
    return (-b - math.sqrt(discriminante)) / (2 * a)

def resolver_ecuacion(a, b, c):
    discriminante = get_discriminante(a, b, c)
    
    if discriminante > 0:
        r1 = get_raiz1(a, b, discriminante)
        r2 = get_raiz2(a, b, discriminante)
        print(f"La ecuación tiene dos raíces {r1:.5f} y {r2:.5f}")
    elif discriminante == 0:
        r1 = -b / (2 * a)
        print(f"La ecuación tiene una raíz {r1:.5f}")
    else:
        print("La ecuación no tiene raíces reales")

# Metemos los datos
a, b, c = map(float, input("Ingrese a, b, c: ").split())
resolver_ecuacion(a, b, c)
