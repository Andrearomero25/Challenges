'''
Escribir un programa que resuelva la secuencia de Fibonacci a pedido del 
usuario. Deberá codificar una función fibonacci(numero), cuyo parámetro 
numero debe ser ingresado por el usuario y su tipo, al igual que en el ejercicio 
anterior, validado. La función debe encargarse de calcular la secuencia para 
dicho número. A continuación, una descripción matemática de la famosa 
secuencia:

'''

def fibonacci(numero):
    if numero <= 0:
        return 'Error: El número debe ser mayor que 0.'
    elif numero == 1:
        return [0]
    elif numero == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, numero):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        return fib_sequence

# Pedir al usuario el número para calcular la secuencia de Fibonacci

numero = int(input('Ingrese un número entero: '))

# Validar el número

if numero <= 0:
    print('Error: El número debe ser mayor que 0.')
else:
    fib_sequence = fibonacci(numero)
    print('Secuencia de Fibonacci:', fib_sequence)

'''
Ejecución:
Ingrese un número entero: 10
Secuencia de Fibonacci: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''