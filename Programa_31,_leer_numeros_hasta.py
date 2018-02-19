print("Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5")

numeros = int(input("Digite numeros enteros y finalice con 0: "))
suma = 0
cantidad = 0
ultdig = 0

while numeros != 0:
    ultdig = int(numeros - int(numeros / 10)*10)
    if ultdig == 5 :
        suma = suma + numeros
        cantidad = cantidad + 1
    numeros = int(input())

promedio = suma / cantidad
print ("El promedio de los números terminados en 5 es: ",promedio)

input("Fin")
    
