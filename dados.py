import random

def tirar_dados():
    valorDelDado1 = random.randint(1, 6)
    valorDelDado2 = random.randint(1, 6)
    suma = valorDelDado1 + valorDelDado2
    print(f"\nHas tirado un {valorDelDado1} y un {valorDelDado2}.")
    print(f"La suma es: {suma}")

def main():
    print("Bienvenido al simulador de tirada de dados 🎲")
    while True:
        tirar_dados()
        respuesta = input("¿Querés tirar los dados otra vez? (s/n): ").strip().lower()
        if respuesta != 's':
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()
