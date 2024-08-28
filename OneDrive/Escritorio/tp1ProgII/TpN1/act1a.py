'''
Escribir una función de nombre palabra_no_tiene_letras(palabra, 
letras_prohibidas), la cual retorne True si es que los caracteres que componen 
una palabra no se encuentran en una lista de caracteres prohibidos.
'''

def palabra_no_tiene_letras(palabra, letras_prohibidas):
    palabra = palabra.lower()  # Convertimos la palabra a minúsculas para facilitar la comparación con las letras prohibidas
    for letra in palabra:
        # Iterar sobre los caracteres de la palabra
        if letra in letras_prohibidas:
            # Si se encuentra alguna letra prohibida, retornamos False
            return False
    # Si no se encontró ninguna letra prohibida, retornamos True
    return True

# Ejemplos
print(palabra_no_tiene_letras('HOLA', ['l', 'o']))  # False
print(palabra_no_tiene_letras('PYTHON', ['h', 'o']))  # False
print(palabra_no_tiene_letras('matemática', ['j','k'])) # True