"""
Ejercicio 4: Tabla de Multiplicar
Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10.

"""
def numMultiplicar(num):
    for i in range(0, 11, 1):
        print(num, " x ", i, "=", num * i )
        
        
try:
    num = int(input("Dame un número: "))
    numMultiplicar(num)
    
except ValueError:
    print("Eso no es un número entero válido.")

        
        
