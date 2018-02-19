print("    Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído")

numero = int(input("Ingrese un numero entero: "))
multiplos = 0

print("Los multiplos de 5 comprendidos entre 1 y ",numero," son: ")

for multiplos in range (1, numero):
    if multiplos % 5 == 0:
        print(multiplos)

input("Fin")

