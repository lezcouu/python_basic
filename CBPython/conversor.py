def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Quieres saber cuantos dolares tienes?, ingresa la cantidad de pesos " + tipo_pesos + " que tienes $:")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $"+ dolares + " dolares" )

menu = """
Bienvendio al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 153)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Ingresa una opción correcta por favor")
#elif opcion == 2:
#    pesos = input("¿Quieres saber cuantos dolares tienes?, ingresa la cantidad de pesos que tienes $")
#    pesos = float(pesos)
#    valor_dolar = 158
#    dolares = pesos / valor_dolar
#    dolares = round(dolares, 2)
#    dolares = str(dolares)
#    print("tienes $"+ dolares + " dolares" )
#elif opcion ==3:
#    pesos = input("¿Quieres saber cuantos dolares tienes?, ingresa la cantidad de pesos que tienes $")
#    pesos = float(pesos)
#    valor_dolar = 24
#    dolares = pesos / valor_dolar
#    dolares = round(dolares, 2)
#    dolares = str(dolares)
#    print("tienes $"+ dolares + " dolares" )
#else:
#    print('ingresa una opción correcta')

#def suma(a,b):
#    print("Se suman dos números")
#    resultado = a + b
#    return resultado
#
#sumatoria = suma(1,4)
#
#print(sumatoria)