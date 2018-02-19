print("Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído")

numero = int(input("Ingrese un numero entero: "))
total = 0

print("La suma de todos los enteros comprendidos entre 1 y ",numero," es igual al ultimo de los numeros que se presentan a continuacion: ")

for suma in range (1,numero):
    total = suma + total

print(total)

input("Fin")


