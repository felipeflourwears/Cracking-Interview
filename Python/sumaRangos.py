"""
Ejercicio 2: Suma de Números en un Rango
Pide dos números al usuario e imprime la suma de todos los números en ese rango (incluyéndolos).
1+2+3+4+5=15
3+4+5=12
-2+-1+0=-3
"""

try:
 x=int(input("Dame el primer numero: "))
 y=int(input("Dame el segundo numero: "))
 if(x>y):
     raise ValueError("El primer número debe ser menor o igual al segundo.")
 sum_total=0
 for i in range(x, y+1):
     sum_total+=i
 print("La suma total es: ", sum_total)
except ValueError:
    print("Mete rangos validos")
    
