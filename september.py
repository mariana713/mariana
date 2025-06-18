##clase 18/06
def pedir_confirmacion(prompt,reintentos=4, queja="Si o no, por favor!"):
    while True:
        ok = input(prompt)
        if ok in("s", "S", "si", "SI"):
            return True
        if ok in("n", "no", "No", "NO"):
            return False
        reintentos = reintentos -1
        if reintentos < 0:
            raise OSError("usuario duro")
        print(queja)
##esta funcion puede ser llamada de distintas maneras:
#-pasando solo el argumento obligatorio:
pedir_confirmacion("¿Realmente quieres salir?")
#-pasando uno de los argumentos opcionales:
pedir_confirmacion("¿sobreescribir archivo?", 2)
pedir_confirmacion("¿hacen silencio?", 5,"")
