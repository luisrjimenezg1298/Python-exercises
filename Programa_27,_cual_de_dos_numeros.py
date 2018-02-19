print("Leer 2 números enteros y determinar cuál de los dos tiene mayor cantidad de dígitos")

numero1 = int(input("Ingresar un numero entero: "))
numero2 = int(input("Ingresar otro numero entero: "))
cantdig1 = 0
cantdig2 = 0
numthen1 = int(numero1)
numthen2 = int(numero2)

while numthen1 != 0 :
    numthen1 = int(numthen1 / 10)
    cantdig1 = cantdig1 + 1

while numthen2 != 0 :
    numthen2 = int(numthen2 / 10)
    cantdig2 = cantdig2 + 1

if cantdig1 > cantdig2 :
    print("El numero ",numero1,"tiene mayor cantidad de digitos que el numero ",numero2,".")

if cantdig2 > cantdig1 :
    print("El numero ",numero2,"tiene mayor cantidad de digitos que el numero ",numero1,".")

if cantdig1 == cantdig2 :
    print("El numero ",numero1,"tiene la misma cantidad de digitos que el numero ",numero2,".")

input("Fin")
    
