print("Leer un número y calcularle su factorial")

numero = int(input("Ingrese un numero entero positivo: "))
facto = 1

if numero < 0:
    print("El factorial no esta definido para numeros negativos.")

for cont in range (1,numero+1):
    facto = facto * cont

print("El factorial de ",numero," es ",facto)
