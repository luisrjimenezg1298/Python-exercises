print("Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído")

numero = int(input("Ingrese un numero entero: "))
pares=0

print("Todos los pares comprendidos entre 1 y ",numero," son:")

for pares in range (2,numero,2):
    print(pares)

input("Fin")
             
             
