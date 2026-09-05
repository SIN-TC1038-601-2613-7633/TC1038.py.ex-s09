def main():
    """
    Determinar si un año determinado es bisiesto:

    Los años bisiestos son cualquier año que es divisible por 4 (como 2012, 2016, etc).
    Excepto si puede dividirse por 100, entonces no lo es (como 2100, 2200, etc).
    A menos que pueda ser divisible por 400, como 2000, 2400.
    Escribe el programa que determine si un año es bisiesto o no.
    """
    agno     = int(input("Ingrese un año: "))

    match agno:
        case a if a % 4 == 0 and a % 100 != 0:
            print(True)
        case a if a % 400 == 0:
            print(True)
        case _:
            print(False)
    
if __name__=='__main__':
    main()
