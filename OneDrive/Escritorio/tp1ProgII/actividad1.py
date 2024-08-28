'''
1. Sección A: Ejercicios básicos de Python
Resolver cada ejercicio en un archivo diferente.
a. Escribir una función de nombre palabra_no_tiene_letras(palabra, letras_prohibidas), la cual retorne True si es que los caracteres que componen 
una palabra no se encuentran en una lista de caracteres prohibidos.
b. Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y cuando las letras que componen dicha palabra estén en orden alfabético, y False 
en caso contrario.
c. Escriba un procedimiento procesar_palabras(entrada) que acepte una secuencia de palabras separadas por coma, las ordene y las imprima. 
Suponiendo que la entrada provista al programa es la siguiente:te,felicito,que,bien,actuas
La salida esperada es:
actuas,bien,felicito,que,te
d. Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2)
que tome ambas como parámetros e imprima dos listas, cada una con:
i. Los elementos en común, en orden inverso.
ii. Los elementos no comunes, en orden alfabético.
El programa debería arrojar el siguiente resultado:
listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
['c', 'b']
['a', 'e', 'd']

e. Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista 
e imprima ambas. La lista de números la ingresa el usuario en forma de números separados por coma.
Suponiendo que el usuario ingresa la siguiente lista:
1,2,3,4,5,6,7,8,9
Entonces, la salida del programa debería ser:
2,4,6,8
1,9,25,49,81
f. Un portal web requiere un formulario de alta de usuario donde se ingrese, mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python, 
una función contrasena_valida(contrasena) que devuelva True en caso de superar las siguientes validaciones sobre la contraseña proporcionada por el 
usuario:
i. Longitud entre 6 y 20 caracteres.
ii. Debe contener al menos un número.
iii. Debe contener al menos dos mayúsculas.
iv. Debe contener al menos un carácter especial.
v. No puede contener espacios.
La salida esperada es la siguiente:
abc.123 es válida: False
Abc.123 es válida: False
AbC.123 es válida: True
AbC.123 es válida: False
ÁbC.123 es válida: False
Para la búsqueda de caracteres de cierto tipo (mayúsculas, acentos, espacios y 
otros) debe hacerse uso de la librería re:
- https://docs.python.org/es/3/library/re.html
- https://relopezbriega.github.io/blog/2015/07/19/expresiones-regularescon-python/
- Para buscar caracteres especiales, puede utilizarse la siguiente expresión
[$&+,:;=?@#|<>.^*()%!-]


'''

import re
 # Ejercicio a
def palabra_no_tiene_letras(palabra, letras_prohibidas):
    for letra in palabra:
        if letra in letras_prohibidas:
            return False
    return True

letras_prohibidas = ['w', 'x', 'y', 'z']
print(palabra_no_tiene_letras('Matemática')) 
print(palabra_no_tiene_letras('Pyhon'))

# Ejercicio b
def es_abc(palabra):
    return palabra == ''.join(sorted(palabra))
    
palabra = 'abc'
print(es_abc(palabra))
palabra = 'Matematica'
(es_abc)

# Ejercicio c
def procesar_palabras(entrada):
    # Separar las palabras por comas
    palabras = entrada.split(',')
    # Ordenar las palabras alfabéticamente
    palabras.sort()
    # Unir las palabras ordenadas en una sola cadena separadas por comas
    print(','.join(palabras))

entrada = 'te,felicito,que,bien,actuas'
procesar_palabras(entrada)

# Ejercicio d

def listas_diferencia(lista1, lista2):
    # Encontramos elementos en común
    comunes = list(set(lista1) & set(lista2))
    comunes.reverse()
    no_comunes = list(set(lista1) ^ set(lista2))
    no_comunes.sort()

print('Listas:', comunes, no_comunes)
listas_diferencia(['b', 'a', 'c'],['e', 'b', 'd', 'c'])

# Ejercicio e

def numeros_par_impar(entrada):
    numeros = [int(num) for num in entrada.split(',')]
    numeros_par = []
    numeros_impar = []
    for num in numeros:
        if num % 2 == 0:
            numeros_par.append(num ** 2)
        else:
            numeros_impar.append(num)
        print(f'{num} elevado al cuadrado: {num ** 2}')

    print('Numeros pares:', numeros_par)
    print('Numeros impares:', numeros_impar)

# Ejercicio f

def contrasena_valida(contrasena):
    longitud = len(contrasena)
    tiene_numero = re.search(r'\d', contrasena)
    tiene_mayuscula = re.search(r'[A-Z]', contrasena)
    tiene_caracter_especial = re.search(r'[$&+,:;=?@#|<>.^*()%!-]', contrasena)
    no_tiene_espacios = re.search(r'\s', contrasena)
    return longitud >= 6 and longitud <= 20 and tiene_numero and tiene_mayuscula and tiene_caracter_especial and no_tiene_espacios is None
    print(f'{contrasena} es válida: {valida}')
    # Para la búsqueda de caracteres de cierto tipo (mayúsculas, acentos, espacios y otros)
    # debe hacerse uso de la librería re:
    # https://docs.python.org/es/3/library/re.html
    # https://relopezbriega.github.io/blog/2015/07/19/expresiones-regulares-con-python/
    # Para buscar caracteres especiales, puede utilizarse la siguiente expresión
    # [$&+,:;=?@#|<>.^*()%!-]

    # Ejercicio a
    palabra_no_tiene_letras('hola', ['o', 'l'])  # True
    print(palabra_no_tiene_letras('hola', ['e', 'l']))  # False
    # Ejercicio b
    print(es_abc('abc'))  # True
    print(es_abc('cba'))  # True
    print(es_abc('abcde'))  # False
    # Ejercicio c
    procesar_palabras('te,felicito,que,bien,actuas')
    # Ejercicio d
    listas_diferencia(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
    # Ejercicio e
    numeros_par_impar('1,2,3,4,5,6,7,8,9')
    # Ejercicio f
    print(contrasena_valida('abc.123'))  # False
    print(contrasena_valida('Abc.123'))  # False
    print(contrasena_valida('AbC.123'))  #
    print(contrasena_valida('AbC.1 23'))  # False
    print(contrasena_valida('ÁbC.123'))  # False
    

