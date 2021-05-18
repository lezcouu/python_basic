import random


def generator_password():
    mayus =  ["A", "B", "C", "D", "E", "F", "G"]
    minusc = ["a", "b", "c", "d", "e", "f", "g"]
    symbol = ["!", "#", "$", "(", ")", "%", "/"]
    number = ["1", "2", "3", "4", "5", "6", "7"]

    character = mayus + minusc + symbol + number

    password = []

    for i in range(15):
        character_random = random.choice(character)
        password.append(character_random)


    password = "".join(password)
    return password


def run():
    password = generator_password()
    print("Tu nueva contraseña es: " + password)


if __name__ == "__main__":
    run()