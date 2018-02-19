print("Generar todas las tablas de multiplicar del 1 al 10")

for mult1 in range (1,11):
    for mult2 in range (1,11):
        producto = mult1 * mult2
        print(mult1, "*",mult2," = ",producto)

input("Fin")
