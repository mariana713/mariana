##clase 11/06
from datetime import datetime, date
objeto = {
    "nombre": "Mariana",
    "edad": 17,
    "ciudad": "Buenos Aires",

}     
objeto["nacimiento"]=date(2007, 6, 5)
hoy = date(2025, 6, 11)
objeto["edad"] = hoy.year - objeto["nacimiento"].year
print("hola",objeto["nombre"])

def naciohoy(fechaDeHoy, fechaDeNacimiento):
   mismoMes = fechaDeHoy.month == fechaDeNacimiento.month
   mismoDia = fechaDeHoy.day == fechaDeNacimiento.day
   return mismoMes and mismoDia


objeto2 = dict(nombre = "Rodolfo",
               edad = 2,
               ciudad = "Moscu",
               nacimiento = date(2005, 10, 30))
listadeDiccionarios = [
   objeto,
   objeto2,
    {
        "nombre": "Sara",
        "edad":88,
        "ciudad": "buenos aires",
        "nacimiento": date(2001, 7, 10),
        "hijos": (objeto, objeto2)
    }
          
]
print("quien es el primer elemento?",
      listadeDiccionarios[0]["nombre"])
   