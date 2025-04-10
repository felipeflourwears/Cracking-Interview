"""
Ejercicio 5: Número más grande
Pide tres números al usuario y muestra cuál es el mayor.

"""
def search_num_mayor(num1, num2, num3):
    arrayNum = [num1, num2, num3]
    numMay = max(arrayNum)
    return numMay
try:
    
    print("Dame 3 numeros para ver cual es el mayor")
    num1=int(input("Dame el primer numero: "))
    num2=int(input("Dame el segundo numero: "))
    num3=int(input("Dame el tercer numero: "))
    numMayor=search_num_mayor(num1, num2, num3)
    print("El numero mayor es: ", numMayor)
except ValueError as e:
    print("Dame 3 numeros validos")



