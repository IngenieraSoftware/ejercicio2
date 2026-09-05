def suma(a, b):
    """Devuelve la suma de a y b."""
    return a + b

def division(a,b):
    """Devuelve la division de a y b."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b


def promedio(a, b):
    """Devuelve el promedio de a y b."""
    return (a + b) / 2

def menu():
    print("=== Calculadora - Ejercicio 2 ===")
    print("1. Suma")
    print("4. Division")
    print("9. Promedio")
    print("0. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = suma(a, b)
        print(f"Resultado: {resultado}")

    elif opcion == "4":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        try:
            resultado = division(a, b)
            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == "9":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = promedio(a, b)
        print(f"Resultado: {resultado}")
                
    elif opcion == "0":
        print("Saliendo...")
    else:
        print("Opcion no valida")


if __name__ == "__main__":
    menu()

def modulo(a, b):
    """Devuelve el resto de la división de a entre b."""
    return a % b