print("Mostrar en pantalla el promedio entero de los n primeros múltiplos de 3 para un número n leído")

n = int(input("Ingrese un numero: "))
promedio = 0
suma = 0
multiplos = 0

print("El promedio entero de los ",n," primeros multiplos de 3 es: ")

for multiplos in range (1,(n*3)+1):
    if multiplos % 3 == 0:
        suma = suma + multiplos
        promedio = suma / n
        promedio = int(promedio)
print(promedio)

input("Fin")

