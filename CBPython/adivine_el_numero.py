import random


def run():
    number_random = random.randint(1, 100)
    number_select = int(input("Escribe un número del 1 al 100: "))
    while number_select != number_random:
        if number_select < number_random:
            print("Dejame ver... mmm no, es mas grande")
        else:
            print("Dejame ver... mmm no, es mas pequeño")
        number_select = int(input("Escribe otro número: "))
    print("¡Ganaste!")


if __name__ == "__main__":
    run()