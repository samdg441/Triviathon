import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir las pantallas disponibles
pantallas = {
    'inicio': 'Pantalla de inicio',
    'seleccion_categorias': 'Pantalla de selección de categorías',
    # Puedes agregar más pantallas aquí según sea necesario
}

# Definir categorias_seleccionadas como una lista vacía
categorias_seleccionadas = []

# Mantener el estado actual de la pantalla
estado_actual = 'inicio'

def cambiar_pantalla(nueva_pantalla):
    global estado_actual
    estado_actual = nueva_pantalla
    print(f"Estado actual cambiado a: {estado_actual}")

# Configurar la pantalla
screen_width = 660
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))

# Cargar las imágenes
background_image_path = "C:\\Users\\samue\\Triviathon\\pythonProject\\Juego\\Imagenes\\Captura.PNG"
background_image = pygame.image.load(background_image_path)
start_button_image = pygame.image.load("C:\\Users\\samue\\Triviathon\\pythonProject\\Juego\\Imagenes\\boton.start-removebg-preview.png")
titulo_image_path = "C:\\Users\\samue\\Triviathon\\pythonProject\\Juego\\Imagenes\\titulo2-removebg-preview.png"
titulo_image = pygame.image.load(titulo_image_path)

# Cargar las imágenes de los botones de categoría
categoria_button_images = [pygame.image.load(f"C:\\Users\\samue\\Triviathon\\pythonProject\\Juego\\Imagenes\\categoria-removebg-preview-{i}.png") for i in range(1, 9)]
next_button_image = pygame.image.load("C:\\Users\\samue\\Triviathon\\pythonProject\\Juego\\Imagenes\\boton.next-removebg-preview.png")

# Crear los rectángulos para los botones de categoría
categoria_button_rects = []
for i in range(8):  # Asumiendo que tienes 8 categorías
    rect = categoria_button_images[i].get_rect(topleft=(50, 50 + i * 70))  # Ajusta x_pos y y_pos según la posición deseada
    categoria_button_rects.append(rect)

# Crear el rectángulo para el botón "Siguiente"
next_button_rect = next_button_image.get_rect(topleft=(210, 500))  # Ajusta x_pos y y_pos según la posición deseada

# Función para manejar el evento de cierre de la ventana
def close_window():
    pygame.quit()
    sys.exit()

# Función para manejar el evento de clic en el botón de inicio
def on_start_button_click():
    global estado_actual
    cambiar_pantalla('seleccion_categorias')

# Función para manejar la selección de categorías
# Función para manejar la selección de categorías
def seleccionar_categoria():
    global categorias_seleccionadas
    # Limpiar la lista de categorías seleccionadas
    categorias_seleccionadas = []
    # Mostrar las categorías disponibles
    y_pos = 150
    for i, categoria in enumerate(categoria_button_images):
        categoria_rect = categoria.get_rect(topleft=(50 + (i % 3) * 220, y_pos))
        screen.blit(categoria, categoria_rect)
        if (i + 1) % 3 == 0:  # Ajustar la posición y para la última categoría de cada fila
            y_pos += 120

    # Dibujar el botón "Next" debajo de las categorías
    next_button_rect = next_button_image.get_rect(topleft=(210, y_pos + 100))  # Ajusta la posición y según sea necesario
    screen.blit(next_button_image, next_button_rect)

    # Actualizar la pantalla
    pygame.display.flip()

    # Esperar a que el usuario seleccione una categoría o haga clic en "Siguiente"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_window()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, categoria_rect in enumerate(categoria_button_rects):
                    if categoria_rect.collidepoint(mouse_pos):
                        # Agregar la categoría seleccionada a la lista
                        categorias_seleccionadas.append(categoria_button_images[i])
                        print(f"Categoría seleccionada: {categoria_button_images[i]}")
                        # Actualizar la pantalla después de la selección
                        seleccionar_categoria()
                        return
                if next_button_rect.collidepoint(mouse_pos):
                    # Aquí manejas el clic en el botón "Siguiente"
                    # Por ejemplo, puedes verificar si se seleccionaron 3 categorías y luego iniciar el juego
                    iniciar_juego()
                    return

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if estado_actual == 'inicio':
                if start_button_image.get_rect(topleft=(210, 500)).collidepoint(mouse_pos):
                    on_start_button_click()
            elif estado_actual == 'seleccion_categorias':
                for i, rect in enumerate(categoria_button_rects):
                    if rect.collidepoint(mouse_pos):
                        # Aquí manejas el clic en un botón de categoría
                        categoria_seleccionada = categoria_button_images[i]  # Accede a la imagen correspondiente
                        print(f"Categoría seleccionada: {categoria_button_images[i]}")
                        # Aquí iría la lógica para permitir al usuario seleccionar otra categoría o avanzar
                        break
                if next_button_rect.collidepoint(mouse_pos):
                    # Aquí manejas el clic en el botón "Siguiente"
                    # Por ejemplo, puedes verificar si se seleccionaron 3 categorías y luego iniciar el juego
                    iniciar_juego()

    # Dibujar el fondo de la pantalla de inicio
    screen.blit(background_image, (0, 0))

    # Dibujar el título del juego
    titulo_rect = titulo_image.get_rect()
    titulo_rect.topleft = (50, 50)  # Ajusta esto según la posición deseada
    screen.blit(titulo_image, titulo_rect)

    # Dibujar el botón de inicio solo cuando el estado es 'inicio'
    if estado_actual == 'inicio':
        start_button_rect = start_button_image.get_rect(topleft=(210, 500))
        screen.blit(start_button_image, start_button_rect)

    # Dibujar los botones de categoría solo cuando el estado es 'seleccion_categorias'
    if estado_actual == 'seleccion_categorias':
        seleccionar_categoria()

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(60)