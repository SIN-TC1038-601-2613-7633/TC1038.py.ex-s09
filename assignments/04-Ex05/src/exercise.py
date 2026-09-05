def main():
    """
     Escribe un programa que calcule el IMC (Índice de Masa Corporal) de una persona, el cual se utiliza para determinar si la proporción de peso y altura es adecuada. El IMC se puede calcular utilizando la siguiente fórmula:

    indice = peso / altura**2

    Donde el peso debe darse en kilogramos y la altura en metros. La siguiente tabla muestra cómo se clasifican los diferentes rangos de índice:

    Rango de índice          Descripción

    índice < 20              : 'PESO BAJO'

    20 <= índice < 25        : 'NORMAL'

    25 <= índice < 30        : 'SOBREPESO'

    30 <= índice < 40        : 'OBESIDAD'

    índice >= 40             : 'OBESIDAD MORBIDA'
    """

    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))

    indice = peso / altura**2

    match indice:
        case _ if indice < 20:
            print("PESO BAJO")
        case _ if indice >= 20 and indice < 25:
            print("NORMAL")
        case _ if indice >= 25 and indice < 30:
            print("SOBREPESO")
        case _ if indice >= 30 and indice < 40:
            print("OBESIDAD")
        case _ if indice >= 40:
            print("OBESIDAD MORBIDA")

if __name__=='__main__':
    main()
