def main():
    """
    Verificar si un número es par positivo/negativo o impar positivo o negativo
    """

    numero = int(input("Ingrese un número entero: "))

    match numero:
        case _ if numero > 0 and numero % 2 == 0:
            print("par positivo")
        case _ if numero > 0 and numero % 2 != 0:
            print("impar positivo")
        case _ if numero < 0 and numero % 2 == 0:
            print("par negativo")
        case _ if numero < 0 and numero % 2 != 0:
            print("impar negativo")
        case _:
            print("Cero")

if __name__=='__main__':
    main()
