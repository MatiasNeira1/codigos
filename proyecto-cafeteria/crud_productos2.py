import os
import csv
os.system("cls")

DIR_PRODUCTOS = 'productos.csv'
FIELDNAMES_PRODUCTOS = ['id_producto', 'nombre_producto', 'precio', 'stock']

def leer_archivo_csv(dir):
    try:
        with open(dir, mode='r', newline='', encoding='utf-8') as archivo:
            data = csv.DictReader(archivo)
            return list(data)
    except:
        return []

def guardar_archivo_csv(dir, data, fieldnames):
    try:
        with open(dir, mode='w', newline='', encoding='utf-8') as archivo:
            data_csv = csv.DictWriter(archivo, fieldnames=fieldnames)
            data_csv.writeheader()
            data_csv.writerows(data)
    except:
        return []


def crear_productos():
    productos=leer_archivo_csv(DIR_PRODUCTOS)
    


    id_producto=input("Ingresar ID del nuevo producto: ")
    nombre_producto=input("Ingresar nombre del nuevo producto: ")
    try:
        precio=int(input("Ingresar el precio del producto nuevo: "))
    except:
        precio=0
    try:
        stock=int(input("Ingresar stock del producto nuevo: "))
    except:
        stock=0
    

    producto_nuevo={

        "id_producto": id_producto,
        "nombre_producto": nombre_producto,
        "precio": precio,
        "stock": stock


    }

    productos.append(producto_nuevo)

    guardar_archivo_csv(DIR_PRODUCTOS, productos, FIELDNAMES_PRODUCTOS)


def actualizar_producto():
    productos=leer_archivo_csv(DIR_PRODUCTOS)


    id_producto=input("Ingresar ID del producto a editar: ")
    nombre_producto=input("Ingresar nombre del producto a editar: ")
    
    precio=int(input("Ingresar el precio del producto a actualizar: "))
    stock=int(input("Ingresar stock del producto a actualizar: "))

    for datos in productos:
        if id_producto=="id_producto":
            datos["id_producto"]=id_producto,
            datos["nombre"]=nombre_producto,
            datos["precio"]=precio,
            datos["stock"]=stock
            break
    guardar_archivo_csv(DIR_PRODUCTOS,productos, FIELDNAMES_PRODUCTOS)
    


def menu_general():
    os.system("cls")
    print("== PRODUCTOS ==")
    print("1. Crear         - Create")
    print("2. Actualizar    - Update")
    print("3. Listar        - Read")
    print("4. Borrar        - Delete")
    print("5. Salir")
    
def seleccionar_opcion(max_value):
    opcion = 0
    while True:
        try:
            opcion = int(input("Ingrese una opción >> "))
        except:
            pass
        if opcion < 1 or opcion > max_value:
            input("Opción inválida, intente nuevamente >> ")
        else:
            return opcion

def iniciar_programa():
    while True:
        menu_general()
        opcion = seleccionar_opcion(5)
        
        if opcion == 1:
            crear_productos()
        elif opcion == 2:
            print("a")
        elif opcion == 3:
            print("a")
        elif opcion == 4:
            print("Borrar")
        elif opcion == 5:
            return
        input()

if __name__ == "__main__":
    iniciar_programa()
