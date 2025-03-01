import math
import matplotlib.pyplot as plt

class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def coord_cartesianas(self) -> tuple[float, float]:
        return (self.x, self.y)

    def coord_polares(self) -> tuple[float, float]:
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
        """Dibuja la línea en la gráfica de matplotlib."""
        ax.plot([self.p1.x, self.p2.x], [self.p1.y, self.p2.y], 'bo-', label="Línea")  # 'bo-' = blue circles + line

class Circulo:
    def __init__(self, c: Punto, r: float):
        self.centro = c
        self.radio = r

    def __str__(self) -> str:
        return f"Círculo con centro en {self.centro} y radio {self.radio:.2f}"

    def dibujaCirculo(self, ax):
        """Dibuja el círculo en la gráfica de matplotlib."""
        circulo = plt.Circle((self.centro.x, self.centro.y), self.radio, color='r', fill=False, label="Círculo")
        ax.add_patch(circulo)



# Punto
p = Punto(2, 3)
print(p) 

print("Coordenadas Cartesianas:", p.coord_cartesianas())  
print("Coordenadas Polares:", p.coord_polares())  

# Línea 
p1 = Punto(0, 0)
p2 = Punto(3, 5)
linea = Linea(p1, p2)
print(linea)

# Círculo
circulo = Circulo(p1, 7.0)  
print(circulo)

# gráfica
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')  # Para que no se deforme el círculo
ax.grid(True)

# Dibujar
linea.dibujaLinea(ax)
circulo.dibujaCirculo(ax)

# Etiquetas y mostrar gráfico
ax.legend()
plt.show()
