a = 4
b = 2

if b != 0: # Si 2 es distinto a 4 entonces va a dividir 4/2
    print(a/b) # 2.0

if b != 0:
    c = a/b # 2.0
    d = c + 1 # 3.0
    print(d)


a = 10

if a > 5 and a < 15:
    print('Mayor que 5 y menor que 15')


x = 5

if x == 9:
    print('Es 5')
elif x == 6:
    print('Es 6')
elif x == 7:
    print('Es 7')
else:
    print('No cumple con ninguna de las condiciones')


# Operador ternario
x = 10
print('Es 10' if x == 10 else "No es 10")
# [código si se cumple] if [condición] else [código si no se cumple]

a = 10
b = 5
c = a/b if b!= 0 else -1
print(c)

# Verifica si un número es par o impar
x = 6
if x % 2 == 0:
    print('Es par')
else:
    print('Es impar')

# Decrementa x en 1 unidad si es mayor que cero
x = 5
x -= 1 if x > 0 else 0
print(x)


# Creamos una funcion donde vamos a ver los rangos de nota de cada alumno.
# Al llamar a la funcion colocamos un numero dentro del rango de nota para saber
# en cual rango de nota esta el estudiante.
def rangoNota(nota):
    if nota >= 90 and nota <= 100:
        print('(A) -> Nota excelente')
        return nota
    elif nota >= 80 and nota <= 89:
        print('(B) -> Nota muy buena')
        return nota
    elif nota >= 70 and nota <= 79:
        print('(C) -> Nota buena')
        return nota
    elif nota >= 60 and nota <= 69:
        print('(D) -> Nota deficiente')
        return nota
    else:
        print('Nota insuficiente para aplicar a un rango de nota')
        return nota
        
    
calificacion = rangoNota(80)
print(calificacion)

calificacion = rangoNota(90)

calificacion = rangoNota(50)
print(calificacion)

