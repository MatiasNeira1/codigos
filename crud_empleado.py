import os
import json

os.system("cls")
URL_EMPLEADOS = "empleados.json"


def cargar_json(url_archivo):
    try:
        with open(url_archivo, "r") as archivo:
            return json.load(archivo)
    except:
        return []


def guardar_archivo(url_archivo, data):
    with open(url_archivo, "w") as archivo:
        json.dump(data, archivo, indent=4)


def crear_empleado():
    empleados = cargar_json(URL_EMPLEADOS)

    id_empleado = input("Ingrese Id de empleado:")
    nombre = input("Ingrese nombre de empleado: ")
    apellido = input("Ingrese apellido de empleado: ")
    try:
        sueldo = int(input("Ingrese sueldo del empleado: "))
    except:
        sueldo = 0
    id_cargo = input("Ingrese el ID del cargo: ")

    nuevo_empleado = {
        "id_empleado": id_empleado,
        "nombre": nombre,
        "apellido": apellido,
        "sueldo": sueldo,
        "id_cargo": id_cargo,
    }

    empleados.append(nuevo_empleado)
    guardar_archivo(URL_EMPLEADOS, empleados)


def actualizar_empleado():
    empleados = cargar_json(URL_EMPLEADOS)

    id_empleado_cambio = input("Ingrese la ID del empleado que quiera cambiar: ")
    nombre_cambio = input("Ingrese nombre de empleado que quiera cambiar: ")
    apellido_cambio = input("Ingrese apellido de empleado que quiera cambiar: ")
    try:
        sueldo_cambio = int(input("Ingrese el nuevo sueldo: "))
    except:
        sueldo_cambio = 0

    id_cargo_cambio = input("Ingrese el ID al cargo que quiere asignar: ")

    for emp in empleados:
        if emp["id_empleado"] == id_empleado_cambio:
            emp["nombre"] = nombre_cambio
            emp["apellido"] = apellido_cambio
            emp["sueldo"] = sueldo_cambio
            emp["id_cargo"] = id_cargo_cambio
            break

    guardar_archivo(URL_EMPLEADOS, empleados)


def eliminar_empleado():
    empleados = cargar_json(URL_EMPLEADOS)

    id_empleado_cambio = input("Ingrese la ID del empleado que quiera eliminar: ")

    empleados_agregados = []

    for emp in empleados:
        if emp["id_empleado"] != id_empleado_cambio:
            empleados_agregados.append(emp)

    guardar_archivo(URL_EMPLEADOS, empleados_agregados)


def menu_general():
    os.system("cls")
    print("1. Crear empleado")
    print("2. Actualizar empleado")
    print("3. Eliminar empleado")
    print("4. Listar empleado")
    print("5. Salir")


def seleccionar_opcion(max_opcion):
    opcion = 0
    while True:
        try:
            opcion = int(input("Seleccione una opción >> "))
        except:
            pass
        if opcion < 1 or opcion > max_opcion:
            input("Opción invalida intente nuevamente >> ")
        else:
            return opcion


def iniciar_programa():
    while True:
        menu_general()
        opcion = seleccionar_opcion(5)

        if opcion == 1:
            crear_empleado()
        elif opcion == 2:
            actualizar_empleado()
        elif opcion == 3:
            eliminar_empleado()
        elif opcion == 4:
            empleados = cargar_json("empleados.json")
            print(empleados)
        elif opcion == 5:
            return

        input()


iniciar_programa()
