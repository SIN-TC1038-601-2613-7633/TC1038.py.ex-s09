def main():
    """
    Programa que dada una fecha (año, mes y día), devuelva la fecha del día siguiente
    Entradas:
    Año, mes, día (enteros positivos) en ese orden.

    Salidas:
    Año, mes y día (enteros positivos) en ese orden, que corresponden a la fecha del día siguiente.
    """
    agno  = int(input())
    mes   = int(input())
    dia   = int(input())

    match mes:
        case 2:
            match dia:
                case 29:
                    dia = 1
                    mes += 1
                case 28:
                    if agno % 4 == 0 and (agno % 100 != 0 or agno % 400 == 0):
                        dia += 1
                    else:
                        dia = 1
                        mes += 1
                case _:
                    dia += 1
        case 4 | 6 | 9 | 11:
            match dia:
                case 30:
                    dia = 1
                    mes += 1
                case _:
                    dia += 1
        case _:
            match dia:
                case 31:
                    dia = 1
                    mes += 1
                    if mes > 12:
                        mes = 1
                        agno += 1
                case _:
                    dia += 1

    print(agno)
    print(mes)
    print(dia)

if __name__=='__main__':
    main()
