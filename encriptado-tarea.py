


# ENCRIPTADOR DE FRASES


choose_characters = input("Ingresa el caracter con el cual quieres encriptar: ")


def encriptar(frase, caracter):
    encriptada = ""
    for letra in frase:
        if letra.lower() in "aeiouáéíóú":
            if letra.isupper():
                encriptada = encriptada + choose_characters.upper()
            else:
                encriptada = encriptada + choose_characters
        else:
            encriptada = encriptada + letra
    return encriptada


while True:
    print(encriptar(input("Ingresa una frase:\n>"), choose_characters))

    print("\nIngresa:\n(1) para encriptar otra frase")
    print("(2) para finalizar")
    opcion = input(">")
    if opcion == "2":
        print("HASTA LUEGO!!!")
        break
    if opcion == "1":
        print("----O----\n")




	





















