

def main():
    cadena = "Practica els problemes de list comprehensions per a ser més Pythonic!"

    nom = [i if i < 5 else 0 for i in cadena]

    print(nom)

if __name__ == '__main__':
    main()