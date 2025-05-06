from NodoCancion import NodoCancion  

class ListaReproduccion:
    def __init__(self):
        self.actual = None

    def agregar_cancion(self, nombre, artista, duracion, ruta):
        nueva = NodoCancion(nombre, artista, duracion, ruta)
        if self.actual is None:
            self.actual = nueva
            self.actual.siguiente = self.actual
            self.actual.anterior = self.actual
        else:
            ultimo = self.actual.anterior
            ultimo.siguiente = nueva
            nueva.anterior = ultimo
            nueva.siguiente = self.actual
            self.actual.anterior = nueva

    def eliminar_cancion_actual(self):
        if self.actual is None:
            return
        elif self.actual.siguiente == self.actual:
            self.actual = None
        else:
            prev = self.actual.anterior
            nxt = self.actual.siguiente
            prev.siguiente = nxt
            nxt.anterior = prev
            self.actual = nxt

    def avanzar(self):
        if self.actual:
            self.actual = self.actual.siguiente

    def retroceder(self):
        if self.actual:
            self.actual = self.actual.anterior

    def mostrar_lista(self):
        canciones = []
        if not self.actual:
            return canciones
        nodo = self.actual
        while True:
            canciones.append(str(nodo))
            nodo = nodo.siguiente
            if nodo == self.actual:
                break
        return canciones

    def obtener_cancion_actual(self):
        return self.actual  