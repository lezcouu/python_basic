#Lista mutable
# numeros = [1,2,3,4,5,6]
#Agregamos info a la lista
numeros.append("HOLA")
#Quitamos info de la lista
numeros.pop(6)

#Tupla inmutable

mi_tupla = (1,2,3,4,5)
mi_tupla.append(5)
#Nos tirara un error que me dira q el numero esta repetido
mi_tupla.pop(2)
#Tirara un error porque la tupla no permite borrar
for numero in mi_tupla:
    print(numero)
#Nos mostrara los elementos

