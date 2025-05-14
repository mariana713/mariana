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

##lista
lista = [0,1,2,3,4,5,6,7]
for elemento in lista[:]:
    lista[elemento]=elemento*2
    print(lista[elemento],end=",")
print("")

for x in range(10):
    print(x)

for x in range(1,7,2):
    print(lista[x])