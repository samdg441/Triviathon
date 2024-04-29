import pygame
from pygame.locals import *
import sys

# Asegúrate de importar la clase Juego y cualquier otra clase necesaria desde tu archivo principal
# Por ejemplo:
# from juego import Juego, Jugador, Pregunta, Ronda, Ayuda

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Triviathon')

# Configuración de fuentes
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def handle_input(event):
    if event.type == MOUSEBUTTONDOWN:
        # Aquí puedes manejar los clics del mouse para seleccionar respuestas
        pass

def game_loop(juego):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            handle_input(event)

        # Limpiar la pantalla
        screen.fill((0, 0, 0))

        # Aquí puedes agregar lógica para mostrar preguntas y opciones de respuesta
        # Por ejemplo, si tienes una pregunta actual en tu juego:
        # pregunta_actual = juego.pregunta_actual
        # draw_text(pregunta_actual.pregunta, font, (255, 255, 255), SCREEN_WIDTH // 2, 100)

        # Actualizar la pantalla
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    # Crear una instancia de Juego
    # Por ejemplo:
    # juego = Juego([Jugador("Jugador 1")])
    # game_loop(juego)
    pass
