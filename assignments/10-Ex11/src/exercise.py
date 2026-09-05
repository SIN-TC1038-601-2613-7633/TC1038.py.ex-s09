def main():
    """
    Escribe un programa que lea un número entero que se encuentre entre 0 y 360 que representa los grados del plano cartesiano y que muestre como resultado el número de cuadrante en donde se encuentra.

    En caso de que el grado caiga en un eje, tu programa debe mostrar la palabra "eje".

    En caso de que el grado sea menor a cero o mayor a 360, tu programa debe mostrar la palabra "excede".
    """
    grado = int(input())

    match grado:
        case _ if grado < 0 or grado > 360:
            print("excede")
        case 0 | 90 | 180 | 270:
            print("eje")
        case _ if grado > 0 and grado < 90:
            print("cuadrante", 1)
        case _ if grado > 90 and grado < 180:
            print("cuadrante", 2)
        case _ if grado > 180 and grado < 270:
            print("cuadrante", 3)
        case _ if grado > 270 and grado < 360:
            print("cuadrante", 4)
        case _:
            print("excede")
if __name__=='__main__':
    main()
