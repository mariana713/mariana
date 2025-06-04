#28demayoclase

def nombreDeFuncion(parametros,argumentos):
    print(parametros,argumentos)

nombreDeFuncion("esto es una funcion,",
                "esto es un argumento")


def ingresarNumero(mensaje):
    entrada = input(mensaje)
    esEntero = int(entrada)
    return esEntero

def sumaNumeros(numero1, numero2):
    suma = numero1 + numero2
    print("la suma de estos numeros da ",suma)
    return suma

def menor(numero1, numero2):
    menor = numero1 < numero2
    if menor:
        print(numero1, "es menor que", numero2)
    return menor

def mayor(numero1, numero2):
    mayor = numero1 > numero2
    if mayor:
        print(numero1, "es mayor que", numero2)
    return mayor

def igual(numero1, numero2):
    igual = numero1 == numero2
    if igual:
        print(numero1, "es igual a", numero2)
    return igual

def rango(start,stop,step):
    for i in range(start, stop, step):
        print(i, end=",")

def nombreDeFuncion(parametros,argumentos):
    numero1=ingresarNumero("ingrese un numero")
    numero2=ingresarNumero("ingrese otro numero")
    sumaNumeros(numero1, numero2)
    menor(numero1, numero2)
    mayor(numero1, numero2)
    igual(numero1, numero2)
    rango(1,100,2)
    print("")

    lista = [0,1,2,3,4,5,6,7]
    for elemento in lista[:]:
        lista[elemento]=elemento*2
        print(lista[elemento], end=",")
    print("")