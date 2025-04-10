class Alumno:
    def __init__(self, nombre, apellido, curso, edad):
        self.nombre = nombre.strip().capitalize()
        self.apellido = apellido.strip().capitalize()
        self.curso = curso.strip().capitalize()
        self.edad = int(edad)
    
    def programar(self, ):
        print(f"el alumno {self.nombre} esta programando")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
curso = input("Ingrese a qué curso va: ")
edad = input("Ingrese su edad: ")

# Instanciación del objeto Alumno
alumno1 = Alumno(nombre, apellido, curso, edad)
alumno1.programar()
