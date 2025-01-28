def invertirString(cadena):
    newCadena= ''
    for i in range(len(cadena)-1, -1, -1):
        newCadena += cadena[i]
    return newCadena

newCadena = invertirString('Hello world')
print(newCadena)