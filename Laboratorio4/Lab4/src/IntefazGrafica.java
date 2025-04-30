/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;
/**
 *
 * @author Fabricio
 */
public class IntefazGrafica {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
    JFrame ventana = new JFrame("Figuras Geométricas");
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setSize(500, 400);
        ventana.setLayout(new BorderLayout());

        // resultados
        JTextArea areaTexto = new JTextArea();
        areaTexto.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(areaTexto);

        //  generar figuras
        JButton botonGenerar = new JButton("Generar Figuras Aleatorias");
        botonGenerar.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                areaTexto.setText(""); 
                Figura[] figuras = generarFigurasAleatorias(5); 
                
                for (Figura figura : figuras) {
                    areaTexto.append("----------------------\n");
                    areaTexto.append(figura + "\n");
                    areaTexto.append(String.format("Área: %.2f\n", figura.area()));
                    areaTexto.append(String.format("Perímetro: %.2f\n", figura.perimetro()));
                    
                    if (figura instanceof Coloreado) {
                        areaTexto.append(((Coloreado) figura).comoColorear() + "\n");
                    }
                }
            }
        });

        // componentes a la ventana
        ventana.add(scrollPane, BorderLayout.CENTER);
        ventana.add(botonGenerar, BorderLayout.SOUTH);

        // Mostrar ventana
        ventana.setVisible(true);
    }

    // figuras aleatorias (Cuadrados o Círculos)
    private static Figura[] generarFigurasAleatorias(int cantidad) {
        Random random = new Random();
        Figura[] figuras = new Figura[cantidad];
        
        for (int i = 0; i < cantidad; i++) {
            String color = "Color" + (i + 1);
            if (random.nextBoolean()) { 
                double lado = 1 + random.nextDouble() * 9; 
                figuras[i] = new Cuadrado(color, lado);
            } else {
                double radio = 1 + random.nextDouble() * 9; 
                figuras[i] = new Circulo(color, radio);
            }
        }
        return figuras;
    }
}
