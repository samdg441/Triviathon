from modulos import Jugador, Juego, solicitar_categorias
def solicitar_nombre():
    nombre = input("Ingresa el nombre del jugador: ")
    return nombre
def mostrar_introduccion():
  print("¡Bienvenido al Triviathon!")
  print("En este emocionante juego, competiras en una serie de preguntas de trivia. El objetivo es responder correctamente a las preguntas de las categorías seleccionadas para ganar puntos.")
  print("\nReglas del juego:")
  print("1. Cada jugador responderá a las preguntas de las categorías seleccionadas.")
  print("2. Las preguntas se seleccionan de manera aleatoria de las categorías elegidas.")
  print("3. Tienes la opción de usar dos tipos de ayudas durante el juego:")
  print("   - 50/50: Elimina dos respuestas incorrectas de las opciones disponibles.")
  print("   - Cambio de pregunta: Puedes cambiar la pregunta actual por otra de la misma categoría.")
  print("4. Puedes usar una ayuda por categoría seleccionada, pero no más de una por ronda.")
  print("5. El juego continuará hasta que todas las preguntas de las categorías seleccionadas hayan sido respondidas o hasta que decidas no continuar.")
  print("\n¡Vamos a empezar!")

def mostrar_resultados_finales(resultados_rondas):
    for resultado in resultados_rondas:
        print(f"Jugador: {resultado['jugador']}")
        print(f"Total de puntos: {resultado['total_puntos']}")
        for i, ronda in enumerate(resultado['rondas'], start=1):
            print(f"Ronda {i}: Puntos: {ronda['puntos']}, Categorías: {', '.join(ronda['categorias'])}")
def main():
    nombres = []
    for i in range(1, 2): # Ajusta el rango según sea necesario
        nombre = solicitar_nombre()
        nombres.append(nombre)

    jugadores = [Jugador(nombre) for nombre in nombres]
    juego = Juego(jugadores)
    juego.jugar()
    mostrar_resultados_finales(juego.resultados_rondas)

if __name__ == "__main__":
    main()
