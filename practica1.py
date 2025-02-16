# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:38:36 2025

@author: Fabricio
"""

import math

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return (self.x, self.y)

    def coord_polares(self):
        r = math.sqrt(self.x**2 + self.y**2)  
        theta = math.atan2(self.y, self.x)  
        return (r, math.degrees(theta))  

    def __str__(self):  
        return f"Punto({self.x}, {self.y})"

p = Punto(5.6, 4.4)
print(p) 
print("Coordenadas Cartesianas:", p.coord_cartesianas())  
print("Coordenadas Polares:", p.coord_polares())  