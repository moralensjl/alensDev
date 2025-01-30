import math

def saludar():
    nombre = input('Cual es tu nombre?')
    print(f'Hola, {nombre} Bienvenido PYTHONIANOS!!!')

saludar()

# definir una funcion que devuelva el area de un circulo

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

calcularRadio = calcular_area_circulo(4)
print(f'El area del circulo es: {calcularRadio}') # El area del circulo es: 50.26548245743669


calcularRadio = calcular_area_circulo(6)
print(f'El area del circulo es: {calcularRadio}') # El area del circulo es: 113.09733552923255

# define una funcion que calcule y devuelva el precio total de un producto dado su precio base y su impuesto
def calcular_precio_total(precio, IVA = 0.16):
    total = precio + (precio * IVA)
    return total

precioTotal = calcular_precio_total(8000)
print(precioTotal) # 9280.0

precioTotal = calcular_precio_total(950, 0.30)
print(precioTotal) # 1235.0


def numeros_promedio(num1, num2, num3, num4, num5):
    promedio_total = num1 + num2 + num3 + num4 + num5 / 2
    return promedio_total

# (*num1) cantidad indeterminada de argumentos

totalDelPromedio = numeros_promedio(12, 23, 3, 5, 16) 
print(totalDelPromedio) # 51.0