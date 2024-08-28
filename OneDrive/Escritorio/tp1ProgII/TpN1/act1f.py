'''
Un portal web requiere un formulario de alta de usuario donde se ingrese, 
mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python, 
una función contrasena_valida(contrasena) que devuelva True en caso de 
superar las siguientes validaciones sobre la contraseña proporcionada por el 
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
AbC.1 23 es válida: False
ÁbC.123 es válida: False
Para la búsqueda de caracteres de cierto tipo (mayúsculas, acentos, espacios y 
otros) debe hacerse uso de la librería re:
- https://docs.python.org/es/3/library/re.html
- https://relopezbriega.github.io/blog/2015/07/19/expresiones-regularescon-python/
- Para buscar caracteres especiales, puede utilizarse la siguiente expresión
[$&+,:;=?@#|<>.^*()%!-]
'''

import re

def contrasena_valida(contrasena):
    # Verificar la longitud
    if not (6 <= len(contrasena) <= 20):
        return False
    # Verificar la presencia de al menos un número
    if not re.search(r'\d', contrasena):
        return False
    # Verificar la presencia de al menos dos mayúsculas
    if not re.search(r'\d', contrasena):
        return False
    # Verificar la presencia de al menos dos letras nayúsculas
    if sum(1 for c in contrasena if c.isupper()) < 2:
        return False
    # Verificar la presencia de al menos un carácter especial
    if not re.search(r'[$&+,:;=?@#|<>.^*()%!-]', contrasena):
        return False
    # Verificar que no contenga espacios
    if ' ' in contrasena:
        return False
    return True

# Ejemplo

print(contrasena_valida('abc.123'))  # False
print(contrasena_valida('Abc.123'))  # False
print(contrasena_valida('AbC.123'))  # True
print(contrasena_valida('AbC.1 23'))  # False
print(contrasena_valida('ÁbC.123'))  # True


# Para buscar caracteres especiales, puede utilizarse la siguiente expresión

# $&+,:;=?@#|<>.^*()%!-]