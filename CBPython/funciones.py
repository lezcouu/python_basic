##FUNCIONES PYTHON
# def imprimir_mensaje():
#    print("mensaje especial: ")
#    print("estoy aprendiendo a usar funciones!")
#
#imprimir_mensaje()
def conversacion(mensaje):
    print('Hola')
    print("¿Cómo estas?")
    print(mensaje)
    print("Adios")




opcion = int(input("Elige una opción(1, 2, 3): "))
if opcion == 1:
    conversacion("Elegiste la opción 1")
elif opcion == 2:
    conversacion("Elegiste la opción 2")
elif opcion == 3:
    conversacion("Elegiste la opción 3")
else:
    print("Elegiste una opción que no existé")
