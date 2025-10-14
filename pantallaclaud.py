import tkinter as tk
from tkinter import messagebox


def mostrar_mensaje():
    nombre = entrada_nombre.get().strip()
    if nombre:
        messagebox.showinfo("Bienvenido", f"Hola, {nombre}! Gracias por visitar PantallaClaud.")
    else:
        messagebox.showwarning("Atención", "Por favor ingresa tu nombre para continuar.")


ventana = tk.Tk()
ventana.title("PantallaClaud")
ventana.geometry("400x250")
ventana.resizable(False, False)

marco = tk.Frame(ventana, padx=20, pady=20)
marco.pack(expand=True)

etiqueta_titulo = tk.Label(marco, text="Bienvenido a PantallaClaud", font=("Arial", 16, "bold"))
etiqueta_titulo.pack(pady=(0, 10))

etiqueta_nombre = tk.Label(marco, text="Ingresa tu nombre:", font=("Arial", 12))
etiqueta_nombre.pack(anchor="w")

entrada_nombre = tk.Entry(marco, font=("Arial", 12))
entrada_nombre.pack(fill="x", pady=(0, 10))

boton_saludar = tk.Button(marco, text="Saludar", font=("Arial", 12), command=mostrar_mensaje)
boton_saludar.pack(fill="x")

boton_salir = tk.Button(marco, text="Salir", font=("Arial", 12), command=ventana.destroy)
boton_salir.pack(fill="x", pady=(10, 0))

ventana.mainloop()
