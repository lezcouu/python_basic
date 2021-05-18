def run():
    mi_diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }
    # print(mi_diccionario["llave1"])
    # print(mi_diccionario["llave2"])
    # print(mi_diccionario["llave3"])
    poblacion_paises = {
        "Argentina" :50000000,
        "Brasil" : 300000000,
        "Colombia" : 60000000
    }
    for pais, poblacion in poblacion_paises.items():
        print("En " + pais + " hay " + str(poblacion) + " habitantes.")

if __name__ == "__main__":
    run()