print("ingrese un numero")
primernumero=int(input())
segundonumero=int(input("ingrese otro numero:  "))
suma=(primernumero+segundonumero)
print("la suma de estos numeros da", suma)
menor= primernumero < segundonumero
mayor= primernumero > segundonumero
igual= primernumero==segundonumero
if mayor:
    print("el primernumero es mayor que segundonumero")
if igual:
    print("el primernumero es igual a segundonumero")
if menor:
    print("el primernumero es menor que segundonumero")
