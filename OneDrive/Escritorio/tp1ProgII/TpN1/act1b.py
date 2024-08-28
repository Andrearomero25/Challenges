'''
Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y 
cuando las letras que componen dicha palabra estén en orden alfabético, y False 
en caso contrario.
'''

def es_abc(palabra):
    # Iterar sobre los caráteres de la palabra
    for i in range(len(palabra) - 1):
        # Comparar cada carácter con el siguiente
        if palabra[i] > palabra[i + 1]:
            # Si se encuentra un carácter que no es alfabético, retornar False
            return False
        return True

# Ejemplos
print(es_abc('abc')) # True
print(es_abc('cba')) # False

# Nota: Esta función solo funciona para palabras que están formadas exclusivamente de letras alfabéticas. Si la palabra contiene caracteres especiales o números, la función retornará False.
        