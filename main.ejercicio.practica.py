
#guardar numeros parejos de una lista en otra lista.

#pedir a alguien el ejemplo de raquel de la pizarra.

def main():

    llista = list()

    for x in range(10):
        llista.append(x*x)


if __name__ == '__main__':
    main()


def main():

    numbers = [0,2,4,6,8]

    numbers2 = [x+3 for x in numbers]

    print(numbers)
    print(numbers2)

if __name__ == '__main__':
    main()


def main():

    text = "Practica els problemes de list comprehensions per a ser més Pythonic!"

    espai = [i for i in text if i in ' ']

    print(len(espai))

if __name__ == '__main__':
    main()


def main():
    text = "Practica els problemes de list comprehensions per a ser més Pythonic!"

    consonants = [i for i in text.split() if len(i) < 6]
    print(consonants)

if __name__ == '__main__':
    main()

