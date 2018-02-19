print("Mostrar en pantalla los primeros 20 múltiplos de 3")

multiplos = 0

print("Los primeros 20 multiplos de 3 son: ")

for multiplos in range (1, 61):
    if multiplos % 3 == 0:
        print(multiplos)

input("Fin")
