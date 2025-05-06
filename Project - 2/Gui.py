import tkinter as tk
from tkinter import filedialog, messagebox
from ListaReproduccion import ListaReproduccion
from Reproductor import Reproductor
import os

class Interfaz:
    def __init__(self):
        self.lista = ListaReproduccion()
        self.reproductor = Reproductor()

        self.ventana = tk.Tk()
        self.ventana.title("🎶 Mi Reproductor de Música")
        self.ventana.geometry("460x550")
        self.ventana.configure(bg="#ffe6f0")

        
        tk.Label(self.ventana, text="🎧 Reproductor🎧", font=("Helvetica", 18, "bold"), bg="#ffe6f0", fg="#cc0066").pack(pady=10)

        
        self.lista_box = tk.Listbox(self.ventana, width=50, height=10, font=("Arial", 10), bg="#fff0f5", fg="#660033", selectbackground="#ffb3d9", selectforeground="black")
        self.lista_box.pack(pady=15)

        
        self.etiqueta_cancion = tk.Label(self.ventana, text="🎵 Canción actual: Ninguna", font=("Arial", 12), bg="#ffe6f0", fg="#800040")
        self.etiqueta_cancion.pack(pady=5)

        # Botones
        controles = tk.Frame(self.ventana, bg="#ffe6f0")
        controles.pack(pady=15)

        botones = [
            ("📂 Cargar Canciones", self.cargar_canciones), 
            ("▶️ Reproducir", self.reproducir_cancion),
            ("⏸️ Pausar", self.pausar),
            ("⏹️ Detener", self.detener),
            ("🔁 Siguiente", self.siguiente),
            ("🔙 Anterior", self.anterior),
            ("❌ Eliminar", self.eliminar),
        ]

        for i, (texto, accion) in enumerate(botones):
            tk.Button(controles, text=texto, command=accion, width=13, font=("Arial", 10), bg="#ffb3d9", fg="black", relief="groove").grid(row=i // 2, column=i % 2, padx=10, pady=6)

        
        tk.Label(self.ventana, text="🎼 Hecho con ❤️ ", font=("Arial", 9, "italic"), bg="#ffe6f0", fg="#800040").pack(pady=15)

    def cargar_canciones(self):
        
        carpeta = filedialog.askdirectory(title="Selecciona una carpeta con canciones")
        if carpeta:
            archivos = [f for f in os.listdir(carpeta) if f.endswith('.mp3')]  
            if archivos:
                for archivo in archivos:
                    ruta = os.path.join(carpeta, archivo)
                    nombre = archivo
                    artista = "Desconocido"
                    duracion = "3:00"  #
                    self.lista.agregar_cancion(nombre, artista, duracion, ruta)
                self.actualizar_lista()
            else:
                messagebox.showinfo("Aviso", "No se encontraron archivos .mp3 en la carpeta seleccionada.")
        else:
            messagebox.showinfo("Aviso", "No se seleccionó ninguna carpeta.")

    def actualizar_lista(self):
        self.lista_box.delete(0, tk.END)
        for cancion in self.lista.mostrar_lista():
            self.lista_box.insert(tk.END, cancion)
        actual = self.lista.obtener_cancion_actual()
        if actual:
            self.etiqueta_cancion.config(text=f"🎵 Canción actual: {actual.nombre}")

    def reproducir_cancion(self):
        actual = self.lista.obtener_cancion_actual()
        if actual:
            self.reproductor.reproducir(actual.ruta)
            self.etiqueta_cancion.config(text=f"🎵 Reproduciendo: {actual.nombre}")
        else:
            messagebox.showinfo("Aviso", "No hay canción cargada.")

    def pausar(self):
        self.reproductor.pausar()
        self.etiqueta_cancion.config(text="⏸️ Pausado")

    def detener(self):
        self.reproductor.detener()
        self.etiqueta_cancion.config(text="⏹️ Detenido")

    def siguiente(self):
        self.lista.avanzar()
        self.reproducir_cancion()
        self.actualizar_lista()

    def anterior(self):
        self.lista.retroceder()
        self.reproducir_cancion()
        self.actualizar_lista()

    def eliminar(self):
        self.lista.eliminar_cancion_actual()
        self.actualizar_lista()

    def ejecutar(self):
        self.ventana.mainloop()
