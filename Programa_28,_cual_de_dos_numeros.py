print("Leer 2 números enteros y determinar cual de los dos tiene mayor cantidad de dígitos primos")

numero1 = int(input("Ingresar un numero entero: "))
numero2 = int(input("Ingresar otro numero entero: "))
ultdig1 = 0
ultdig2 = 0
numthen1 = int(numero1)
numthen2 = int(numero2)
primos1 = 0
primos2 = 0

while numthen1 != 0 :
    ultdig1 =  int(numthen1 - int(numthen1 / 10) * 10)
    numthen1 = int(numthen1 / 10)
    if ultdig1 == 1 or ultdig1 == 2 or ultdig1 == 3 or ultdig1 == 5 or ultdig1 == 7:
        primos1 = int(primos1 + 1)

while numthen2 != 0 :
    ultdig2 =  int(numthen2 - int(numthen2 / 10) * 10)
    numthen2 = int(numthen2 / 10)
    if ultdig2 == 1 or ultdig2 == 2 or ultdig2 == 3 or ultdig2 == 5 or ultdig2 == 7:
        primos2 = int(primos2 + 1)

if primos1 > primos2 :
    print("El numero ",numero1,"tiene mayor cantidad de digitos primos que el numero ",numero2,".")

if primos2 > primos1 :
    print("El numero ",numero2,"tiene mayor cantidad de digitos primos que el numero ",numero1,".")

if primos1 == primos2 :
    print("El numero ",numero1,"tiene la misma cantidad de digitos primos que el numero ",numero2,".")

input("Fin")

