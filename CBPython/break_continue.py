def run():
    # for contador in range(1,11):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
    # for i in range(1,10):
    #     print(i)
    #     if i == 8:
    #         break
    texto = input("Ingresa tu texto: ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)


if __name__ == "__main__":
    run()