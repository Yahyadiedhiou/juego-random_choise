import random

def guessing_game(palabritas):
    # Seleccionar la palabra correcta de forma aleatoria
    palabra_correcta = random.choice(palabritas)
    intentos = 0

    while intentos < 3:
        # Pedir al usuario que adivine
        entrada = input("Prueba suerte: ").strip()

        # Aumentar el contador de intentos
        intentos += 1

        # Comprobar si el jugador acertó
        if entrada == palabra_correcta:
            print("¡Has acertado! 🎉")
            return

        # Pistas de "Caliente" o "Frío" según la cercanía de la palabra
        if entrada[0] == palabra_correcta[0]:  # Comparar la primera letra
            print("Caliente, caliente. Estás cerca de la palabra.")
        else:
            print("Frío, frío... Vamos, espabila pipiolo.")

    # Si se acaban los intentos y no se ha adivinado
    print(f"Se te han acabado los intentos. Has fallado. La palabra correcta era: {palabra_correcta}")

# Lista de palabras
palabritas = [
    "Horizonte",
    "Laberinto",
    "Luciérnaga",
    "Tarántula",
    "Nebulosa",
    "Alquimia",
    "Péndulo",
    "Murmullo",
    "Abismo",
    "Relámpago",
    "Corazón",
    "Cúpula",
    "Éter",
    "Bosque",
    "Espejismo",
    "Sereno",
    "Refugio",
    "Gaviota",
    "Estrella",
    "Susurro"
]

# Ejecutar el juego
guessing_game(palabritas)
