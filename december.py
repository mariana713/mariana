##clasedel20deagosto

import random

numero_azar = random.randint(-10,30)
print(numero_azar)

class Numerosalazar:
    def __init__(self, minimo, maximo):
        self.minimo= minimo
        self.maximo= maximo
        self.numero_al_azar=random.randint(self.minimo,self.maximo)
    def mostrar_numero(self):
        print(self.numero_al_azar)

instancia=Numerosalazar(-10,900)
instancia.mostrar_numero()



class Persona:
    def __init__(self, nombre):
        self.nombre=nombre
class Alumno(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
class Profesor(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
class Clase:
    def __init__(self, materia, grado, division,profesor):
        self.materia=materia
        self.grado=grado
        self.division=division
        self.alumnos=[]
        self.profesor=profesor
    def agregar_alumno(self,nombre):
        alumno=Alumno(nombre)
        self.alumno.append(alumno)
    def llenar_clase(self,nombres_de_alumnos):
        for nombre in nombres_de_alumnos:
            alumno=Alumno(nombre)
            self.agregar_alumno(alumno)

Gabriel=Profesor("Gabriel")
nombres_de_alumno=["Dania","Anghely","Belen","Mariana","Abigail"]
tic5to1ra = Clase("Tecnologia",5,1,Gabriel)
tic5to1ra.llenar_clase(nombres_de_alumno)


