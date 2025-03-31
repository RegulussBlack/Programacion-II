# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 17:39:42 2025

@author: Fabricio
"""

import math

class Vector3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
    
   
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
           
            return Vector3D(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3D):
          
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Operación no soportada")
    
   
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
  
    def __xor__(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
  
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
   
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector3D()
        return Vector3D(self.x/mag, self.y/mag, self.z/mag)
    
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    
    def is_orthogonal_to(self, other):
        return abs(self * other) < 1e-10  
    
   
    def projection_onto(self, other):
        scalar = (self * other) / (other * other)
        return other * scalar
    
    
    def orthogonal_component_to(self, other):
        return self - self.projection_onto(other)


# main
if __name__ == "__main__":
    # Creación de vectores
    a = Vector3D(1, 2, 3)
    b = Vector3D(4, 5, 6)
    
    print("Vector a:", a)
    print("Vector b:", b)
    
    # Suma de vectores
    c = a + b
    print("\nSuma a + b:", c)
    
    # Multiplicación por escalar
    d = a * 2.5
    print("\nMultiplicación a * 2.5:", d)
    
    # Producto escalar
    dot_product = a * b
    print("\nProducto escalar a · b:", dot_product)
    
    # Producto vectorial
    cross_product = a ^ b
    print("\nProducto vectorial a × b:", cross_product)
    
    # Longitud del vector
    print("\nLongitud de a:", a.magnitude())
    
    # Vector normalizado
    print("\nVector a normalizado:", a.normalize())
    
    # Verificación de ortogonalidad
    print("\n¿a es ortogonal a b?:", a.is_orthogonal_to(b))
    
    # Vectores ortogonales de prueba
    ortho1 = Vector3D(1, 0, 0)
    ortho2 = Vector3D(0, 1, 0)
    print("¿(1,0,0) es ortogonal a (0,1,0)?:", ortho1.is_orthogonal_to(ortho2))
    
    # Proyección ortogonal
    print("\nProyección de a sobre b:", a.projection_onto(b))
    
    # Componente ortogonal
    print("Componente ortogonal de a sobre b:", a.orthogonal_component_to(b))