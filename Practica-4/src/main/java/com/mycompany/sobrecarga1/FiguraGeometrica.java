package com.mycompany.sobrecarga1;

public class FiguraGeometrica {

    // Círculo
    double area(double radio, String tipoFigura) {
        if (tipoFigura.equalsIgnoreCase("circulo")) {
            return Math.PI * radio * radio;  
        }
        return 0;  
    }

    // Rectángulo
    double area(double base, double altura) {
        return base * altura;  
    }

    // Triángulo
    double area(double base, double altura, String tipoFigura) {
        if (tipoFigura.equals("triangulo")) {
            return (base * altura) / 2;  
        } else {
            return base * altura;  
        }
    }

    // Trapecio
    double area(double B, double b, double h, String tipoFigura) {
        if (tipoFigura.equals("trapecio")) {
            return ((B + b) / 2) * h;  
        } else {
            return 0;
        }
    }

    // Pentágono
    double area(double L) {
        return (1.0 / 4) * Math.sqrt(5 * (5 + 2 * Math.sqrt(5))) * L * L; 
    }

    public static void main(String[] args) {
        FiguraGeometrica f1 = new FiguraGeometrica();
        FiguraGeometrica f2 = new FiguraGeometrica();
        FiguraGeometrica f3 = new FiguraGeometrica();
        FiguraGeometrica f4 = new FiguraGeometrica();
        FiguraGeometrica f5 = new FiguraGeometrica();

        // Mostrar resultados
        System.out.println("Círculo: " + f1.area(3, "circulo"));  
        System.out.println("Rectángulo: " + f2.area(2, 3)); 
        System.out.println("Triángulo rectángulo: " + f3.area(2, 4, "triangulo"));  
        System.out.println("Trapecio: " + f4.area(5, 3, 2, "trapecio"));  
        System.out.println("Pentágono: " + f5.area(5));  
    }
}
