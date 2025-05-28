##consigna21/mayo

import random
adivinar = random.randint(0, 100)
noAdivinar = True

def rangoCorrecto(numeroc):
    minimo=0
    maximo=100
    return minimo<numeroc or numeroc>maximo

while noAdivinar:
    numeroc=int(input("ingrese un numero entre 0 y 100: "))
    if not rangoCorrecto(numeroc):
        print("incorrecto, tiene que ingresar un numero entre 0 y 100")
        continue
    if numeroc < adivinar:
        print("el numero que tiene que adivinar en mayor")
    if numeroc > adivinar:
        print("el numero que tiene que adivinar es menor")
    if numeroc == adivinar:
        print("muy bien, adivinaste el numero")
        noAdivinar = False