"""
Ejercicio 1: Números Pares e Impares
Escribe un programa que pida un número al usuario y determine si es par o impar.

"""

try:
    x = int(input("Dame un número: "))
    if x % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
except ValueError:
    print("Por favor, ingresa un número válido.")
