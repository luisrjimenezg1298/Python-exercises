print("Leer un número entero y mostrar todos sus componentes numéricos o sea aquellos para quienes el sea un múltiplo")

numero = int(input("Ingrese un numero entero: "))
multiplo = 0

for multiplo in range (1,numero+1):
    if numero % multiplo == 0:
        print(multiplo)

input("\nFin")
