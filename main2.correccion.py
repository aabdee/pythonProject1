
#CORRECCIÓN EJERCICIO DE MOSTRAR TABLA CON CODIGOS I DATOS INDTRODUCIDOS

def main():

    usuaris = int(input("Quants usuaris vols introduir? "))
    i = 0
    while i < usuaris:
        nom = input("Introdueix el teu nom: ")
        cognom1 = input("Introdueix el primer cognom: ")
        cognom2 = input("Introdueix el segon cognom: ")
        telefon = int(input("Introdueix el telèfon: "))
        edat = int(input("Introdueix l'edat: "))
        contacte = bool(input("Contacte (T / F): "))

    i+=1

    print("******")

    codi = cognom2[:2] + cognom1[:2] + nom[:2]
    print("______________________________________")
    print("|Codi|","|Edat|","|  Telefon  |","|Contacte|")
    print("**************************************")

    print(codi, "\t", edat,"\t", telefon, "\t", contacte, "\t")

    print("______________________________________")

if __name__ == '__main__':
    main()