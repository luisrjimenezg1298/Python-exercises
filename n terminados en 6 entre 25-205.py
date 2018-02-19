print("      Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205")

terminados = 0

print("Todos los numeros terminados en 6 comprendidos entre 25 y 205 son: ")

for terminados in range (25,205):
    if terminados % 10 == 6:
        print(terminados)

input("Fin")
