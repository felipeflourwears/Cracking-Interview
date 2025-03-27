"""
Ejercicio 2: Suma de Números en un Rango
Pide dos números al usuario e imprime la suma de todos los números en ese rango (incluyéndolos).
"""

try:
 x=int(input("Dame el primer numero: "))
 y=int(input("Dame el segundo numero: "))
 sum=0
 for i in range(x-1, y+1):
     sum+=i
 print("La suma total es: ", sum)
except ValueError:
    print("Mete rangos validos")