print("Utilizando ciclos anidados generar las siguientes parejas de números")
ciclo1 = 0
ciclo2 = 0
cond = 0

while ciclo1 <= 7:
    ciclo1 = ciclo1 + 1
    print(ciclo1)   

while cond <= 4:
    for ciclo2 in range (1,2+1):
        cond = cond + 1
    print(ciclo2)

input("Fin")
