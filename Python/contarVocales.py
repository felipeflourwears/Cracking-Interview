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

def contar_vocales(frase):
    frase = frase.lower()
    try:
        for i in range(0, len(frase), 1):
            if frase[i] in vocales:
                letter = frase[i]
                vocales_dic[letter] += 1

        print(vocales_dic)

        for i in vocales_dic:
            print("Letra:", i, "Cantidad:", vocales_dic[i])

    except Exception as e:
        raise ValueError("La frase no puede estar vacía")



contar_vocales(frase)
    
