import random

alumnos = []

def grabar_alumno():
    rut = input("Ingrese el Rut del alumno: ")
    #12345678-0
    while len(rut) != 10 or rut[9].lower() != 'k' and not rut[9].isdigit():
        rut = input("Rut inválido. Vuelva a ingresar el Rut del alumno: ")
    
    nombre = input("Ingrese el nombre del alumno: ")
    while len(nombre) < 2 or len(nombre) > 12:
        nombre = input("Nombre inválido. Vuelva a ingresar el nombre del alumno: ")
    
    apellido = input("Ingrese el apellido del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno: ")
    carrera = input("Ingrese la carrera del alumno: ")
    
    asignaturas = []
    cantidad_asignaturas = int(input("Ingrese la cantidad de asignaturas del alumno: "))
    for _ in range(cantidad_asignaturas):
        nombre_asignatura = input("Ingrese el nombre de la asignatura: ")
        promedio_asignatura = float(input("Ingrese el promedio de la asignatura: "))
        while promedio_asignatura < 1.0 or promedio_asignatura > 7.0:
            promedio_asignatura = float(input("Promedio inválido. Vuelva a ingresar el promedio de la asignatura: "))
        asignaturas.append({"nombre": nombre_asignatura, "promedio": promedio_asignatura})
    cert_notas = random.randint(1000, 5000)
    cert_regular = random.randint(1000, 5000)
    cert_mat = random.randint(1000, 5000)
    alumno = {"rut": rut, "nombre": nombre, "apellido": apellido, "fecha_nacimiento": fecha_nacimiento, "carrera": carrera, "asignaturas": asignaturas, "cert_notas": cert_notas, "cert_regular": cert_regular, "cert_mat": cert_mat}
    alumnos.append(alumno)
    print("Alumno registrado con éxito.")

def buscar_alumno():
    rut = input("Ingrese el Rut del alumno que desea buscar: ")
    for alumno in alumnos:
        if alumno["rut"] == rut:
            print("Información del alumno:")
            print(f"Rut: {alumno['rut']}")
            print(f"Nombre: {alumno['nombre']}")
            print(f"Apellido: {alumno['apellido']}")
            print(f"Fecha de Nacimiento: {alumno['fecha_nacimiento']}")
            print(f"Carrera: {alumno['carrera']}")
            print("Asignaturas:")
            for asignatura in alumno['asignaturas']:
                print(f"Nombre: {asignatura['nombre']}")
                print(f"Promedio: {asignatura['promedio']}")
            return
    
    print("Alumno no encontrado.")

def notas():
    rut = input("Ingrese el Rut del alumno que desea buscar: ")
    for alumno in alumnos:
        if alumno["rut"] == rut:
            print("Certificado de Notas:")
            print(f"Rut: {alumno['rut']}")
            print(f"Nombre: {alumno['nombre']}")
            print(f"Apellido: {alumno['apellido']}")
            print("Asignaturas:")
            for asignatura in alumno['asignaturas']:
                print(f"Nombre: {asignatura['nombre']}")
                print(f"Promedio: {asignatura['promedio']}")
            print(f"Valor Certificado: {alumno['cert_notas']}")
            return
    
def regular():
    rut = input("Ingrese el Rut del alumno que desea buscar: ")
    for alumno in alumnos:
        if alumno["rut"] == rut:
            print("Certificado de Alumno Regular:")
            print(f"Rut: {alumno['rut']}")
            print(f"Nombre: {alumno['nombre']}")
            print(f"Apellido: {alumno['apellido']}")
            print(f"Fecha de Nacimiento: {alumno['fecha_nacimiento']}")
            print(f"Carrera: {alumno['carrera']}")
            print(f"Valor Certificado: {alumno['cert_regular']}")
            return
    
    print("Alumno no encontrado.")

def mat():
    rut = input("Ingrese el Rut del alumno que desea buscar: ")
    for alumno in alumnos:
        if alumno["rut"] == rut:
            print("Certificado de Matricula:")
            print(f"Rut: {alumno['rut']}")
            print(f"Nombre: {alumno['nombre']}")
            print(f"Apellido: {alumno['apellido']}")
            print(f"Fecha de Nacimiento: {alumno['fecha_nacimiento']}")
            print(f"Carrera: {alumno['carrera']}")
            print(f"Valor Certificado: {alumno['cert_mat']}")
            return
    
    print("Alumno no encontrado.")
    
def imprimir_certificados():
    
    print("Menú Certificados:")
    print("1. Notas")
    print("2. Alumno Regular")
    print("3. Matricula")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        notas()
    elif opcion == "2":
        regular()
    elif opcion == "3":
        mat()
    elif opcion == "4":
        menu()
    else:
            print("Opción inválida. Intente nuevamente.")

def menu():
    while True:
        print("Menú:")
        print("1. Grabar alumno")
        print("2. Buscar alumno")
        print("3. Imprimir certificados")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            grabar_alumno()
        elif opcion == "2":
            buscar_alumno()
        elif opcion == "3":
            imprimir_certificados()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()