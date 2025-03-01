package com.mycompany.practica2;

import javax.swing.*;
import java.awt.*;

public class Practica2 {
    public static void main(String[] args) {
        Punto p1 = new Punto(0, 0);
        Punto p2 = new Punto(-5, -5);
        Linea linea = new Linea(p1, p2);
        Circulo circulo = new Circulo(new Punto(0,0), 5);

        // Ventanalínea
        JFrame ventanaLinea = new JFrame("Plano Cartesiano - Línea");
        ventanaLinea.setSize(600, 600);
        ventanaLinea.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventanaLinea.add(new PanelLinea(p1, p2));
        ventanaLinea.setVisible(true);

        // Ventanacírculo
        JFrame ventanaCirculo = new JFrame("Plano Cartesiano - Círculo");
        ventanaCirculo.setSize(600, 600);
        ventanaCirculo.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventanaCirculo.add(new PanelCirculo(p1, 5));
        ventanaCirculo.setVisible(true);
    }
}

// Panel  línea
class PanelLinea extends JPanel {
    private final Punto p1, p2;

    public PanelLinea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        int ancho = getWidth(), alto = getHeight();
        int centroX = ancho / 2, centroY = alto / 2;

        //  ejes
        g.setColor(Color.BLACK);
        g2.setStroke(new BasicStroke(2));
        g.drawLine(0, centroY, ancho, centroY);
        g.drawLine(centroX, 0, centroX, alto);

        //  línea
        g.setColor(Color.RED);
        int x1 = centroX + (int) (p1.x * 50), y1 = centroY - (int) (p1.y * 50);
        int x2 = centroX + (int) (p2.x * 50), y2 = centroY - (int) (p2.y * 50);
        g.drawLine(x1, y1, x2, y2);
    }
}

// dibujar el círculo
class PanelCirculo extends JPanel {
    private final Punto centro;
    private final int radio;

    public PanelCirculo(Punto centro, int radio) {
        this.centro = centro;
        this.radio = radio;
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        int ancho = getWidth(), alto = getHeight();
        int centroX = ancho / 2, centroY = alto / 2;

        // Dibujar ejes
        g.setColor(Color.BLACK);
        g2.setStroke(new BasicStroke(2));
        g.drawLine(0, centroY, ancho, centroY);
        g.drawLine(centroX, 0, centroX, alto);

        // Dibujar círculo
        g.setColor(Color.BLUE);
        int cx = centroX + (int) (centro.x * 50);
        int cy = centroY - (int) (centro.y * 50);
        int r = radio * 50;
        g.drawOval(cx - r, cy - r, 2 * r, 2 * r);
    }
}
