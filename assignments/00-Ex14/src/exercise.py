def main():
    """
    Calculadora de tarifas de estacionamiento
    """
    tipo = int(input("Tipo de vehículo: "))
    horas = int(input("Horas estacionado: "))

    match tipo:
        case 1:
            vehiculo = "Motocicleta"
            tarifa = 10
        case 2:
            vehiculo = "Automóvil"
            tarifa = 20
        case 3:
            vehiculo = "Camioneta"
            tarifa = 30
        case 4:
            vehiculo = "Camión"
            tarifa = 50
        case _:
            tarifa = 0

    if tarifa == 0:
        print("Tipo de vehículo no válido")
    else:
        subtotal = horas * tarifa

        if horas > 5:
            descuento = subtotal * 0.10
        else:
            descuento = 0

        total = subtotal - descuento

        print("\nVehículo:", vehiculo)
        print("Tarifa por hora: $", tarifa)
        print("Subtotal: $", subtotal)
        print("Descuento: $", descuento)
        print("Total a pagar: $", total)

if __name__ == "__main__":
    main()