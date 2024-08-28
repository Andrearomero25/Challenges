'''
Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2)
que tome ambas como parámetros e imprima dos listas, cada una con:
i. Los elementos en común, en orden inverso.
ii. Los elementos no comunes, en orden alfabético.
El programa debería arrojar el siguiente resultado:
listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
['c', 'b']
['a', 'd', 'e']
'''

def lista_diferencia(lista1, lista2):
    # Encontrar elementos en común
    comunes = list(set(lista1) & set(lista2))
    # Ordenar los elementos en común en orden inverso
    comunes.reverse()
    # Encontrar elementos no comunes
    no_comunes = list(set(lista1) ^ set(lista2))
    # Ordenar los elementos no comunes en orden alfabético
    no_comunes.sort()
    # Imprimir las listas
    print('Listas:', comunes, no_comunes)

# Ejemplo
lista_diferencia(['b','a','c'],['e','b','d','c'])

# Output:
 # Listas: ['c', 'b'] ['a', 'd', 'e']

'''
Nota: La función set(lista1) ^ set(lista2) calcula la diferencia simétrica de las dos listas, es decir, los elementos que están en una lista pero no en la otra.
'''