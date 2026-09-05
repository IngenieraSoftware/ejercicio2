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

def promedio(a, b):
    """Devuelve el promedio de a y b."""
    return (a + b) / 2
def raiz_cuadrada(a):
    """Devuelve la raíz cuadrada de a."""
    return math.sqrt(a)

def MCD(a, b):
    """Devuelve el máximo común divisor de a y b."""
    if b == 0:
        return a
    else:
        return MCD(b, a % b) 
def modulo(a, b):
    """Devuelve el resto de la división de a entre b."""
    return a % b
  
def factorial(a):
    if a < 0:
        raise ValueError("El numero debe ser mayor o igual a 0")
    resultado = 1 
    for numero in range(2, a + 1):
        resultado *= numero
    return resultado
  
def raiz_cubica(numero):
    if numero < 0:
        return -((-numero) ** (1 / 3))
    return numero ** (1 / 3)

def menu():
    print("=== Calculadora - Ejercicio 2 ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Modulo")
    print("8. Factorial")
    print("9. Promedio")
    print("10. MCD")
    print("11. Raiz cubica")
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


    elif opcion == "7":
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = modulo(a, b)
        print(f"Resultado: {resultado}")
    
    elif opcion == "8":
        a = int(input("Ingresa un numero para calcular su factorial: "))
        try:
            resultado = factorial(a)
            print(f"El factorial de {a} es: {resultado}")
        except ValueError as e:
            print(e)


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
        
    elif opcion == "11":
        a = float(input("Ingresa el numero: "))
        resultado = raiz_cubica(a)
        print(f"Resultado: {resultado}")

            
    elif opcion == "0":
        print("Saliendo...")
    else:
        print("Opcion no valida")


if __name__ == "__main__":
    menu()




