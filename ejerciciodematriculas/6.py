class registrar:
    def __init__(self, nombre, edad, telefono, usuario, contrasena):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.usuario = usuario
        self.contrasena = contrasena


class Instructor:
    def __init__(self, nombre, credenciales):
        self.nombre = nombre
        self.credenciales = credenciales

class Transaccion:
    def __init__(self, estudiante, cantidad, fecha, detalles):
        self.estudiante = estudiante
        self.cantidad = cantidad
        self.fecha = fecha
        self.detalles = detalles

class Estudiante:
    def __init__(self, nombre, edad, telefono, curso):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.curso = curso

class Materia:
    def __init__(self, nombre, descripcion, cronograma, instructor):
        self.nombre = nombre
        self.descripcion = descripcion
        self.cronograma = cronograma
        self.instructor = instructor

class Curso:
    def __init__(self, descripcion, fecha, nivel, materia):
        self.descripcion = descripcion
        self.fecha = fecha
        self.nivel = nivel
        self.materia = materia

class Inscripcion:
    def __init__(self, estudiante, curso):
        self.estudiante = estudiante
        self.curso = curso

class Sistema:
    def __init__(self):
        self.usuario = []
        self.instructores = []
        self.transacciones = []
        self.estudiantes = []
        self.materias = []
        self.cursos = []
        self.inscripciones = []

    def registrar_usuario(self, nombre, edad, telefono, usuario, contrasena):
        nuevo_usuario = registrar(nombre, edad, telefono, usuario, contrasena)
        self.usuarios.append(nuevo_usuario)

    def agregar_instructor(self, nombre, credenciales):
        nuevo_instructor = Instructor(nombre, credenciales)
        self.instructores.append(nuevo_instructor)

    def crear_transaccion(self, estudiante, cantidad, fecha, detalles):
        nueva_transaccion = Transaccion(estudiante, cantidad, fecha, detalles)
        self.transacciones.append(nueva_transaccion)

    def agregar_estudiante(self, nombre, edad, telefono, curso):
        nuevo_estudiante = Estudiante(nombre, edad, telefono, curso)
        self.estudiantes.append(nuevo_estudiante)

    def crear_materia(self, nombre, descripcion, cronograma, instructor):
        nueva_materia = Materia(nombre, descripcion, cronograma, instructor)
        self.materias.append(nueva_materia)

    def crear_curso(self, descripcion, fecha, nivel, materia):
        nuevo_curso = Curso(descripcion, fecha, nivel, materia)
        self.cursos.append(nuevo_curso)

    def crear_inscripcion(self, estudiante, curso):
        nueva_inscripcion = Inscripcion(estudiante, curso)
        self.inscripciones.append(nueva_inscripcion)

usuario1 = registrar("Juan Perez", 25, 123456789, "juan123", "contraseña123")
"""
instructor1 = Instructor("Pedro Rodriguez", "Licenciatura en Educación")

transaccion1 = Transaccion("Juan Perez", 50, "2022-01-01", "Pago de inscripción")


estudiante1 = Estudiante("Maria Garcia", 20, "987654321", "Introducción a la programación")


materia1 = Materia("Programación Orientada a Objetos", "Aprende a programar en POO", "Lunes a Viernes, 9am a 12pm", instructor1)


curso1 = Curso("Introducción a la programación en Python", "2022-03-15", "Básico", materia1)


inscripcion1 = Inscripcion(estudiante1, curso1)

print("Nombre: ", usuario1.nombre)
print("Edad: ", usuario1.edad)
print("Teléfono: ", usuario1.telefono)
print("Usuario: ", usuario1.usuario)
print("Contraseña: ", usuario1.contrasena)

print("Nombre: ", instructor1.nombre)
print("Credenciales: ", instructor1.credenciales)


print("Estudiante: ", transaccion1.estudiante)
print("Cantidad: ", transaccion1.cantidad)
print("Fecha: ", transaccion1.fecha)
print("Detalles: ", transaccion1.detalles)


print("Nombre: ", estudiante1.nombre)
print("Edad: ", estudiante1.edad)
print("Teléfono: ", estudiante1.telefono)
print("Curso: ", estudiante1.curso)


print("Nombre: ", materia1.nombre)
print("Descripción: ", materia1.descripcion)
print("Cronograma: ", materia1.cronograma)
print("Instructor: ", materia1.instructor.nombre)


print("Descripción: ", curso1.descripcion)
print("Fecha: ", curso1.fecha)
print("Nivel: ", curso1.nivel)
print("Materia: ", curso1.materia.nombre)


print("Estudiante: ", inscripcion1.estudiante.nombre)
print("Curso: ", inscripcion1.curso.descripcion)

"""



def menu_principal():
    sistema = Sistema()
    while True:
        print("Seleccione una opción:")
        print("1. Registrar usuario")
        print("2. Agregar instructor")
        print("3. Crear transacción")
        print("4. Agregar estudiante")
        print("5. Crear materia")
        print("6. Crear curso")
        print("7. Crear inscripción")
        print("0. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            telefono = input("Teléfono: ")
            usuario = input("Usuario: ")
            contrasena = input("Contraseña: ")
            sistema.registrar_usuario(nombre, edad, telefono, usuario, contrasena)
        elif opcion == "2":
            nombre = input("Nombre: ")
            credenciales = input("Credenciales: ")
            sistema.agregar_instructor(nombre, credenciales)
        elif opcion == "3":
            estudiante = input("Estudiante: ")
            cantidad = float(input("Cantidad: "))
            fecha = input("Fecha: ")
            detalles = input("Detalles: ")
            sistema.crear_transaccion(estudiante, cantidad, fecha, detalles)
        elif opcion == "4":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            telefono = input("Teléfono: ")
            curso = input("Curso: ")
            sistema.agregar_estudiante(nombre, edad, telefono, curso)
        elif opcion == "5":
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            cronograma = input("Cronograma: ")
            instructor = input("Instructor: ")
            sistema.crear_materia(nombre, descripcion, cronograma, instructor)
        elif opcion == "6":
            descripcion = input("Descripción: ")
            fecha = input("Fecha: ")
            nivel = input("Nivel: ")
            materia = input("Materia: ")
            sistema.crear_curso(descripcion, fecha, nivel, materia)
        elif opcion == "7":
            estudiante = input("Estudiante: ")
            curso = input("Curso: ")
            sistema.crear_inscripcion(estudiante, curso)
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")
menu_principal()

print("Nombre: ", usuario1.nombre)
print("Edad: ", usuario1.edad)
print("Teléfono: ", usuario1.telefono)
print("Usuario: ", usuario1.usuario)
print("Contraseña: ", usuario1.contrasena)