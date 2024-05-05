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

import requests

# Reemplaza 'YOUR_API_KEY' con tu clave de API de SerpApi
api_key = 'b2696886ce070a16f352f6bf3a5a7a0a45df24c0f9375f3930099dc54870f654'

# Definir la consulta de búsqueda
query = "¿Quién pintó la Mona Lisa?"

# Ajustar el número de resultados por página para limitar los resultados a 3 páginas
num_results_per_page = 1  # Asumiendo 10 resultados por página
total_pages = 1  # Total de páginas que deseas obtener
num = num_results_per_page * total_pages  # Calcular el número total de resultados

# Realizar la solicitud GET a la API de SerpApi
response = requests.get(
    f"https://serpapi.com/search?engine=duckduckgo&q={query}&api_key={api_key}&num={num}"
)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a JSON
    data = response.json()

    # Filtrar e imprimir solo las descripciones de los resultados de búsqueda, limitando a 3 líneas
    for result in data['organic_results']:
        lines = result['snippet'].split('\n')
        if len(lines) > 3:
            # Limita la descripción a las primeras 3 líneas
            print('\n'.join(lines[:3]))
        else:
            print(result['snippet'])  # Muestra todo el texto si hay menos de 3 líneas
else:
    print(f"Error: {response.status_code}")