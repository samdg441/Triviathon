import pygame
import sys
import random
import requests
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
    'final': 'Pantalla de inicio del juego',
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
pygame.display.set_caption("Triviathon")
screen_width = 660
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))

# Cargar las imágenes
background_image_path = "Imagenes\\Captura.PNG"
background_image = pygame.image.load(background_image_path)
start_button_image = pygame.image.load(
    "Imagenes\\boton.start-removebg-preview.png")
titulo_image_path = "Imagenes\\titulo2-removebg-preview.png"
titulo_image = pygame.image.load(titulo_image_path)
reglas_image_path = "Imagenes\\fondo3.PNG"  # Última imagen proporcionada
reglas_image = pygame.image.load(reglas_image_path)  # Aquí está la corrección

# Cargar la imagen del botón "Siguiente"
next_button_image = pygame.image.load(
    "Imagenes\\boton.next-removebg-preview.png")
next_button_rect = next_button_image.get_rect(topleft=(210, 500))  # Ajusta x_pos y y_pos según la posición deseada

# Cargar las imágenes de los botones de categoría dinámicamente
categoria_button_images = [pygame.image.load(
    f"Imagenes\\categoria-removebg-preview-{i}.png") for i in
    range(1, 9)]

# Crear los rectángulos para los botones de categoría
categoria_button_rects = []
for i, categoria_image in enumerate(categoria_button_images):
    rect = categoria_image.get_rect(topleft=(50, 50 + i * 70))  # Ajusta x_pos y y_pos según la posición deseada
    categoria_button_rects.append(rect)


# Definir el rectángulo para la imagen del título de las reglas
reglas_titulo_imagen_path = "Imagenes\\titulo_reglas-removebg-preview.png"
reglas_titulo_imagen = pygame.image.load(reglas_titulo_imagen_path)
reglas_titulo_imagen_rect = reglas_titulo_imagen.get_rect(
    topleft=(115, 10))  # Ajusta x_pos y y_pos según la posición deseada

pregunta_image_path = "Imagenes\\casilla.texto.preguntas-removebg-preview.png"
pregunta_image = pygame.image.load(pregunta_image_path)
opcion_image_path = "Imagenes\\boton.respuestas-removebg-preview.png"


# Cargar las imágenes de los botones de ayuda
button_5050_image = pygame.image.load("Imagenes\\boton.5050.png")
button_change_question_image = pygame.image.load("Imagenes\\boton.cambio.pregunta-removebg-preview.png")
button_ai_image = pygame.image.load("Imagenes\\boton.Ia-removebg-preview.png")

# Escalar las imágenes de los botones de ayuda al tamaño deseado
button_5050_image = pygame.transform.scale(button_5050_image, (120, 82))
button_change_question_image = pygame.transform.scale(button_change_question_image, (120, 85))
button_ai_image = pygame.transform.scale(button_ai_image, (120, 90))

# Definir los rectángulos para los botones de ayuda con las nuevas dimensiones
button_5050_rect = button_5050_image.get_rect(bottomleft=(10, screen_height - 60))
button_change_question_rect = button_change_question_image.get_rect(bottomleft=(120, screen_height - 60))
button_ai_rect = button_ai_image.get_rect(bottomleft=(230, screen_height - 60))

# Función para manejar el evento de cierre de la ventana
def close_window():
    pygame.quit()
    sys.exit()


# Función para manejar el evento de clic en el botón de inicio
def on_start_button_click():
    global estado_actual
    cambiar_pantalla('reglas')

# Función para manejar el evento de clic en el botón "Next"
def on_next_button_click():
    global estado_actual
    if estado_actual == 'reglas':  # Verificar si estamos en la pantalla de reglas
        cambiar_pantalla('seleccion_categorias')  # Cambiar al estado de seleccionar categorías
    elif estado_actual == 'seleccion_categorias':  # Si estamos en la pantalla de selección de categorías
        mostrar_pantalla_juego()  # Mostrar la pantalla del juego

def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def mostrar_reglas():
    # Cargar la nueva imagen de fondo usando reglas_image_path
    nueva_imagen = pygame.image.load(reglas_image_path)
    # Dibujar la nueva imagen de fondo
    screen.blit(nueva_imagen, (0, 0))
    # Dibujar el botón "Next" un poco más abajo
    next_button_rect = next_button_image.get_rect(topleft=(210, 550))  # Ajusta x_pos y y_pos según la posición deseada
    screen.blit(next_button_image, next_button_rect)

    # Cargar la imagen de texto de las reglas
    reglas_texto_image_path = "Imagenes\\texto_reglas.PNG"
    reglas_texto_image = pygame.image.load(reglas_texto_image_path)
    # Dibujar la imagen de texto de las reglas
    reglas_texto_rect = reglas_texto_image.get_rect()
    reglas_texto_rect.center = (screen_width // 2, 330)  # Ajusta la posición horizontal y vertical según sea necesario
    screen.blit(reglas_texto_image, reglas_texto_rect)

    # Dibujar el título de las reglas
    screen.blit(reglas_titulo_imagen, reglas_titulo_imagen_rect)

    pygame.display.flip()

def seleccionar_categoria():
    global categorias_seleccionadas, estado_actual, banco_preguntas

    # Limpiar la lista de categorías seleccionadas
    categorias_seleccionadas.clear()  # Utiliza clear() para limpiar la lista sin reasignarla

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
                    # Crear un banco de preguntas filtrando las preguntas según las categorías seleccionadas
                    banco_preguntas = {}
                    for categoria in categorias_seleccionadas:
                        if categoria in categorias_y_preguntas:  # Asegúrate de que la categoría esté en el diccionario de preguntas
                            banco_preguntas[categoria] = categorias_y_preguntas[categoria]

                    # Verificar si se han seleccionado entre una y tres categorías
                    if 1 <= len(banco_preguntas) <= 3:
                        # Cambiar el estado actual a 'juego'
                        estado_actual = 'juego'
                        categoria_seleccionada = True  # Cambiar la variable a True para salir del ciclo
                    else:
                        mostrar_mensaje_seleccion(
                            "Debes seleccionar entre una y tres categorías para iniciar el juego.")



# Variable para almacenar la pregunta actual
pregunta_actual = None

def mostrar_pantalla_juego():
    global pregunta_actual

    # Cargar la imagen de fondo de la pregunta
    pregunta_image = pygame.image.load('Imagenes\\casilla.texto.preguntas-removebg-preview.png')

    # Dibujar el fondo de la pantalla
    screen.blit(reglas_image, (0, 0))

    # Dibujar los botones de ayuda en la esquina inferior izquierda
    screen.blit(button_5050_image, button_5050_rect)
    screen.blit(button_change_question_image, button_change_question_rect)
    screen.blit(button_ai_image, button_ai_rect)

    # Si no hay una pregunta actual, cargar una nueva pregunta
    if not pregunta_actual:
        # Seleccionar una pregunta aleatoria de las categorías seleccionadas
        categoria_seleccionada = random.choice(list(banco_preguntas.keys()))
        pregunta_actual = random.choice(banco_preguntas[categoria_seleccionada])

    # Dibujar la pregunta
    screen.blit(pregunta_image, (0, 0))

    # Texto de la pregunta
    pregunta_font = pygame.font.Font(None, 24)  # Reducir el tamaño de la fuente
    pregunta_color = (0, 0, 0)  # Color negro
    pregunta_text_surface = pregunta_font.render(pregunta_actual.pregunta, True, pregunta_color)
    pregunta_text_rect = pregunta_text_surface.get_rect(center=(pregunta_image.get_width() // 2, pregunta_image.get_height() // 2))
    screen.blit(pregunta_text_surface, pregunta_text_rect)

    # Definir posiciones para los botones de opción
    opcion_positions = [
        (screen_width // 4, screen_height // 3),
        (3 * screen_width // 4, screen_height // 3),
        (screen_width // 4, 2 * screen_height // 3),
        (3 * screen_width // 4, 2 * screen_height // 3)
    ]

    # Dibujar las opciones en la matriz 2x2
    opciones_font = pygame.font.Font(None, 20)  # Reducir el tamaño de la fuente
    opciones_color = (0, 0, 0)
    opcion_rects = []  # Lista para almacenar los rectángulos de las opciones

    for i in range(4):
        opcion_texto = pregunta_actual.respuestas[i]
        opcion_image = pygame.image.load(opcion_image_path.format(i))
        opcion_rect = opcion_image.get_rect(center=opcion_positions[i])
        screen.blit(opcion_image, opcion_rect)
        draw_text(screen, opcion_texto, opciones_font, opciones_color, opcion_rect.centerx, opcion_rect.centery)
        opcion_rects.append(opcion_rect)  # Agregar el rectángulo a la lista

    pygame.display.flip()

    # Devolver opcion_rects para que esté disponible fuera de la función
    return opcion_rects


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


def pedir_nombre():
    nombre = input("Por favor, introduce tu nombre: ")
    return nombre


# Inicializar el contador de respuestas correctas
respuestas_correctas = 0


def verificar_respuesta(respuesta_elegida):
    global pregunta_actual, respuestas_correctas

    # Comparar la respuesta elegida con la respuesta correcta de la pregunta actual
    if respuesta_elegida == pregunta_actual.respuesta_correcta:
        respuestas_correctas += 1
        # Aquí podrías mostrar algún mensaje de "¡Respuesta correcta!" o algo similar

    # Cargar y mostrar la siguiente pregunta
    cargar_siguiente_pregunta()


# Función para cargar la siguiente pregunta


def on_change_question_button_click():
    global pregunta_actual,ayuda_disponibles
    pregunta_actual = None
    # Restar una ayuda disponible
    ayuda_disponibles -= 1
    mostrar_pantalla_juego()
    pygame.display.flip()
def on_50_50_button_click():
    global pregunta_actual, ayuda_disponibles
    # Seleccionar dos índices aleatorios para eliminar dos respuestas incorrectas
    indices_incorrectos = []
    while len(indices_incorrectos) < 2:
        indice = random.randint(0, 3)
        respuesta = pregunta_actual.respuestas[indice]
        if respuesta != pregunta_actual.respuesta_correcta and indice not in indices_incorrectos:
            indices_incorrectos.append(indice)

    # Establecer el texto de las respuestas incorrectas seleccionadas en una cadena vacía
    for indice in indices_incorrectos:
        pregunta_actual.respuestas[indice] = ""
        ayuda_disponibles -= 1  # Reducir una ayuda disponible

    # Actualizar la pantalla para reflejar los cambios
    mostrar_pantalla_juego()
    pygame.display.flip()
def ayuda_api():
    global pregunta_actual, ayuda_disponibles
    api_key = 'b2696886ce070a16f352f6bf3a5a7a0a45df24c0f9375f3930099dc54870f654'
    query = pregunta_actual.pregunta  # Accede al texto de la pregunta

    num_results_per_page = 1
    total_pages = 1
    num = num_results_per_page * total_pages

    response = requests.get(
        f"https://serpapi.com/search?engine=duckduckgo&q={query}&api_key={api_key}&num={num}"
    )

    if response.status_code == 200:
        data = response.json()
        for result in data['organic_results']:
            lines = result['snippet'].split('\n')
            if len(lines) > 3:
                texto_ayuda = '\n'.join(lines[:3])
            else:
                texto_ayuda = result['snippet']
            ayuda_disponibles -= 1  # Reducir una ayuda disponible
            # Mostrar el texto de ayuda
            print("Ayuda de la IA:")
            print(texto_ayuda)
    else:
        print(f"Error: {response.status_code}")

    pygame.display.flip()

def mostrar_pantalla_final(nombre_jugador):
    # Cambiar el fondo de la pantalla final
    screen.fill((0, 0, 0))  # Rellenar la pantalla con negro
    # Aquí puedes cargar y mostrar la imagen de fondo que desees
    fondo_final_image = pygame.image.load("Imagenes\\fondo4.PNG")
    screen.blit(fondo_final_image, (0, 0))

    # Mostrar el nombre del jugador y el número de respuestas correctas
    font = pygame.font.SysFont(None, 30)
    texto_nombre = font.render(f"Jugador: {nombre_jugador}", True, (255, 255, 255))
    texto_respuestas = font.render(f"Respuestas correctas: {contador_respuestas_correctas}", True, (255, 255, 255))
    screen.blit(texto_nombre, (250, 200))
    screen.blit(texto_respuestas, (250, 250))

    # Mostrar las categorías seleccionadas
    y_pos = 300
    for categoria in categorias_seleccionadas:
        texto_categoria = font.render(categoria, True, (255, 255, 255))
        screen.blit(texto_categoria, (240, y_pos))
        y_pos += 30

def on_game_end():
    mostrar_pantalla_final(nombre_jugador)
    global estado_actual
    estado_actual = 'final'  # Cambiar al estado final
    running= False

running = True
ayuda_disponibles = len(categorias_seleccionadas)  # Inicializar las ayudas disponibles al número de categorías seleccionadas
total_preguntas = 0  # Inicializar el total de preguntas

def cargar_siguiente_pregunta():
    global pregunta_actual

    # Obtener una categoría aleatoria de las disponibles en el banco de preguntas
    categoria_aleatoria = random.choice(list(banco_preguntas.keys()))

    # Obtener una pregunta aleatoria de la categoría seleccionada
    pregunta_aleatoria = random.choice(banco_preguntas[categoria_aleatoria])

    # Asignar la pregunta aleatoria como la pregunta actual
    pregunta_actual = pregunta_aleatoria

    # Después de cargar la siguiente pregunta, mostrarla en la pantalla
    mostrar_pantalla_juego()

contador_respuestas_correctas = 0

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
                if estado_actual == 'juego':  # Verificar si se ha cambiado al estado de juego
                    mostrar_pantalla_juego()  # Mostrar la pantalla de juego
            elif estado_actual == 'reglas':
                mostrar_reglas()
                nombre_jugador = pedir_nombre()
                print(f"Bienvenido, {nombre_jugador} Ahora que conoces las reglas, ¡prepárate para jugar!")
                on_next_button_click()  # Llamar a la función para cambiar a la pantalla de selección de categorías
            elif estado_actual == 'juego':
                if button_change_question_rect.collidepoint(mouse_pos):
                    on_change_question_button_click()  # Llamar a la función para cambiar la pregunta
                elif button_5050_rect.collidepoint(mouse_pos):
                    on_50_50_button_click()  # Llamar a la función para eliminar dos respuestas incorrectas
                    ayuda_disponibles -= 1  # Reducir una ayuda disponible
                elif button_ai_rect.collidepoint(mouse_pos):  # Verificar si se hizo clic en el botón de la IA
                    texto_ayuda = ayuda_api()
                    print("Ayuda de la IA:")
                    print(texto_ayuda)
                    ayuda_disponibles -= 1  # Reducir una ayuda disponible

                # Verificar si se produce un evento de clic del mouse en la pantalla de juego
                for i, opcion_rect in enumerate(opcion_rects):
                    if opcion_rect.collidepoint(mouse_pos):
                        if pregunta_actual.respuestas[i] == pregunta_actual.respuesta_correcta:
                            contador_respuestas_correctas += 1
                            if total_preguntas == ayuda_disponibles * 5:
                                estado_actual = 'final'
                                on_game_end()
                            else:
                                # Preparar la siguiente pregunta
                                total_preguntas += 1  # Incrementar el total de preguntas
                                cargar_siguiente_pregunta()  # Llamar a la función para cargar la siguiente pregunta
                        else:
                            estado_actual = 'final'
                            on_game_end()

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

    # Dibujar la pantalla de juego solo cuando el estado es 'juego'
    if estado_actual == 'juego':
        opcion_rects = mostrar_pantalla_juego()  # Llamar a la función y obtener los rectángulos de las opciones
        # Inicializar el contador de ayudas al número de categorías seleccionadas
        ayuda_disponibles = len(categorias_seleccionadas)

    # Verificar si el juego ha terminado y mostrar la pantalla final
    if estado_actual == 'final':
        mostrar_pantalla_final(nombre_jugador)
        # Detener el bucle principal


    # Actualiza la pantalla
    pygame.display.flip()

    # Controla la velocidad de actualización
    pygame.time.Clock().tick(60)