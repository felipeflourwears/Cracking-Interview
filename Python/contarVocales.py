"""
Ejercicio 3: Contar Vocales en una Frase
Solicita una frase al usuario y cuenta cuántas vocales (a, e, i, o, u) tiene.
"""

frase=str(input("Dame una frase: "))
vocales = ["a", "e", "i", "o", "u"]
vocales_dic = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}
print(vocales_dic["a"])

try:
    for i in range(0, len(frase), 1):
        if(frase[i] in vocales):
            print(frase[i])
            vocales_dic[i]+=1
    print(vocales_dic)
except ValueError as e:
    print("Error: ", e)
    