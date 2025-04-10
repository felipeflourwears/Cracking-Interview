"""
Ejercicio 6: Palíndromo
Pide una palabra o frase al usuario y determina si es un palíndromo.

📌 Un palíndromo es una palabra o frase que se lee igual al derecho y al revés (ignorando espacios y mayúsculas).\

"""



def word_palindromo(palindromo):
    palindromo=palindromo.lower()
    palindromo=palindromo.replace(" ", "")
    word = ''
    for i in range(len(palindromo)-1, -1, -1):
        if palindromo[i] != ' ':
            word+=palindromo[i]
    
    if word == palindromo:
        return "Es palindromo"
    else:
        return "No es palindromo"


try:
    
    print("Palindromo")
    palabra=input("Dame un frase para ver si es palindromo: ")
    print(word_palindromo(palabra))
    
except ValueError as e:
    print("Dame una frase valida")