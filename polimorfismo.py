'''  POLIMORFISMO  '''

# EJEMPLO SIN POLIMORFISMO
class Perro:
    def ladridos(self):
        return 'Guau!'
    

class Gato:
    def maullido(self):
        return 'Miau!'
        
#CREAMOS EL OBJETO GATO Y PERRO
mi_perro = Perro()
mi_gato = Gato()

#LLAMAMOS SUS METODOS
print(mi_gato.maullido()) # Miau!
print(mi_perro.ladridos()) # Guau!


# EJEMPLO SIN POLIMORFISMO
class Perro1:
    def Sonido(self):
        return 'Guau!'
    

class Gato1:
    def Sonido(self):
        return 'Miau!'
    

mi_perro = Perro1()
mi_gato = Gato1()    

print(mi_gato.Sonido()) # Miau!
print(mi_perro.Sonido()) # Guau!
