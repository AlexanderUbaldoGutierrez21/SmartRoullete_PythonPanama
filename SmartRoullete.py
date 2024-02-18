import random
import os

# Palabras para la ruleta
palabras = ["python", "programing", "computadora", "technological", "inteligencia"]

# Definir la función para jugar
def jugar_ruleta():
    palabra_secreta = random.choice(palabras)
    palabra_adivinada = "_" * len(palabra_secreta)
    intentos = 3
    puntos = 0

    while intentos > 0:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\nPalabra a adivinar:", palabra_adivinada)
        print("Intentos restantes:", intentos)
        print("Puntos:", puntos)

        letra = input("Ingresa una letra: ").lower()

        if letra in palabra_secreta:
            palabra_adivinada = "".join(l if l == letra or a == letra else a for a, l in zip(palabra_adivinada, palabra_secreta))
            puntos += 1
        else:
            intentos -= 1

        if palabra_adivinada == palabra_secreta:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
            print("¡Has ganado con", puntos, "puntos!")
            return

    os.system('clear' if os.name == 'posix' else 'cls')
    print("\n¡Se acabaron los intentos! La palabra secreta era:", palabra_secreta)

# Jugar hasta que alguien adivine la palabra
while True:
    jugar_ruleta()
    respuesta = input("\n¿Deseas jugar de nuevo? (s/n): ").lower()
    if respuesta != "s":
        break