##clasedel13agosto
class Persona:
    def hablar(self):
        pass
class Padre(Persona):
    apellido=""
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return self.nombre+" "+self.apellido
    def hablar(self):
        print("hola soy", self.nombre, self.apellido)

class Hijo(Padre):
    def __init__(self, nombre, lenguajesDeProgramacion):
        super().__init__(nombre)
        self.lenguajesDeProgramacion = lenguajesDeProgramacion

class Hija(Padre):
    def __init__(self,nombre,artistaMusical):
        super().__init__(nombre)
        self.artistaMusical = artistaMusical
    def hablar(self):
        print("hola soy", self.nombre, self.apellido, "y mi musico favorito es", self.artistaMusical)

padre = Padre("nombre del padre")
Padre.apellido="apellido del padre"
hijo = Hijo("nombre del hijo","python")
hijo.hablar()
hija = Hija("nombre de la hija","artista favorito")
hija.hablar()

##Tarea: Crea una clase `Empleado` con atributos `nombre` y `salario`. Luego, define una subclase `Gerente` que herede de `Empleado` y añada un atributo `departamento`. Implementa un método `mostrar_informacion()` en ambas clases.
class Empleado:         
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        return f"El nombre del empleado es: {self.nombre}, y su salario es el siguiente: {self.salario}"
    
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
        
    def mostrar_informacion(self):
        return f"El nombre del gerente es: {self.nombre}, su salario es: {self.salario}, y su departamento es: {self.departamento}"
empleado = Empleado("Marcos", 20000)
print(empleado.mostrar_informacion())

gerente = Gerente("Pablo", 50000, "Recursos Humanos")
print(gerente.mostrar_informacion())