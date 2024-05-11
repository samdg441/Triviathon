import random
import requests
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Pregunta:
    def __init__(self, pregunta, respuestas, respuesta_correcta, categoria):
        self.pregunta = pregunta
        self.respuestas = respuestas
        self.respuesta_correcta = respuesta_correcta
        self.categoria = categoria

class Ronda:
    def __init__(self, preguntas, categorias_seleccionadas):
        self.preguntas = preguntas
        self.categorias_seleccionadas = categorias_seleccionadas
        self.puntos = 0

    def incrementar_puntos(self, puntos):
        self.puntos += puntos

class Ayuda:
    def __init__(self, juego, total_categorias):
        self.juego = juego
        self.total_categorias = total_categorias
        self.ayudas_usadas = 0

    def ayuda_50_50(self, pregunta):
        if self.ayudas_usadas >= self.total_categorias:
            print("No puedes usar más ayudas.")
            return pregunta
        self.ayudas_usadas += 1
        respuestas_incorrectas = [respuesta for respuesta in pregunta.respuestas if respuesta != pregunta.respuesta_correcta] #contiene todas las respuestas incorrectas de la pregunta actual
        if len(respuestas_incorrectas) < 2:
            print("No hay suficientes respuestas incorrectas para aplicar el 50/50.")
            return pregunta
        respuestas_eliminadas = random.sample(respuestas_incorrectas, 2)
        for respuesta in respuestas_eliminadas:
            pregunta.respuestas.remove(respuesta)
        if pregunta.respuesta_correcta not in pregunta.respuestas:
            respuestas_restantes = [respuesta for respuesta in pregunta.respuestas if respuesta != pregunta.respuesta_correcta]
            respuesta_mantener = random.choice(respuestas_restantes)
            pregunta.respuestas.remove(respuesta_mantener)
            pregunta.respuestas.append(pregunta.respuesta_correcta)
        return pregunta

    def cambio_pregunta(self):
        if self.ayudas_usadas >= self.total_categorias:
            print("No puedes usar más ayudas.")
            return None
        self.ayudas_usadas += 1
        return self.juego.obtener_pregunta_aleatoria()
    def ayuda_api(self, pregunta):
        if self.ayudas_usadas >= self.total_categorias:
            print("No puedes usar más ayudas.")
            return
        self.ayudas_usadas += 1
        api_key = 'b2696886ce070a16f352f6bf3a5a7a0a45df24c0f9375f3930099dc54870f654'
        query = pregunta.pregunta

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
                    print('\n'.join(lines[:3]))
                else:
                    print(result['snippet'])
        else:
            print(f"Error: {response.status_code}")


categorias = {
    "Historia": [
        Pregunta("¿Quién fue el primer presidente de los Estados Unidos?", ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John F. Kennedy"], "George Washington", "Historia"),
        Pregunta("¿En qué año comenzó la Segunda Guerra Mundial?", ["A. 1914", "B. 1939", "C. 1941", "D. 1945"], "1939", "Historia")
    ],
    "Arte": [
        Pregunta("¿Quién pintó la Mona Lisa?", ["Leonardo da Vinci", "Michelangelo", "Pablo Picasso", "Vincent van Gogh"], "Leonardo da Vinci", "Arte"),
        Pregunta("¿Cuál es el nombre del famoso cuadro de Van Gogh con los girasoles?", ["Estrellas nocturnas", "La noche estrellada", "Los girasoles", "La noche"], "Los girasoles", "Arte")
    ],
"Cultura Pop": [
    Pregunta("¿Cuál es el nombre del actor que interpreta a Iron Man en el Universo Cinematográfico de Marvel?", ["Chris Evans", "Robert Downey Jr.", "Chris Hemsworth", "Mark Ruffalo"], "Robert Downey Jr.", "Cultura Pop"),
    Pregunta("¿Qué banda de pop lanzó el álbum 'Thriller' en 1982?", ["The Beatles", "Queen", "Michael Jackson", "ABBA"], "Michael Jackson", "Cultura Pop"),
    Pregunta("¿Quién es el cantante de 'Bad Guy'?", ["Ariana Grande", "Billie Eilish", "Taylor Swift", "Lady Gaga"], "Billie Eilish", "Cultura Pop"),
    Pregunta("¿Cuál es el nombre de la banda de rock alternativo?", ["The Beatles", "Nirvana", "The Rolling Stones", "The Clash"], "Nirvana", "Cultura Pop"),
    Pregunta("¿Cuál es el nombre del álbum más vendido de todos los tiempos?", ["Dark Side of the Moon", "Back in Black", "Thriller", "Abbey Road"], "Thriller", "Cultura Pop"),
    Pregunta("¿Quién es el director de la película 'Pulp Fiction'?", ["Quentin Tarantino", "Steven Spielberg", "Martin Scorsese", "Christopher Nolan"], "Quentin Tarantino", "Cultura Pop"),
    Pregunta("¿Cuál es el nombre real de la cantante Lady Gaga?", ["Stefani Germanotta", "Katy Perry", "Beyoncé Knowles", "Taylor Swift"], "Stefani Germanotta", "Cultura Pop"),
    Pregunta("¿Qué película ganó el Premio Óscar a la Mejor Película en 2020?", ["Parasite", "1917", "Joker", "Green Book"], "Parasite", "Cultura Pop"),
    Pregunta("¿Cuál es el nombre completo de la cantante Rihanna?", ["Robyn Rihanna Fenty", "Beyoncé Giselle Knowles", "Katheryn Elizabeth Hudson", "Stefani Joanne Angelina Germanotta"], "Robyn Rihanna Fenty", "Cultura Pop"),
    Pregunta("¿Qué grupo musical lanzó el álbum 'Abbey Road'?", ["The Beatles", "The Rolling Stones", "Led Zeppelin", "Pink Floyd"], "The Beatles", "Cultura Pop")
],


"Ciencia y Tecnología": [
    Pregunta("¿Qué científico desarrolló la teoría de la relatividad?", ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"], "Albert Einstein", "Ciencia y Tecnología"),
    Pregunta("¿Qué compañía lanzó el primer iPhone en 2007?", ["Samsung", "Apple", "Sony", "Microsoft"], "Apple", "Ciencia y Tecnología"),
    Pregunta("¿Quién inventó el primer microscopio?", ["Antonie van Leeuwenhoek", "Robert Hooke", "Galileo Galilei", "Isaac Newton"], "Antonie van Leeuwenhoek", "Ciencia y Tecnología"),
    Pregunta("¿Cuál es el nombre del satélite natural de la Tierra?", ["Luna", "Marte", "Júpiter", "Venus"], "Luna", "Ciencia y Tecnología"),
    Pregunta("¿Quién es considerado el padre de la computación?", ["Alan Turing", "Charles Babbage", "Tim Berners-Lee", "Bill Gates"], "Alan Turing", "Ciencia y Tecnología"),
    Pregunta("¿Cuál es el elemento químico más abundante en el universo?", ["Hidrógeno", "Oxígeno", "Helio", "Carbono"], "Hidrógeno", "Ciencia y Tecnología"),
    Pregunta("¿Qué inventor patentó el primer teléfono?", ["Alexander Graham Bell", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi"], "Alexander Graham Bell", "Ciencia y Tecnología"),
    Pregunta("¿En qué año se envió el primer correo electrónico?", ["1969", "1971", "1983", "1990"], "1971", "Ciencia y Tecnología"),
    Pregunta("¿Qué científico formuló la ley de la gravitación universal?", ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"], "Isaac Newton", "Ciencia y Tecnología"),
    Pregunta("¿Cuál es el elemento más abundante en la corteza terrestre?", ["Oxígeno", "Silicio", "Hierro", "Aluminio"], "Oxígeno", "Ciencia y Tecnología")
],

"Geografía": [
    Pregunta("¿Cuál es el río más largo del mundo?", ["Amazonas", "Nilo", "Misisipi", "Yangtsé"], "Amazonas", "Geografía"),
    Pregunta("¿En qué continente se encuentra el monte Kilimanjaro?", ["África", "Asia", "Europa", "América"], "África", "Geografía"),
    Pregunta("¿Cuál es el país más grande del mundo por área?", ["Rusia", "Canadá", "China", "Estados Unidos"], "Rusia", "Geografía"),
    Pregunta("¿En qué continente se encuentra el desierto del Sahara?", ["África", "Asia", "América", "Europa"], "África", "Geografía"),
    Pregunta("¿Cuál es el país más pequeño del mundo por área?", ["Mónaco", "Nauru", "Vaticano", "Maldivas"], "Vaticano", "Geografía"),
    Pregunta("¿En qué continente se encuentra el río Amazonas?", ["América del Sur", "África", "Asia", "Europa"], "América del Sur", "Geografía"),
    Pregunta("¿Cuál es el país más poblado del mundo?", ["China", "India", "Estados Unidos", "Indonesia"], "China", "Geografía"),
    Pregunta("¿En qué continente se encuentra el monte Everest?", ["Asia", "Europa", "América del Norte", "África"], "Asia", "Geografía"),
    Pregunta("¿Cuál es el océano más grande del mundo?", ["Océano Pacífico", "Océano Atlántico", "Océano Índico", "Océano Antártico"], "Océano Pacífico", "Geografía"),
    Pregunta("¿Qué país es conocido como 'La Tierra del Sol Naciente'?", ["China", "Japón", "India", "Australia"], "Japón", "Geografía")
],
"Deportes": [
    Pregunta("¿Qué equipo de fútbol ha ganado más Copas del Mundo de la FIFA?", ["Brasil", "Alemania", "Argentina", "Italia"], "Brasil", "Deportes"),
    Pregunta("¿Cuál es el deporte más popular en Estados Unidos?", ["Fútbol", "Béisbol", "Baloncesto", "Hockey sobre hielo"], "Béisbol", "Deportes"),
    Pregunta("¿En qué deporte se utiliza una puntuación llamada 'strike'?", ["Fútbol", "Béisbol", "Baloncesto", "Hockey sobre hielo"], "Béisbol", "Deportes"),
    Pregunta("¿Qué equipo ganó la Copa Mundial de Fútbol de la FIFA en 2018?", ["Francia", "Brasil", "Alemania", "Argentina"], "Francia", "Deportes"),
    Pregunta("¿Cuál es el deporte más popular en la India?", ["Críquet", "Fútbol", "Hockey sobre hierba", "Baloncesto"], "Críquet", "Deportes"),
    Pregunta("¿En qué deporte se utiliza una red y una pelota blanca?", ["Tenis", "Voleibol", "Balonmano", "Bádminton"], "Tenis", "Deportes"),
    Pregunta("¿En qué deporte se otorga el premio 'Balón de Oro'?", ["Fútbol", "Baloncesto", "Tenis", "Atletismo"], "Fútbol", "Deportes"),
    Pregunta("¿Cuál es el deporte principal en el Tour de Francia?", ["Ciclismo", "Atletismo", "Natación", "Voleibol"], "Ciclismo", "Deportes"),
    Pregunta("¿Cuál es el deporte más popular en Italia?", ["Fútbol", "Rugby", "Baloncesto", "Voleibol"], "Fútbol", "Deportes"),
    Pregunta("¿En qué deporte se utiliza una raqueta y una pelota?", ["Tenis", "Golf", "Polo", "Bádminton"], "Tenis", "Deportes")
],
    "Entretenimiento": [
        Pregunta("¿Quién interpretó a Harry Potter en las películas de la saga?", ["Daniel Radcliffe", "Rupert Grint", "Emma Watson", "Tom Felton"], "Daniel Radcliffe", "Entretenimiento"),
        Pregunta("¿Cuál es el nombre del actor que protagonizó 'Forrest Gump'?", ["Tom Hanks", "Leonardo DiCaprio", "Brad Pitt", "Johnny Depp"], "Tom Hanks", "Entretenimiento"),
        Pregunta("¿Quién interpretó a Batman en la trilogía dirigida por Christopher Nolan?", ["Christian Bale", "Ben Affleck", "George Clooney", "Michael Keaton"], "Christian Bale", "Entretenimiento"),
        Pregunta("¿Qué actor interpretó a Jack en la película 'Titanic'?", ["Leonardo DiCaprio", "Brad Pitt", "Johnny Depp", "Matt Damon"], "Leonardo DiCaprio", "Entretenimiento"),
        Pregunta("¿Quién dirigió la película 'El Padrino'?", ["Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola", "Alfred Hitchcock"], "Francis Ford Coppola", "Entretenimiento"),
        Pregunta("¿En qué película animada aparece el personaje Buzz Lightyear?", ["Toy Story", "Shrek", "Frozen", "Monsters, Inc."], "Toy Story", "Entretenimiento"),
       Pregunta("¿Quién es el actor que interpreta a Tony Stark / Iron Man en el Universo Cinematográfico de Marvel?", ["Robert Downey Jr.", "Chris Evans", "Chris Hemsworth", "Mark Ruffalo"], "Robert Downey Jr.", "Entretenimiento"),
        Pregunta("¿Cuál es el nombre del director de la película 'Inception'?", ["Christopher Nolan", "Steven Spielberg", "Quentin Tarantino", "Martin Scorsese"], "Christopher Nolan", "Entretenimiento"),
         Pregunta("¿Quién es el director de la trilogía 'El Señor de los Anillos'?", ["Peter Jackson", "George Lucas", "James Cameron", "Steven Spielberg"], "Peter Jackson", "Entretenimiento"),
        Pregunta("¿Cuál es el nombre del actor que interpreta a Sherlock Holmes en la serie de la BBC 'Sherlock'?", ["Benedict Cumberbatch", "Martin Freeman", "Tom Hiddleston", "Daniel Radcliffe"], "Benedict Cumberbatch", "Entretenimiento")
    ],
    "Ciencia Ficción": [
        Pregunta("¿Qué autor escribió '1984'?", ["Aldous Huxley", "Ray Bradbury", "George Orwell", "Philip K. Dick"], "George Orwell", "Ciencia Ficción"),
        Pregunta("¿Cuál es el nombre del robot en la película 'Blade Runner'?", ["HAL 9000", "C-3PO", "R2-D2", "Roy Batty"], "Roy Batty", "Ciencia Ficción"),
        Pregunta("¿Cuál es el nombre del androide interpretado por Rutger Hauer en 'Blade Runner'?", ["HAL 9000", "C-3PO", "R2-D2", "Roy Batty"], "Roy Batty", "Ciencia Ficción"),
        Pregunta("¿Quién escribió la novela 'El fin de la eternidad'?", ["Isaac Asimov", "Arthur C. Clarke", "Robert A. Heinlein", "Isaac Asimov"], "Isaac Asimov", "Ciencia Ficción"),
        Pregunta("¿Cuál es el nombre del robot en la película 'WALL-E'?", ["EVE", "R2-D2", "C-3PO", "WALL-E"], "WALL-E", "Ciencia Ficción"),
        Pregunta("¿Quién escribió la novela 'Neuromante'?", ["Isaac Asimov", "Philip K. Dick", "Arthur C. Clarke", "William Gibson"], "William Gibson", "Ciencia Ficción"),
        Pregunta("¿Cuál es el nombre del protagonista en la saga 'Star Wars'?", ["Luke Skywalker", "Darth Vader", "Han Solo", "Princesa Leia"], "Luke Skywalker", "Ciencia Ficción"),
        Pregunta("¿Qué nave espacial es conocida como la 'Nave del Halcón Milenario'?", ["Millennium Falcon", "Star Destroyer", "X-Wing", "TIE Fighter"], "Millennium Falcon", "Ciencia Ficción"),
        Pregunta("¿En qué año se estrenó la primera película de 'Star Wars'?", ["1977", "1980", "1983", "1975"], "1977", "Ciencia Ficción"),
        Pregunta("¿Cuál es el nombre del robot protagonista en la película 'WALL-E'?", ["WALL-E", "EVE", "C-3PO", "R2-D2"], "WALL-E", "Ciencia Ficción")
    ]
   }
def solicitar_categorias():
    print("Elige hasta 3 categorías:")
    categorias_disponibles = {
        "Historia": [],
        "Arte": [],
        "Cultura Pop": [],
        "Ciencia y Tecnología": [],
        "Geografía": [],
        "Deportes": [],
        "Entretenimiento": [],
        "Ciencia Ficción": []
    }
    categorias_seleccionadas = []
    for i in range(3):
        print("Categorías disponibles:")
        for key in categorias_disponibles.keys():
            print(f"{key}.")
        categoria_elegida = input(f"Ingresa el número de la categoría {i+1} (o presiona Enter para terminar): ")
        if not categoria_elegida:
            break
        while categoria_elegida not in categorias_disponibles:
            print("Opción no válida. Intenta de nuevo.")
            categoria_elegida = input(f"Ingresa el número de la categoría {i+1}: ")
        categorias_seleccionadas.append(categoria_elegida)
    return categorias_seleccionadas, len(categorias_seleccionadas)

class Juego:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.resultados_rondas = []
        self.todas_las_preguntas = self.crear_lista_preguntas()

    def crear_lista_preguntas(self):
        todas_las_preguntas = []
        for categoria in categorias.values():
            todas_las_preguntas.extend(categoria)
        return todas_las_preguntas

    def iniciar_ronda(self, jugador):
        categorias_seleccionadas, total_categorias = solicitar_categorias()
        preguntas = []
        for categoria in categorias_seleccionadas:
            preguntas.extend(categorias[categoria])
        if total_categorias == 1:
            preguntas = preguntas[:5]
        elif total_categorias == 2:
            preguntas = preguntas[:10]
        elif total_categorias == 3:
            preguntas = preguntas[:15]
        ronda = Ronda(preguntas, categorias_seleccionadas)
        return ronda

    def jugar_ronda(self, ronda):
        ayuda = Ayuda(self, len(ronda.categorias_seleccionadas))
        puntos = 0
        respuestas_correctas = 0  # Contador de respuestas correctas
        for pregunta in ronda.preguntas:
            respuesta_usuario = self.jugar_pregunta(pregunta, ayuda)
            if not respuesta_usuario:
                return puntos  # Retorna los puntos obtenidos hasta ahora si el jugador se equivoca
            puntos += 1
            respuestas_correctas += 1
            # Verifica si se han alcanzado 6 respuestas correctas
            if respuestas_correctas % 6 == 0:
                continuar = input("Has alcanzado 6 respuestas correctas. ¿Deseas continuar jugando? (s/n): ")
                if continuar.lower() != 's':
                    return puntos  # Retorna los puntos obtenidos hasta ahora si el jugador decide no continuar
        return puntos  # Retorna los puntos obtenidos si el jugador responde todas correctamente

    def jugar_pregunta(self, pregunta, ayuda):
        print(pregunta.pregunta)
        for letra, respuesta in zip("ABCD", pregunta.respuestas):
            print(f"{letra}. {respuesta}")
        print("Opciones de ayuda:")
        print("1. Usar 50/50")
        print("2. Cambiar de pregunta")
        print("3. Usar ayuda de la API")  # Nueva opción de ayuda
        ayuda_opcion = input("Elige una opción de ayuda (1/2/3) o presiona Enter para continuar sin ayuda: ")

        if ayuda_opcion == "1":
            pregunta = ayuda.ayuda_50_50(pregunta)
            print("Respuestas actualizadas:")
            for letra, respuesta in zip("ABCD", pregunta.respuestas):
                print(f"{letra}. {respuesta}")
        elif ayuda_opcion == "2":
            pregunta = ayuda.cambio_pregunta()
            if pregunta is None:
                return False
            print("Nueva pregunta:")
            print(pregunta.pregunta)
            for letra, respuesta in zip("ABCD", pregunta.respuestas):
                print(f"{letra}. {respuesta}")
        elif ayuda_opcion == "3":
            ayuda.ayuda_api(pregunta)

        respuesta_usuario = input("Elige una respuesta (A/B/C/D): ")

        if respuesta_usuario == pregunta.respuesta_correcta:
            print("¡Correcto!")
            return True
        else:
            print("Incorrecto.")
            return False

    def jugar(self):
        for jugador in self.jugadores:
            print(f"Jugador: {jugador.nombre}")
            rondas_jugadas = 0
            rondas = []
            while rondas_jugadas < 3:  # Permitir hasta 3 rondas
                ronda = self.iniciar_ronda(jugador)
                puntos_ronda = self.jugar_ronda(ronda)
                if puntos_ronda is None:  # El jugador se equivocó y decidió no jugar de nuevo
                    break
                rondas_jugadas += 1
                print(f"Puntos en esta ronda: {puntos_ronda}")
                rondas.append({"puntos": puntos_ronda, "categorias": ronda.categorias_seleccionadas})
                continuar = input("¿Deseas jugar de nuevo? (s/n): ")
                if continuar.lower() != 's':
                    break
            self.resultados_rondas.append({
                "jugador": jugador.nombre,
                "total_puntos": sum(ronda["puntos"] for ronda in rondas),
                "rondas": rondas
            })

    def obtener_pregunta_aleatoria(self):
        return random.choice(self.todas_las_preguntas)

def obtener_categorias_y_preguntas():
    return categorias

