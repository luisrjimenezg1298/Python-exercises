print("  Leer un número entero y determinar cuántas veces tiene el dígito 1")

numero = int(input("Ingresar un numero entero : "))
ultdig = 0
veces = 0

print("Las veces que el numero tiene el digito 1 son: ")

while numero != 0:
    ultdig = int(numero - int(numero / 10) * 10) 
    numero = int(numero / 10)
    if ultdig == 1:
        veces = int(veces + 1)
    
print(veces)

input("Fin")
