class NodoCancion:
    def __init__(self, nombre, artista, duracion, ruta):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion
        self.ruta = ruta
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"🎵 {self.nombre} - {self.artista} ({self.duracion})"
