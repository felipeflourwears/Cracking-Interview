"""
Ejercicio 7: Números Primos
Escribe un programa que pida un número al usuario y determine si es un número primo.

Tip: Un número primo es aquel que solo tiene dos divisores: 1 y él mismo.

"""

def numPrimo(num):
    for i in range(2, num):
        if num % i == 0:
            print("No es primo")
            return
    print("Es primo")
    return
        
        
    
try:
    num=int(input("Dame un numero: "))
    numPrimo(num)
    


except ValueError:
    print("Introduce numeros validos")