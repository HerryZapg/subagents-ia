import tkinter as tk
from tkinter import messagebox


ESCENARIOS = {
    "Clásico": {
        "titulo": "Bienvenido a PantallaClaud",
        "descripcion": "Un espacio acogedor para saludarte.",
        "saludo_titulo": "Bienvenido",
        "saludo": "Hola, {nombre}! Gracias por visitar PantallaClaud.",
        "ventana_bg": "#f5f5f5",
        "marco_bg": "#ffffff",
        "texto_fg": "#333333",
        "boton_bg": "#4c9aff",
        "boton_fg": "#ffffff",
        "boton_activo_bg": "#1f7ae0",
        "boton_salir_bg": "#e04c4c",
        "boton_salir_activo_bg": "#c03939",
        "entrada_bg": "#ffffff",
        "entrada_fg": "#333333",
    },
    "Bosque": {
        "titulo": "Explora el Bosque",
        "descripcion": "Un escenario sereno entre árboles y naturaleza.",
        "saludo_titulo": "Bosque encantado",
        "saludo": "Hola, {nombre}! Disfruta la paz del bosque mágico.",
        "ventana_bg": "#d6f5d6",
        "marco_bg": "#c2e7c2",
        "texto_fg": "#1d4d1d",
        "boton_bg": "#2f855a",
        "boton_fg": "#ffffff",
        "boton_activo_bg": "#276749",
        "boton_salir_bg": "#b91c1c",
        "boton_salir_activo_bg": "#991b1b",
        "entrada_bg": "#ffffff",
        "entrada_fg": "#1d4d1d",
    },
    "Playa": {
        "titulo": "Relájate en la Playa",
        "descripcion": "Escucha las olas y siente la brisa marina.",
        "saludo_titulo": "Olas de bienvenida",
        "saludo": "Hola, {nombre}! Que la brisa marina te acompañe.",
        "ventana_bg": "#fff5d6",
        "marco_bg": "#ffe5b4",
        "texto_fg": "#7c4a03",
        "boton_bg": "#f59e0b",
        "boton_fg": "#ffffff",
        "boton_activo_bg": "#d97706",
        "boton_salir_bg": "#ea580c",
        "boton_salir_activo_bg": "#c2410c",
        "entrada_bg": "#fffaf0",
        "entrada_fg": "#7c4a03",
    },
}


def aplicar_escenario(nombre_escenario: str) -> None:
    """Aplica los estilos y textos del escenario seleccionado."""

    configuracion = ESCENARIOS[nombre_escenario]

    ventana.configure(bg=configuracion["ventana_bg"])
    marco.configure(bg=configuracion["marco_bg"])

    etiqueta_titulo.configure(
        text=configuracion["titulo"],
        bg=configuracion["marco_bg"],
        fg=configuracion["texto_fg"],
    )

    etiqueta_descripcion.configure(
        text=configuracion["descripcion"],
        bg=configuracion["marco_bg"],
        fg=configuracion["texto_fg"],
    )

    etiqueta_nombre.configure(bg=configuracion["marco_bg"], fg=configuracion["texto_fg"])

    selector_escenario.configure(
        bg=configuracion["boton_bg"],
        fg=configuracion["boton_fg"],
        activebackground=configuracion["boton_activo_bg"],
        activeforeground=configuracion["boton_fg"],
        highlightthickness=0,
    )

    menu_escenarios = selector_escenario["menu"]
    menu_escenarios.configure(
        bg=configuracion["marco_bg"],
        fg=configuracion["texto_fg"],
        activebackground=configuracion["boton_activo_bg"],
        activeforeground=configuracion["boton_fg"],
    )

    entrada_nombre.configure(
        bg=configuracion["entrada_bg"],
        fg=configuracion["entrada_fg"],
        insertbackground=configuracion["entrada_fg"],
    )

    boton_saludar.configure(
        bg=configuracion["boton_bg"],
        fg=configuracion["boton_fg"],
        activebackground=configuracion["boton_activo_bg"],
        activeforeground=configuracion["boton_fg"],
    )

    boton_salir.configure(
        bg=configuracion["boton_salir_bg"],
        fg="white",
        activebackground=configuracion["boton_salir_activo_bg"],
        activeforeground="white",
    )


def mostrar_mensaje():
    nombre = entrada_nombre.get().strip()
    escenario = escenario_actual.get()
    configuracion = ESCENARIOS[escenario]

    if nombre:
        mensaje = configuracion["saludo"].format(nombre=nombre)
        messagebox.showinfo(configuracion["saludo_titulo"], mensaje)
    else:
        messagebox.showwarning("Atención", "Por favor ingresa tu nombre para continuar.")


ventana = tk.Tk()
ventana.title("PantallaClaud")
ventana.geometry("420x320")
ventana.resizable(False, False)

marco = tk.Frame(ventana, padx=20, pady=20)
marco.pack(expand=True, fill="both")

escenario_actual = tk.StringVar(value=list(ESCENARIOS.keys())[0])

etiqueta_titulo = tk.Label(marco, font=("Arial", 16, "bold"))
etiqueta_titulo.pack(pady=(0, 6))

etiqueta_descripcion = tk.Label(marco, font=("Arial", 11))
etiqueta_descripcion.pack(pady=(0, 12))

selector_escenario = tk.OptionMenu(
    marco, escenario_actual, *ESCENARIOS.keys(), command=lambda _: aplicar_escenario(escenario_actual.get())
)
selector_escenario.configure(font=("Arial", 11), relief="flat")
selector_escenario.pack(fill="x", pady=(0, 12))

etiqueta_nombre = tk.Label(marco, text="Ingresa tu nombre:", font=("Arial", 12))
etiqueta_nombre.pack(anchor="w")

entrada_nombre = tk.Entry(marco, font=("Arial", 12))
entrada_nombre.pack(fill="x", pady=(0, 10))

boton_saludar = tk.Button(marco, text="Saludar", font=("Arial", 12), command=mostrar_mensaje)
boton_saludar.pack(fill="x")

boton_salir = tk.Button(marco, text="Salir", font=("Arial", 12), command=ventana.destroy)
boton_salir.pack(fill="x", pady=(10, 0))

aplicar_escenario(escenario_actual.get())

ventana.mainloop()
