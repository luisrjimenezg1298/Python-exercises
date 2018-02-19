print("Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos")

numero = input("Ingrese un numero entero de tres digitos: ")
lista = list(map(int,numero))
dig1 = lista[0]
dig2 = lista[1]
dig3 = lista[2]
todos1 = 0
todos2 = 0
todos3 = 0

print("Los enteros comprendidos entre 1 y",dig1,"son: ")
for todos1 in range(1+1,dig1):
    print(todos1)
        
print("Los enteros comprendidos entre 1 y",dig2,"son: ")
for todos2 in range(1+1,dig2):
    print(todos2)

print("Los enteros comprendidos entre 1 y",dig3,"son: ")
for todos3 in range(1+1,dig3):
    print(todos3)

input("Fin")

    
