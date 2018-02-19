print("Leer dos números entero y mostrar todos los múltiplos de 5 comprendidos entre el menor y el mayor")

numero1 = int(input("Ingresar un numero: "))
numero2 = int(input("Ingresar otro numero: "))
multiplos = 0
multiplos2 = 0


if numero1 < numero2:
    print("Todos los múltiplos de 5 comprendidos entre el ",numero1," y ",numero2,"son: ")
    for multiplos in range (numero1+1,numero2):
        if multiplos % 5 == 0:
            print(multiplos)

if numero2 < numero1:
    print("Todos los múltiplos de 5 comprendidos entre el ",numero2," y el ",numero1,"son: ")
    for multiplos2 in range (numero2+1,numero1):
        if multiplos2 % 5 == 0:
            print(multiplos2)

input("Fin")
