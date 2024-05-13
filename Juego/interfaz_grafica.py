import pygame
import sys
import random
from modulos import obtener_categorias_y_preguntas

# Definir las categorías en el orden correcto
categorias = ['Historia', 'Arte', 'Cultura Pop', 'Ciencia y Tecnología', 'Geografía', 'Deportes', 'Entretenimiento',
              'Ciencia Ficción']

# Asumiendo que obtener_categorias_y_preguntas devuelve las categorías en el orden correcto
categorias_y_preguntas = obtener_categorias_y_preguntas()

# Inicializar Pygame
pygame.init()

# Definir las pantallas disponibles
pantallas = {
    'inicio': 'Pantalla de inicio',
    'seleccion_categorias': 'Pantalla de selección de categorías',
    'reglas': 'Pantalla de reglas',
    'juego': 'Pantalla de inicio del juego',
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
start_button_image = pygame.image.load(
    "C:\\Users\\samue\\Triviathon\\pythonProject\\Juego\\Imagenes\\boton.start-removebg-preview.png")
titulo_image_path = "C:\\Users\\samue\\Triviathon\\pythonProject\\Juego\\Imagenes\\titulo2-removebg-preview.png"
titulo_image = pygame.image.load(titulo_image_path)
reglas_image_path = "C:\\Users\\samue\\Triviathon\\pythonProject\\Juego\\Imagenes\\fondo2.PNG"  # Última imagen proporcionada
reglas_image = pygame.image.load(reglas_image_path)  # Aquí está la corrección

# Cargar la imagen del botón "Siguiente"
next_button_image = pygame.image.load(
    "C:\\Users\\samue\\Triviathon\\pythonProject\\Juego\\Imagenes\\boton.next-removebg-preview.png")
next_button_rect = next_button_image.get_rect(topleft=(210, 500))  # Ajusta x_pos y y_pos según la posición deseada

# Cargar las imágenes de los botones de categoría dinámicamente
categoria_button_images = [pygame.image.load(
    f"C:\\Users\\samue\\Triviathon\\pythonProject\\Juego\\Imagenes\\categoria-removebg-preview-{i}.png") for i in
                           range(1, 9)]

# Crear los rectángulos para los botones de categoría
categoria_button_rects = []
for i, categoria_image in enumerate(categoria_button_images):
    rect = categoria_image.get_rect(topleft=(50, 50 + i * 70))  # Ajusta x_pos y y_pos según la posición deseada
    categoria_button_rects.append(rect)


# Función para manejar el evento de cierre de la ventana
def close_window():
    pygame.quit()
    sys.exit()


# Función para manejar el evento de clic en el botón de inicio
def on_start_button_click():
    global estado_actual
    cambiar_pantalla('seleccion_categorias')


# Función para manejar el evento de clic en el botón "Next"
def on_next_button_click():
    global estado_actual
    cambiar_pantalla('reglas')


# Añade esta función para mostrar las reglas


def seleccionar_categoria():
    global categorias_seleccionadas

    # Limpiar la lista de categorías seleccionadas
    categorias_seleccionadas = []

    # Mostrar las categorías disponibles
    y_pos = 150
    x_pos = 50
    row_count = 0
    column_count = 0
    for i, categoria_image in enumerate(categoria_button_images):
        categoria_rect = categoria_image.get_rect(topleft=(x_pos, y_pos))
        categoria_button_rects[i] = categoria_rect  # Actualizar la lista de rectángulos de botones de categoría
        screen.blit(categoria_image, categoria_rect)
        column_count += 1
        if column_count == 3:  # Si se han dibujado 3 categorías en la fila actual
            column_count = 0  # Reiniciar el contador de columnas
            row_count += 1  # Pasar a la siguiente fila
            x_pos = 50  # Reiniciar la posición en x para la nueva fila
            y_pos += 120  # Ajustar la posición en y para la nueva fila
        else:
            x_pos += 220  # Ajustar la posición en x para la siguiente columna

    # Dibujar el botón "Next" debajo de las categorías
    screen.blit(next_button_image, next_button_rect)
    # Dibujar el título del juego
    titulo_rect = titulo_image.get_rect()
    titulo_rect.topleft = (50, 50)  # Ajusta esto según la posición deseada
    screen.blit(titulo_image, titulo_rect)

    # Actualizar la pantalla
    pygame.display.flip()

    # Variable para indicar si se ha seleccionado una categoría
    categoria_seleccionada = False

    # Esperar a que el usuario seleccione una categoría o haga clic en "Siguiente"
    while not categoria_seleccionada:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_window()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, categoria_rect in enumerate(categoria_button_rects):
                    if categoria_rect.collidepoint(mouse_pos):
                        # Agregar la categoría seleccionada a la lista
                        categoria = categorias[i]
                        if categoria not in categorias_seleccionadas:
                            categorias_seleccionadas.append(categoria)
                            # Generar el mensaje de selección
                            mensaje = f"{len(categorias_seleccionadas)}ª Categoría seleccionada: {categoria}"
                            # Mostrar el mensaje de selección
                            mostrar_mensaje_seleccion(mensaje)
                        else:
                            mostrar_mensaje_seleccion("¡Esta categoría ya ha sido seleccionada!")

                if next_button_rect.collidepoint(mouse_pos):
                    # Contar el número de categorías seleccionadas
                    num_categorias_seleccionadas = len(categorias_seleccionadas)

                    # Verificar si el número de categorías seleccionadas está entre una y tres
                    if 1 <= num_categorias_seleccionadas <= 3:
                        mostrar_mensaje_seleccion("Iniciando juego...")
                        categoria_seleccionada = True  # Cambiar la variable a True para salir del ciclo
                    else:
                        mostrar_mensaje_seleccion("Debes seleccionar entre una y tres categorías para iniciar el juego.")

    # Cambiar a la siguiente pantalla
    cambiar_pantalla('reglas')



def mostrar_mensaje_seleccion(mensaje):
    # Limpiar la pantalla
    screen.blit(background_image, (0, 0))
    # Dibujar el título del juego
    titulo_rect = titulo_image.get_rect()
    titulo_rect.topleft = (50, 50)  # Ajusta esto según la posición deseada
    screen.blit(titulo_image, titulo_rect)
    # Dibujar los botones de categoría
    for i, categoria_image in enumerate(categoria_button_images):
        screen.blit(categoria_image, categoria_button_rects[i])
    # Dibujar el botón "Next"
    screen.blit(next_button_image, next_button_rect)
    # Dibujar el mensaje de selección
    font = pygame.font.SysFont(None, 30)  # Fuente y tamaño del texto
    mensaje_renderizado = font.render(mensaje, True, (134, 48, 48))  # Color del texto (vino claro)
    mensaje_rect = mensaje_renderizado.get_rect()
    mensaje_rect.midtop = (
    screen_width // 2, next_button_rect.bottom + 20)  # Posición del texto debajo del botón "Next"
    screen.blit(mensaje_renderizado, mensaje_rect)
    # Actualizar la pantalla
    pygame.display.flip()
    # Esperar un breve momento antes de borrar el mensaje
    pygame.time.delay(1500)

def mostrar_reglas():
    # Cargar la nueva imagen de fondo usando reglas_image_path
    nueva_imagen = pygame.image.load(reglas_image_path)
    # Dibujar la nueva imagen de fondo
    screen.blit(nueva_imagen, (0, 0))
    # Dibujar el botón "Next" en la misma posición que en la pantalla anterior
    screen.blit(next_button_image, next_button_rect)
    # Actualizar la pantalla
    pygame.display.flip()



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
                seleccionar_categoria()
            elif estado_actual == 'reglas':
                mostrar_reglas()

    # Dibujar el fondo de la pantalla
    screen.blit(background_image, (0, 0))

    # Dibujar el botón de inicio solo cuando el estado es 'inicio'
    if estado_actual == 'inicio':
        start_button_rect = start_button_image.get_rect(topleft=(210, 500))
        screen.blit(start_button_image, start_button_rect)
        # Dibujar el título del juego
        titulo_rect = titulo_image.get_rect()
        titulo_rect.topleft = (50, 50)  # Ajusta esto según la posición deseada
        screen.blit(titulo_image, titulo_rect)

    # Dibujar los botones de categoría solo cuando el estado es 'seleccion_categorias'
    if estado_actual == 'seleccion_categorias':
        y_pos = 150
        x_pos = 50
        row_count = 0
        column_count = 0
        for i, categoria_image in enumerate(categoria_button_images):
            categoria_rect = categoria_image.get_rect(topleft=(x_pos, y_pos))
            screen.blit(categoria_image, categoria_rect)
            column_count += 1
            if column_count == 3:  # Si se han dibujado 3 categorías en la fila actual
                column_count = 0  # Reiniciar el contador de columnas
                row_count += 1  # Pasar a la siguiente fila
                x_pos = 50  # Reiniciar la posición en x para la nueva fila
                y_pos += 120  # Ajustar la posición en y para la nueva fila
            else:
                x_pos += 220  # Ajustar la posición en x para la siguiente columna

        # Dibujar el botón "Next" debajo de las categorías
        screen.blit(next_button_image, next_button_rect)

    # Dibujar la imagen de reglas solo cuando el estado es 'reglas'
    if estado_actual == 'reglas':
        mostrar_reglas()

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(60)
