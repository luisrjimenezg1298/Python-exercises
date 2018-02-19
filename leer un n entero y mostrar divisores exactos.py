print("Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído")

numero = int(input("Ingresa un numero entero: "))
divisores = 0

print("Todos los divisores exactos del numero ",numero,"comprendidos entre 1 y ",numero," son: ")

for divisores in range (1,numero):
    if numero % divisores == 0:
        print(divisores)
input("Fin")

