import pygame

class Reproductor:
    def __init__(self):
        pygame.mixer.init()  
        pygame.mixer.music.set_endevent(pygame.USEREVENT)  

    def reproducir(self, ruta):
        try:
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.play()
        except Exception as e:
            print("❌ Error al reproducir:", e)

    def pausar(self):
        pygame.mixer.music.pause()

    def detener(self):
        pygame.mixer.music.stop()

    def reanudar(self):
        pygame.mixer.music.unpause()

    def evento_fin(self):
        """Método para manejar la canción al terminarla"""
        if pygame.mixer.music.get_busy() == False:
            return True
        return False
