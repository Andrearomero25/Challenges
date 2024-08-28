'''
Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo 
que numero = 10:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
En el programa que invoque dicha función:
i. El usuario debe poder ingresar el valor del parámetro numero.
ii. Debe validarse que el dato ingresado por el usuario corresponda a 
un dígito, y no a otro tipo de dato como un carácter.
iii. El cálculo debe realizarse utilizando algún tipo de bucle (ej: for, 
while).
BONUS: Luego, codificar una función equivalente que utilice recursividad.
'''

def suma(numero):
    total = 0
    for i in range(1, numero + 1):
        total += i
    return total

# Ingreso del parametro por el usuario,input() para permitir que el usuario ingrese un número. 
numero = input('Ingrese un número: ')

# Validación del parametro, se utiliza el método isdigit() para verificar que el valor ingresado sea un dígito.
if numero.isdigit():
    numero = int(numero)
    resultado = suma(numero)
    print(f'La suma de los números desde 1 hasta {numero} es: {resultado}')
else:
    print('Error: Ingreso inválido. Debe ingresar un dígito.')

# Ejecución de la función con recursividad suma_recursiva(numero), se utiliza una llamada recursiva para sumar los números desde 1 hasta numero. (BONUS)
def suma_recursiva(numero):
    if numero == 1:
        return 1
    else:
        return numero + suma_recursiva(numero - 1)

# Ingreso del parámetro por el usuario
numero = input('Ingrese un número: ')

# Validación del parámetro
if numero.isdigit():
    numero = int(numero)
    resultado = suma_recursiva(numero)
    print(f'La suma de los números desde 1 hasta {numero} es: {resultado}')
else:
    print('Error: Ingreso inválido. Debe ingresar un dígito.')