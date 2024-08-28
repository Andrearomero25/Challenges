class NaveEspacial:

    #Atributo de clase
    max_deposito = 1000
    parsec = 100

    # Método de inicialización
    def __init__(self, co, comb):
        self.estado_alertas = False

        # Atributo de instancia
        self.color = co
        if (comb > self.max_deposito):
            self.combustible = self.max_deposito
        else:
            self.combustible = comb

    
    def establecerEstadoAlertas(self, habilitar):
        self.estado_alertas = habilitar

    def obtenerCombustible(self):
        return self.combustible

    def agregarCombustible(self, comb):
        if self.combustible + comb > self.max_deposito:
            if self.estado_alertas:
                print('¡De los ' + str(comb) + ' litros, solo se pudieron cargar ' + str(self.max_deposito - self.combustible) + ' litros!')
            self.combustible = self.max_deposito
        else:
            if self.estado_alertas:
                print('Se agregaron ' + str(comb) + ' litros de combustible.')
            self.combustible += comb

'''
nave_espacial1 = NaveEspacial('R', 500)
print('Combustible de Nave 1: ' + str(nave_espacial1.obtenerCombustible()))
nave_espacial1.establecerEstadoAlertas(True)
nave_espacial1.agregarCombustible(700)
print('Combustible de Nave 1: ' + str(nave_espacial1.obtenerCombustible()))

nave_espacial2 = NaveEspacial('A', 0)
print(f'Combustible de Nave 2: {str(nave_espacial2.obtenerCombustible())}')
nave_espacial2.establecerEstadoAlertas
nave_espacial2.agregarCombustible(200)
print(f'Combustible de Nave 2: {str(nave_espacial2.obtenerCombustible())}')
'''



'''
nave_espacial1 = NaveEspacial()
print('Combustible de Nave 1: ' + str(nave_espacial1.obtenerCombustible()))
nave_espacial1.establecerEstadoAlertas(True)
nave_espacial1.agregarCombustible(700)
print('Combustible de Nave 1: ' + str(nave_espacial1.obtenerCombustible()))
'''



'''
nave_espacial1 = NaveEspacial
print('Combustible de Nave 1: ' + str(nave_espacial1.obtenerCombustible()))
nave_espacial1.establecerEstadoAlertas(True)
nave_espacial1.agregarCombustible(700)
print('Combustible de Nave 1: ' + str(nave_espacial1.obtenerCombustible()))
'''



'''
nave_espacial1 = NaveEspacial('R', 500)
nave_espacial1.establecerEstadoAlertas(True)
nave_espacial1.combustible += 700
print(nave_espacial1.obtenerCombustible())
'''


nave_espacial1 = NaveEspacial('R', 500)
nave_espacial2 = NaveEspacial('R', 500)
print(f'Nave 1 = Nave 2: {str(nave_espacial1 == nave_espacial2)}')