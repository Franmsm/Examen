import datetime
import re


# variables declaradas
pisos = 10
departamentos_por_piso = 4
precios = {'A': 3800, 'B': 3000, 'C': 2800, 'D': 3500}
departamentos_disponibles = [[True] * departamentos_por_piso for _ in range(pisos)]
compradores = []


def validar_run(run): #validador de run
    run = run.replace(".", "").replace("-", "")  # eliminar puntos y guiones en caso de que el usuario los ingrese


    if not run.isdigit() or len(run) < 8 or len(run) > 9:
        return False


    rut = run[:-1]
    digito_verificador = run[-1]


    rut = rut[::-1]
    multiplicador = 2
    suma = 0


    for digito in rut:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2


    resto = suma % 11
    digito_calculado = 11 - resto
    if digito_calculado == 11:
        digito_calculado = 0
    elif digito_calculado == 10:
        digito_calculado = 'K'


    return str(digito_calculado).upper() == digito_verificador.upper()


def comprar_departamento():
    while True:
        departamento = input("Ingrese el departamento a comprar (Ejemplo: ABCD//1-10): ")
        departamento = departamento.upper()


        if len(departamento) != 2 or departamento[0] not in "ABCD" or not departamento[1].isdigit():
            print("Departamento inválido. Vuelva a intentarlo.")
            continue


        tipo_departamento = departamento[0]
        piso = int(departamento[1])


        if piso < 1 or piso > pisos or tipo_departamento not in precios:
            print("Departamento fuera de rango. Vuelva a intentarlo.")
            continue


        if not departamentos_disponibles[piso-1][ord(tipo_departamento) - ord('A')]:
            print("El departamento no está disponible. Vuelva a intentarlo.")
            continue


        break


    while True:
        run = input("Ingrese el RUN del comprador (sin puntos ni guion): ")


        if not validar_run(run):
            print("RUN inválido. Vuelva a ingresar el RUN.")
        else:
            break


    compradores.append((run, departamento))
    departamentos_disponibles[piso-1][ord(tipo_departamento) - ord('A')] = False


    print("La operación se ha realizado correctamente.")


def mostrar_departamentos_disponibles():
    print("***** Departamentos Disponibles *****")
    for piso, disponibles_piso in enumerate(departamentos_disponibles, start=1):
        print(f"Piso {piso}: ", end="")
        for i, disponible in enumerate(disponibles_piso):
            tipo_departamento = chr(ord('A') + i)
            if disponible:
                print(f"{tipo_departamento}{piso} ", end="")
            else:
                print("X ", end="")
        print()


def ver_listado_compradores():
    if len(compradores) == 0:
        print("No se han realizado compras.")
        return


    compradores_ordenados = sorted(compradores, key=lambda x: x[0])


    print("****** Listado de Compradores ******")
    for run, departamento in compradores_ordenados:
        run_sin_digito_verificador = run[:-1]
        print(f"RUN: {run_sin_digito_verificador}, Departamento: {departamento}")




def mostrar_ganancias_totales():
    ventas_totales = {tipo: [0, 0] for tipo in precios.keys()}  


    for _, departamento in compradores:
        tipo_departamento = departamento[0]
        ventas_totales[tipo_departamento][0] += 1
        ventas_totales[tipo_departamento][1] += precios[tipo_departamento]


    print("****** Ganancias Totales ******")
    print("Tipo de Departamento\tCantidad\tTotal")
    total_general = 0
    for tipo_departamento, (cantidad, total) in ventas_totales.items():
        print(f"{tipo_departamento}\t\t\t{cantidad}\t\t{total} UF")
        total_general += total
    print(f"TOTAL\t\t\t\t\t{total_general} UF")


def salir():
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nGracias por utilizar el sistema. Salida del sistema: {fecha_actual}")


def mostrar_menu():
    print("****** Casa Feliz ******\n* * * *   Menú   * * * *")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")


        if opcion == '1':
            comprar_departamento()
        elif opcion == '2':
            mostrar_departamentos_disponibles()
        elif opcion == '3':
            ver_listado_compradores()
        elif opcion == '4':
            mostrar_ganancias_totales()
        elif opcion == '5':
            salir()
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()








