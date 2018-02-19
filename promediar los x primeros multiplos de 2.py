print("Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos")

x = int(input("Ingrese un numero para los primeros multiplos de 2: "))
y = int(input("Ingrese un numero para los primeros multiplos de 5: "))
promedio = 0
suma = 0
multiplos = 0
promedio2 = 0
suma2 = 0
multiplos2 = 0

for multiplos in range (1,(x*2)+1):
    if multiplos % 2 == 0:
        suma = suma + multiplos
        promedio = suma / x
        promedio = int(promedio)

for multiplos2 in range (1,(y*5)+1):
    if multiplos2 % 5 == 0:
        suma2 = suma2 + multiplos2
        promedio2 = suma2 / x
        promedio2 = int(promedio2)

if promedio > promedio2:
    print("El promedio de los ",x," primeros multiplos de 2 es mayor que el promedio de los ",y," primeros multiplos de 5.")

else:
    print("El promedio de los ",x," primeros multiplos de 2 es menor que el promedio de los ",y," primeros multiplos de 5.")

input("Fin")
