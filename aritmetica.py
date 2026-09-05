def suma(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def menu():
    print("=== Calculadora - Ejercicio 2 ===")
    print("1. Suma")
    print("0. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = suma(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == "0":
        print("Saliendo...")
    else:
        print("Opcion no valida")


if __name__ == "__main__":
    menu()

def factorial(a):
    if a < 0:
        raise ValueError("El numero debe ser mayor o igual a 0")
    resultado = 1 
    for numero in range(2, a + 1):
        resultado *= numero

    return resultado
