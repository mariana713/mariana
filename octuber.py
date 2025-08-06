##clasede6deagosto
class Clase:
    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        return "El atributo es: " + self.atributo
    
    def imprimir(self):
        print("Imprimiendo: " + self.atributo )

instancia = Clase("valor")
print(instancia.metodo() )
instancia.imprimir() 



##ejercicio:crear una clase que sume dos numeros y los muestre por pantalla
class SumaNumeros:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        return self.numero1 + self.numero2
    
    def mostrar(self):
        print("La suma de", self.numero1, "y", self.numero2, "es:", self.sumar())