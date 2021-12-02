
#ACTIVITAT QUE DEMANA NOM COGNOM I 2N COGNOM I MOSTRI EL CODI
def main():

    nom = input("Introdueix el teu nom: ")
    cognom1 = input("Introdueix el primer cognom: ")
    cognom2 = input("Introdueix el segon cognom: ")

    print("********************************")

    print("El teu codi és:", cognom1[:2], end="")
    print(cognom2[:2], end="")
    print(nom[:2], end="")

if __name__ == '__main__':
    main()