class PelotaConNombre:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __establecerEstadoInicial(self):
        self.__establecerEstado('FRENADA')

    def _establecerEstado(self, estado):
        self.estado = estado


    def establecerNombre(self, nombre):
        self.nombre = nombre

    def establecerEstado(self):
        return self.estado

    def obtenerNombre(self):
        return self.nombre

    def rodar(elf):
        print('Rodando...')
        self._establecerEstado('RODANDO')

    def frenar(self):
        print('Frenando...')
        self._establecerEstado('FRENADA')

    def imprimirEstado(self):
        print(f'Estado de {self.nombre()} : {self.estado()}')


'''
pelota1 = PelotaConNombre('Pelota 1')
pelota1.__establecerEstadoInicial()
pelota1.imprimirEstado()
'''

pelota1 = PelotaConNombre('Pelota 1')
pelota2 = PelotaConNombre('Pelota 2')
pelota1.establecerNombre('Pelota 2')
pelota2.establecerNombre('Pelota 1')
print(pelota1.obtenerNombre())
print(pelota2.obtenerNombre())