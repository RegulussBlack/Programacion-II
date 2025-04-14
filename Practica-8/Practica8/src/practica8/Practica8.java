/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package practica8;

/**
 *
 * @author Fabricio
 */
public class Practica8 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        
       
        A a = new A(1, 2);
        B b = new B(3, 4);
        D d = new D(5, 6, 7);

       
        System.out.println("\nal comienzo:");
        System.out.println("A: x=" + a.x + ", z=" + a.z);
        System.out.println("B: y=" + b.y + ", z=" + b.z);
        System.out.println("D: x=" + d.x + ", y=" + d.getY() + ", z=" + d.z);

       
        a.incrementaXZ();
        a.incrementaZ();
        System.out.println("\nOperaciones en A:");
        System.out.println("A: x=" + a.x + ", z=" + a.z);

        
        b.incrementaYZ();
        b.incrementaZ();
        System.out.println("\nOperaciones en B:");
        System.out.println("B: y=" + b.y + ", z=" + b.z);

       
        d.incrementaXYZ();
        d.incrementaXZ();
        d.b.incrementaYZ();
        System.out.println("\nOperaciones en D:");
        System.out.println("D: x=" + d.x + ", y=" + d.getY() + ", z=" + d.z);
    }
    
}
