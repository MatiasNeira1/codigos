import os
import time
os.system("cls")

def menu_calculadora():
    menu=True
    while menu:
        print("CALCULADORA")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        opcion_usuario=0
        try:
            opcion_usuario=int(input("Ingresa una de las opciones: "))

        except:
            print("La opcion debe ser numerica")

        if opcion_usuario < 1 or opcion_usuario >3:
            input("La opcion ingresada no es valida, presione enter para continuar")
            
        else:
            return opcion_usuario
#input(f"La opcion elegida es: {menu_calculadora()}")
#input(f"La otra opcion elegida es: {menu_calculadora()}")

os.system("cls")
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2


def acciones(var_elegida):
    if var_elegida==1:
        numero_1=int(input("Ingresa el primer numero: "))
        numero_2=int(input("Ingresa el segundo numero: "))
        input(f"La suma de los dos numeros es {suma(numero_1,numero_2) }")

    elif var_elegida==2:
        numero_1=int(input("Ingrese el primer numero: "))
        numero_2=int(input("Ingrese el segundo numero: "))
        input(f"La resta de los dos numeros es {resta(numero_1,numero_2) }")

    elif var_elegida==3:
        numero_1=int(input("Ingresa el primer numero: "))
        numero_2=int(input("Ingresa el segundo numero: "))
        input(f"La multiplicacion de los dos numeros es {multiplicacion(numero_1, numero_2)}")

    

acciones(menu_calculadora())
            


