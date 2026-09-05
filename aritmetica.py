import math

def suma(a, b):
    """Devuelve la suma de a y b."""
    return a + b
def multiplicacion(a, b):
    """Devuelve la multiplicacion de a y b."""
    return a * b

def resta(a, b):
    """Devuelve la resta de a y b."""
    return a - b

def division(a,b):
    """Devuelve la division de a y b."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def potencia(a,b):
    """Devuelve la potencia de a elevado a b"""
    return pow(a,b)

def raiz_cuadrada(a):
    """Devuelve la raíz cuadrada de a."""
    return math.sqrt(a)


def menu():
    print("=== Calculadora - Ejercicio 2 ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("10. MCD")
    print("0. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = suma(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == "2":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = resta(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == "3":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = multiplicacion(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == "4":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        try:
            resultado = division(a, b)
            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == "5":
        a = float(input("Ingresa la base: "))
        b = float(input("Ingresa el exponente: "))
        try:
            resultado = potencia(a, b)
            print(f"Resultado: {resultado}")
        except ZeroDivisionError:
            print("Error: No se puede elevar 0 a un exponente negativo.")
            
    elif opcion == "6":
        a = float(input("Ingresa el numero: "))
        resultado = raiz_cuadrada(a)
        print(f"Resultado: {resultado}")
    elif opcion == "10":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = MCD(a, b)
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