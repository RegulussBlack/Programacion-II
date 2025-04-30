# -*- coding: utf-8 -*-
"""
Spyder Editor

Faboo Scripts.
"""
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class Boleto:
    def __init__(self, numero):
        self.numero = numero
    
    def get_precio(self):
        return 0
    
    def __str__(self):
        return f"[Boleto {self.numero}] Tipo: {self.__class__.__name__}, Precio: {self.get_precio():.1f} Bs"

class Palco(Boleto):
    def get_precio(self):
        return 100.0

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion
    
    def get_precio(self):
        return 50.0 if self.dias_anticipacion >= 10 else 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        self.dias_anticipacion = dias_anticipacion
    
    def get_precio(self):
        return 25.0 if self.dias_anticipacion >= 10 else 30.0

class TeatroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teatro Municipal")
        self.root.geometry("450x550")
        
        # Variables
        self.numero_boleto = 1
        self.total = 0.0
        
        # Cargar imagen
        try:
            img = Image.open("teatro.jpg")
            img = img.resize((250, 150))
            self.logo = ImageTk.PhotoImage(img)
            tk.Label(self.root, image=self.logo).pack()
        except:
            tk.Label(self.root, text="Teatro Municipal", font=("Arial", 16)).pack()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Marco principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=10)
        
        # Número de boleto (¡AHORA VISIBLE!)
        tk.Label(main_frame, text=f"Número de boleto actual: {self.numero_boleto}", 
                font=("Arial", 10)).pack()
        
        # Tipo de boleto
        tk.Label(main_frame, text="Seleccione tipo de boleto:").pack()
        
        self.tipo_boleto = tk.StringVar(value="Palco")
        
        tk.Radiobutton(main_frame, text="Palco - Bs 100.00", 
                      variable=self.tipo_boleto, value="Palco").pack(anchor="w")
        
        tk.Radiobutton(main_frame, text="Platea - Bs 50.00 (10+ días) / Bs 60.00", 
                      variable=self.tipo_boleto, value="Platea").pack(anchor="w")
        
        tk.Radiobutton(main_frame, text="Galería - Bs 25.00 (10+ días) / Bs 30.00", 
                      variable=self.tipo_boleto, value="Galería").pack(anchor="w")
        
        # Días de anticipación
        tk.Label(main_frame, text="Días de anticipación (para Platea/Galería):").pack()
        self.dias_entry = tk.Entry(main_frame)
        self.dias_entry.pack()
        self.dias_entry.insert(0, "0")
        
        # Botones
        tk.Button(main_frame, text="Vender Boleto", command=self.vender_boleto).pack(pady=10)
        tk.Button(main_frame, text="Salir", command=self.root.quit).pack()
        
        # Área de información
        tk.Label(main_frame, text="Registro de ventas:").pack()
        self.info_text = tk.Text(main_frame, height=12, width=50)
        self.info_text.pack()
        self.info_text.insert(tk.END, "=== Boletos Vendidos ===\n\n")
    
    def vender_boleto(self):
        try:
            tipo = self.tipo_boleto.get()
            dias = int(self.dias_entry.get())
            
            # Validación
            if tipo in ["Platea", "Galería"] and dias < 0:
                raise ValueError("Los días deben ser ≥ 0")
            
            # Crear boleto
            if tipo == "Palco":
                boleto = Palco(self.numero_boleto)
            elif tipo == "Platea":
                boleto = Platea(self.numero_boleto, dias)
            else:
                boleto = Galeria(self.numero_boleto, dias)
            
            # Actualizar sistema
            self.total += boleto.get_precio()
            self.info_text.insert(tk.END, f"{boleto}\n")
            self.info_text.insert(tk.END, f"--> Total acumulado: {self.total:.2f} Bs\n\n")
            
            # Actualizar número para próximo boleto
            self.numero_boleto += 1
            self.update_boleto_number()  # Actualizar visualización
            
        except ValueError as e:
            messagebox.showerror("Error", f"Dato inválido: {str(e)}")
    
    def update_boleto_number(self):
        # Actualizar el label que muestra el número
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                for child in widget.winfo_children():
                    if isinstance(child, tk.Label) and "Número de boleto actual" in child.cget("text"):
                        child.config(text=f"Número de boleto actual: {self.numero_boleto}")
                        break

if __name__ == "__main__":
    root = tk.Tk()
    app = TeatroApp(root)
    root.mainloop()