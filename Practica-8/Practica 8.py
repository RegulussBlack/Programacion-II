# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 21:40:52 2025

@author: Fabricio
"""

class A:
    def __init__(self, x, z):
        self.x = x
        self.z = z
    
    def incrementaXZ(self):
        self.x += 1
        self.z += 1
    
    def incrementaZ(self):
        self.z += 1


class B:
    def __init__(self, y, z):
        self.y = y
        self.z = z
    
    def incrementaYZ(self):
        self.y += 1
        self.z += 1
    
    def incrementaZ(self):
        self.z += 1


class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x, z)
        B.__init__(self, y, z)
    
    def incrementaXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1


if __name__ == "__main__":
  
    
   
    a = A(1, 2)
    b = B(3, 4)
    d = D(5, 6, 7)

   
    print("\nPrincipio:")
    print(f"A: x={a.x}, z={a.z}")
    print(f"B: y={b.y}, z={b.z}")
    print(f"D: x={d.x}, y={d.y}, z={d.z}")


    a.incrementaXZ()
    a.incrementaZ()
    print("\noperaciones en A:")
    print(f"A: x={a.x}, z={a.z}")


    b.incrementaYZ()
    b.incrementaZ()
    print("\noperaciones en B:")
    print(f"B: y={b.y}, z={b.z}")

  
    d.incrementaXYZ()
    d.incrementaXZ()
    d.incrementaYZ()  
    print("\noperaciones en D:")
    print(f"D: x={d.x}, y={d.y}, z={d.z}")