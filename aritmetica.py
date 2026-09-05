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

def MCD(a, b):
    """Devuelve el máximo común divisor de a y b."""
    if b == 0:
        return a
    else:
        return MCD(b, a % b) 

def promedio(a, b):
    """Devuelve el promedio de a y b."""
    return (a + b) / 2

def menu():
    print("=== Calculadora - Ejercicio 2 ===")
    print("1. Suma")
    print("2. Resta")
    print("4. Division")
    print("9. Promedio")
    print("3. Multiplicacion")
    print("4. Division")
    print("10. MCD")
    print("0. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = suma(a, b)
        print(f"Resultado: {resultado}")

    if opcion == "2":
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

    elif opcion == "9":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = promedio(a, b)
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