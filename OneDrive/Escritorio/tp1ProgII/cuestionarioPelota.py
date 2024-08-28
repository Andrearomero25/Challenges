class Pelota:
    """
    Esta clase representa una pelota.
    """
    def __init__(self):
        self.estado = 'FRENADA'

    
    def obtenerEstado(self):
        return self.estado

    def rodar(self):
        print('Rodando...')
        self.estado = 'RODANDO'
    
    def frenar(self):
        print('Frenando...')
        self.estado = 'FRENANDA'

    def imprimirEstado(self):
        print(f'Estado: {self.estado}')


# Crear una pelota y probar sus métodos
'''
pelota = Pelota()
pelota.imprimirEstado()

pelota.rodar()
print(pelota.obtenerEstado())

pelota.frenar()
pelota.imprimirEstado()
'''

'''
pelota = new Pelota()   #Error de sintaxis
pelota.imprimir_estado()
pelota.rodar()
print(pelota.obtenerEstado())
pelota.frenar()
pelota.imprimir_estado()
'''