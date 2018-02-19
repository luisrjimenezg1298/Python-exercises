print("Leer números hasta que digiten 0 y determinar a cuanto es igual el promedio entero de los número primos leídos")

numero = int(input("Digite numeros enteros y finalice con 0: "))
suma = 0
cantidad = 0
numeros = 0

while numero != 0:
    for numeros in range (2,numero):
        if numeros == 2:
            suma = suma + numeros
            cantidad = cantidad + 1
        if numero == 1:
            suma = suma + numeros
            cantidad = cantidad + 1
        if ((numero / numeros) != 0):
            suma = suma + numeros
            cantidad = cantidad + 1
    numero = int(input())

promedio = int(suma / cantidad)

print("el promedio entero de los número primos leídos es igual: ",promedio)

input("Fin")
            
