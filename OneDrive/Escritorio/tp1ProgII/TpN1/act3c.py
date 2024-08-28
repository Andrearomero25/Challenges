'''
Tal como sucede con la lógica proposicional, en Python muchas veces las 
expresiones booleanas pueden ser simplificadas manteniendo el valor de 
verdad de la expresión. Así, por ejemplo, (a and b) or (b and a) es equivalente 
a a and b. A continuación, intente simplificar las siguientes expresiones y 
escriba un procedimiento procesar_sentencias(a, b, c) que permita evaluar el 
valor de verdad de las expresiones ya simplificadas:
i. (a or b) or (b and c)
ii. b and c or False
iii. a and b or c or (b and a)
iv. a == True or b == False

'''


def procesar_sentencia(a, b, c):
    # Simplificación de las expresiones
    exp1 = a or b
    exp2 = b and c
    exp3 = a and b or c
    exp4 = a or not b
    
    # Evaluación de las expresiones
    resultado1 = exp1
    resultado2 = exp2
    resultado3 = exp3
    resultado4 = exp4 

    # Devolución de los resultados
    print(f'Resultado de (a or b) or (b and c): {resultado1}')

    print(f'Resultado de b and c or False: {resultado2}')

    print(f'Resultado de a and b or c or (b and a): {resultado3}')

    print(f'Resultado de a == True or b == False: {resultado4}')

# Nota: La evaluación de las expresiones puede ser más efectiva cuando las expresiones son más complejas.
a = True
b = False
c = True
procesar_sentencia(a, b, c)



'''
Salida esperada:
(True, False, True, True)
'''