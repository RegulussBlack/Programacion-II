# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 22:11:38 2025

@author: Fabricio
"""
import math

class FiguraGeometrica:

   
    def area(self, *args):
        # Si se pasan 2 parámetros (radio y tipoFigura)
        if len(args) == 2:
            if args[1] == "circulo":
                return math.pi * args[0] * args[0]  #  círculo
            elif args[1] == "pentagono":
                return (1.0 / 4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * args[0] * args[0]  # pentágono
            elif args[1] == "hexagono":
                return 6 * (args[0] * args[0] * math.sqrt(3) / 4)  # hexágono
            return 0  #  ninguna de las figuras anteriores
        
        # Si se pasan 3 parámetros (base, altura y tipoFigura)
        elif len(args) == 3:
            if args[2] == "rectangulo":
                return args[0] * args[1]  #  rectángulo
            elif args[2] == "triangulo":
                return (args[0] * args[1]) / 2  # riángulo
            elif args[2] == "trapecio":
                return ((args[0] + args[1]) / 2) * args[2]  # trapecio
            return 0  # Si no es rectángulo, triángulo ni trapecio

        # Si se pasan 4 parámetros (Base, base, altura, y tipoFigura para trapecio)
        elif len(args) == 4 and args[3] == "trapecio":
            return ((args[0] + args[1]) / 2) * args[2]  # trapecio
        
        return 0  # En cualquier otro caso, retorna 0


# Crear objeto de la clase FiguraGeometrica
figura = FiguraGeometrica()


print("Círculo: ", figura.area(1, "circulo"))  # círculo 
print("Rectángulo: ", figura.area(2, 3, "rectangulo"))  #  rectángulo 
print("Triángulo rectángulo: ", figura.area(2, 4, "triangulo"))  # triángulo 
print("Trapecio: ", figura.area(5, 3, 2, "trapecio"))  # trapecio 
print("Pentágono: ", figura.area(5, "pentagono"))  #  pentágono 
print("Hexágono: ", figura.area(5, "hexagono"))  #  hexágono 
