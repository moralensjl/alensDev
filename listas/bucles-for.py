'''  Bucles for  '''

for numero in range(5):
    print(numero * 2)
# 0
# 2
# 4
# 6
# 8

nombres = ['Pedro', 'Cecilia', 'Maria', 'Miguel']
for nombre in nombres:
    print(nombre)

# Pedro
# Cecilia
# Maria
# Miguel

for index, nombres in enumerate(nombres, 1):
    print(f'El nombre de {nombres} tiene el indice {index}')

# El nombre de Pedro tiene el indice 1
# El nombre de Cecilia tiene el indice 2
# El nombre de Maria tiene el indice 3
# El nombre de Miguel tiene el indice 4

comprex = [f'La persona{index} se llama {nombres}' for index, nombres in enumerate(nombres)]
print(comprex)