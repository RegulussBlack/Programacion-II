/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package practica8;

/**
 *
 * @author Fabricio
 */
public class D extends A {
    B b;
    
    public D(int x, int y, int z) {
        super(x, z);
        this.b = new B(y, z);
    }
    
    public void incrementaXYZ() {
        x++;
        b.y++;
        z++;
        b.z++;
    }
    
    public int getY() {
        return b.y;
    }
    
    public int getBZ() {
        return b.z;
    }
}