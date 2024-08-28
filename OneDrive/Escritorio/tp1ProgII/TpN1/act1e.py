'''
Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de 
números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista 
e imprima ambas. La lista de números la ingresa el usuario en forma de números 
separados por coma.
Suponiendo que el usuario ingresa la siguiente lista:
1,2,3,4,5,6,7,8,9
Entonces, la salida del programa debería ser:
2,4,6,8
1,9,25,49,8
'''

def numeros_par_impar(entrada):
    # Convertir la cadena de entrada en una lista de enteros
    numeros = list(map(int, entrada.split(',')))
    # Lista para números pares e impares y elevar los impares al cuadrado
    pares = []
    impares_cuadrado = []
    # Separar números pares e impares  y elevar los impares al cuadrado
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares_cuadrado.append(numero ** 2)

    # Imprimir las listas resultantes
    print(','.join(map(str, pares)))
    print(','.join(map(str, impares_cuadrado)))

entrada = '1,2,3,4,5,6,7,8,9' # Debe imprimir: 2,4,6,8
# 1,9,25,49,81
numeros_par_impar(entrada)
