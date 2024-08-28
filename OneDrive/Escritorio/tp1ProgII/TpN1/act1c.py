'''
Escriba un procedimiento procesar_palabras(entrada) que acepte una 
secuencia de palabras separadas por coma, las ordene y las imprima. 
Suponiendo que la entrada provista al programa es la siguiente:
te,felicito,que,bien,actuas
La salida esperada es:
actuas,bien,felicito,que,te
'''

def procesar_palabras(entrada):
    # Dividir la cadena en una lista de palabras
    palabras = entrada.split(',')
    # Ordenar la lista de palabras alfabéticamente
    palabras.sort()
    # Unir las palabras ordenadas en una cadena
    salida = ','.join(palabras)
    # Imprimir salida 
    print(salida)

# Ejemplo
entrada = 'te,felicito,que,bien,actuas'
procesar_palabras(entrada)