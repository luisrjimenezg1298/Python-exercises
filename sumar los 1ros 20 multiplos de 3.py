print("Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3")

total = 0
multiplos = 0

print("La suma de los primeros 20 multiplos de 3 son: ")

for multiplos in range (1,(20*3)+1):
    if multiplos % 3 == 0:
        total = total + multiplos

print(total)

input("Fin")
