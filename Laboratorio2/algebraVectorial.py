# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 15:13:47 2025

@author: Fabricio
"""
import math

class AlgebraVectorial:
    def __init__(self, *componentes):
        """Constructor que acepta 1 a n componentes"""
        self.componentes = list(componentes)
        self.dimension = len(componentes)
    
    def __str__(self):
        return f"Vector{self.dimension}D({', '.join(map(str, self.componentes))})"
    
    def __add__(self, other):
        """Sobrecarga del operador + para suma de vectores"""
        if self.dimension != other.dimension:
            raise ValueError("Los vectores deben tener la misma dimensión para sumarse")
        return AlgebraVectorial(*[a + b for a, b in zip(self.componentes, other.componentes)])
    
    def __sub__(self, other):
        """Sobrecarga del operador - para resta de vectores"""
        if self.dimension != other.dimension:
            raise ValueError("Los vectores deben tener la misma dimensión para restarse")
        return AlgebraVectorial(*[a - b for a, b in zip(self.componentes, other.componentes)])
    
    def __mul__(self, other):
        """Sobrecarga del operador * para producto punto y producto por escalar"""
        if isinstance(other, (int, float)):
            # Producto por escalar
            return AlgebraVectorial(*[a * other for a in self.componentes])
        elif isinstance(other, AlgebraVectorial):
            # Producto punto
            if self.dimension != other.dimension:
                raise ValueError("Los vectores deben tener la misma dimensión para producto punto")
            return sum(a * b for a, b in zip(self.componentes, other.componentes))
        else:
            raise TypeError("Operación no soportada")
    
    def modulo(self):
        """Calcula el módulo del vector"""
        return math.sqrt(sum(a**2 for a in self.componentes))
    
    # Métodos
    def es_perpendicular(self, other, metodo=1):
        """Determina si dos vectores son perpendiculares usando diferentes métodos"""
        if metodo == 1:
            # Método 1: |a + b| = |a - b|
            return math.isclose((self + other).modulo(), (self - other).modulo())
        elif metodo == 2:
            # Método 2: |a - b| = |b - a| (siempre verdadero, no es buen método)
            return math.isclose((self - other).modulo(), (other - self).modulo())
        elif metodo == 3:
            # Método 3: a · b = 0
            return math.isclose(self * other, 0)
        elif metodo == 4:
            # Método 4: |a + b|² = |a|² + |b|²
            suma_mod = (self + other).modulo()**2
            return math.isclose(suma_mod, self.modulo()**2 + other.modulo()**2)
        else:
            raise ValueError("Método no válido. Use 1, 2, 3 o 4")
    
    # Métodos 
    def es_paralelo(self, other, metodo=1):
        """Determina si dos vectores son paralelos usando diferentes métodos"""
        if metodo == 1:
            # Método 1: a = r*b (existe un escalar r tal que...)
            if any(b == 0 for b in other.componentes):
                # Evitar división por cero
                ratios = [a / b for a, b in zip(self.componentes, other.componentes) if b != 0]
                if not ratios:
                    return True  # ambos vectores son cero en todas componentes no cero de other
                return all(math.isclose(r, ratios[0]) for r in ratios)
            else:
                r = self.componentes[0] / other.componentes[0]
                return all(math.isclose(a, b * r) for a, b in zip(self.componentes, other.componentes))
        elif metodo == 2:
            # Método 2: a × b = 0 (solo para R3)
            if self.dimension != 3 or other.dimension != 3:
                raise ValueError("El producto cruz solo está definido para R3")
            # Calculamos el producto cruz
            a1, a2, a3 = self.componentes
            b1, b2, b3 = other.componentes
            cruz = [
                a2 * b3 - a3 * b2,
                a3 * b1 - a1 * b3,
                a1 * b2 - a2 * b1
            ]
            return all(math.isclose(c, 0) for c in cruz)
        else:
            raise ValueError("Método no válido. Use 1 o 2")
    
    def proyeccion(self, other):
        """Calcula la proyección ortogonal de self sobre other"""
        producto_punto = self * other
        modulo_other_cuadrado = other.modulo() ** 2
        if modulo_other_cuadrado == 0:
            raise ValueError("No se puede proyectar sobre el vector cero")
        factor = producto_punto / modulo_other_cuadrado
        return other * factor
    
    def componente(self, other):
        """Calcula el componente de self en la dirección de other"""
        producto_punto = self * other
        modulo_other = other.modulo()
        if modulo_other == 0:
            raise ValueError("No se puede calcular componente sobre el vector cero")
        return producto_punto / modulo_other


# main
if __name__ == "__main__":
    # Crear vectores
    v1 = AlgebraVectorial(1, 0, 2, -1)
    v2 = AlgebraVectorial(0, 3, 1, 2)
    v3 = AlgebraVectorial(2, 0, 4, -2)  
    v4 = AlgebraVectorial(1, 1, 0)      
    
    print("Vectores creados:")
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v3 = {v3}")
    print(f"v4 = {v4}")
    
    #  perpendicularidad
    print("\nPruebas de perpendicularidad (v1 y v2):")
    for metodo in range(1, 5):
        print(f"Método {metodo}: {v1.es_perpendicular(v2, metodo)}")
    
    # paralelismo
    print("\nPruebas de paralelismo (v1 y v3):")
    print(f"Método 1: {v1.es_paralelo(v3, 1)}")
    
    #  R3 para producto cruz
    v5 = AlgebraVectorial(1, 0, 0)
    v6 = AlgebraVectorial(2, 0, 0)
    print("\nPruebas de paralelismo en R3 (v5 y v6):")
    print(f"Método 2 (producto cruz): {v5.es_paralelo(v6, 2)}")
    
    #  proyección y componente
    print("\nProyección de v1 sobre v2:")
    print(v1.proyeccion(v2))
    
    print("\nComponente de v1 en dirección de v2:")
    print(v1.componente(v2))