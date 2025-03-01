# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt


class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def coord_cartesianas(self) :
        return (self.x, self.y)

    def coord_polares(self) :
        radio = math.sqrt(self.x**2 + self.y**2)  
        angulo = math.atan2(self.y, self.x)  
        return (radio, math.degrees(angulo))  

    def __str__(self) -> str:
        return f"Punto({self.x}, {self.y})"

class Linea:
    def __init__(self, p1: Punto, p2: Punto):
        self.p1 = p1
        self.p2 = p2

    def __str__(self) -> str:
        return f"Línea de {self.p1} a {self.p2}"

    def dibujaLinea(self, ax):
        ax.plot([self.p1.x, self.p2.x], [self.p1.y, self.p2.y], 'bo-', label="Línea")
        ax.set_xlim(-10, 20)
        ax.set_ylim(-10, 20)
        ax.set_aspect('equal')
        ax.grid(True)
        ax.legend()
        ax.set_title("Gráfico de Línea")

class Circulo:
    def __init__(self, c: Punto, r: float):
        if r <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.centro = c
        self.radio = r

    def __str__(self) -> str:
        return f"Círculo con centro en {self.centro} y radio {self.radio:.2f}"

    def dibujaCirculo(self, ax):
        circulo = plt.Circle((self.centro.x, self.centro.y), self.radio, color='r', fill=False, label="Círculo")
        ax.add_patch(circulo)
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_aspect('equal')
        ax.grid(True)
        ax.legend()
        ax.set_title("Gráfico de Círculo")

# Creación de objetos
p1 = Punto(0, 0)
p2 = Punto(5, 5)
linea = Linea(p1, p2)
circulo = Circulo(p1, 5.0)

# Gráfico de Línea
fig1, ax1 = plt.subplots()
linea.dibujaLinea(ax1)
plt.show()

# Gráfico de Círculo
fig2, ax2 = plt.subplots()
circulo.dibujaCirculo(ax2)
plt.show()
