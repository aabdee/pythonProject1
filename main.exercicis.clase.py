
# ejercicio 1 practica 10
def main():

    n1 = int(input("Introdueix el primer nombre enter: "))
    n2 = int(input("Introdueix el segon nombre enter: "))

    if n1 < n2:
        while n1 < n2+1:
            print(n1)
            n1+=1
    else:
        while n1 > n2:
            print("Error")
            n1 = int(input("Introdueix el primer nombre enter: "))
            n2 = int(input("Introdueix el segon nombre enter: "))
        while n1 < n2+1:
            print(n1)
            n1=+1

if __name__ == '__main__':
    main()


#ejercicio 3 practica 10

def main():

    persona={}
    bbdd={}
    contador=0
    numero_usuaris=int(input("Introdueix el numero d'usuaris que vols inserir: "))

    while contador<numero_usuaris:
        print("Introdueix l'usuari: ")
        persona["Nom"]=input("Introdueix el nom: ")
        persona["departament"] = input("Introdueix el departament: ")
        persona['clase']=0
        while persona['clase']<1 or persona ['clase']>15:
            persona['clase']=int(input("Introdueix la clase entre el 1 i el 15: "))
            bbdd[contador]=persona
            contador=+1
    print("Els usuaris introduits són: ")

    print()
    print(bbdd)

if __name__ == '__main__':
    main()