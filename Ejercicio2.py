# Código por Xoaquín Fabeiro Monteagudo

from datetime import date, datetime


class Empleado:
    def __init__(self, NIF, nombre, fecha_nacimiento, tipo, fecha_alta, sueldo):
        self.NIF = NIF
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo = tipo
        self.fecha_alta = fecha_alta
        self.sueldo = sueldo


class EmpleadoTemporal(Empleado):
    def __init__(self, *args, fecha_baja):
        super().__init__(*args)
        self.fecha_baja = fecha_baja

    def calcular_sueldo(self):
        return self.sueldo


class EmpleadoFijo(Empleado):
    def __init__(self, *args, complemento_anual):
        super().__init__(*args)
        self.complemento_anual = complemento_anual

    def calcular_sueldo(self):
        dt = datetime.now()
        if self.fecha_alta.month <= dt.month:
            anosdif = dt.year - self.fecha_alta.year
        else:
            anosdif = dt.year - self.fecha_alta.year - 1
        return self.sueldo + self.complemento_anual * anosdif


def Anadir_empleado(diccionario):
    print("Introduzca los datos del empleado")
    tipo = input("Tipo de empleado (Fijo/Temporal): ")
    while tipo != "Temporal" and tipo != "Fijo":
        tipo = input("Respuesta errónea, debe introducir tipo fijo (Fijo) o tipo temporal (Temporal): ")
    nif = input("Introduzca el NIF del nuevo empleado: ")
    nombre = input("Introduzca el nombre del nuevo empleado: ")
    fechanazaux = input("Introduzca la fecha de nacimiento del nuevo empleado con formato dd/mm/aaaa: ").split("/")
    fechanaz = date(int(fechanazaux[2]), int(fechanazaux[1]), int(fechanazaux[0]))
    fechaaltaux = input("Introduzca la fecha de alta del nuevo empleado con formato dd/mm/aaaa: ").split("/")
    fechaalta = date(int(fechaaltaux[2]), int(fechaaltaux[1]), int(fechaaltaux[0]))
    sueldo = float(input("Introduzca el sueldo base mensual del nuevo empleado: "))
    if tipo == "Fijo":
        comp = float(input("Introduzca el complemento anual del sueldo del nuevo empleado: "))
        diccionario[nif] = EmpleadoFijo(nif, nombre, fechanaz, tipo, fechaalta, sueldo, complemento_anual=comp)
    elif tipo == "Temporal":
        fechabajaaux = input("Introduzca la fecha de baja del nuevo empleado con formato dd/mm/aaaa: ").split("/")
        fechabaja = date(int(fechabajaaux[2]), int(fechabajaaux[1]), int(fechabajaaux[0]))
        diccionario[nif] = EmpleadoTemporal(nif, nombre, fechanaz, tipo, fechaalta, sueldo, fecha_baja=fechabaja)
    print("Empleado guardado correctamente.")
    print("")


def Borrar_empleado(diccionario):
    nif = input("Introduzca el NIF del usuario que se desea borrar: ")
    del diccionario[nif]


def Listar_empleados(diccionario):
    print("")
    print("Nombre                             Tipo")
    print("------------------------------------------")
    for clave in diccionario:
        print(f"{diccionario[clave].nombre:35}{diccionario[clave].tipo}")
    print("")


def Mostrar_empleado(diccionario):
    nif = input("Introduzca el NIF del empleado: ")
    print("")
    print("NIF:\t\t\t", diccionario[nif].NIF)
    print("Nombre:\t\t\t", diccionario[nif].nombre)
    print("Fecha de nacimiento:\t", diccionario[nif].fecha_nacimiento)
    print("Sueldo mensual:\t\t", diccionario[nif].calcular_sueldo(), " €")
    print("Tipo:\t\t\t", diccionario[nif].tipo)
    if diccionario[nif].tipo == "Temporal":
        print("Fecha de alta:\t\t", diccionario[nif].fecha_alta)
        print("Fecha de baja:\t\t", diccionario[nif].fecha_baja)
    else:
        print("Fecha de alta:\t\t", diccionario[nif].fecha_alta.day)
        print("Complemento anual:\t", diccionario[nif].complemento_anual, " €")
    print("")


def Mostrar_empleados_cumpleanos(diccionario):
    mes = int(input("Introduzca el mes deseado en un número del 1-12 (1:Enero,...,12:Diciembre): "))
    print("")
    print("Lista de empleados de cumpleaños:")
    print("")
    for clave in diccionario:
        if diccionario[clave].fecha_nacimiento.month == mes:
            print(diccionario[clave].nombre, "\t", diccionario[clave].fecha_nacimiento)
    print("")


def main():
    dic = {
        "32.234.234M": EmpleadoFijo(
            "32.234.234M",
            "Pedro Rodriguez Martinez",
            date(1985, 5, 12),
            "Fijo",
            date(2010, 9, 4),
            2000,
            complemento_anual=200,
        ),
        "33.345.879Z": EmpleadoTemporal(
            "33.345.879Z",
            "Lucía López Rodríguez",
            date(1990, 6, 30),
            "Temporal",
            date(2018, 5, 15),
            2400,
            fecha_baja=date(2022, 5, 15),
        ),
    }
    n = 0
    while not n == 6:
        print("Menú de opciones")
        print("")
        print("(1) Añadir empleado")
        print("(2) Borrar empleado")
        print("(3) Mostrar lista empleados")
        print("(4) Mostrar detalle de un empleado")
        print("(5) Mostrar empleados de cumpleaños")
        print("(6) Terminar")
        n = int(input("Elige una opción :"))
        if n == 1:
            Anadir_empleado(dic)
        elif n == 2:
            Borrar_empleado(dic)
        elif n == 3:
            Listar_empleados(dic)
        elif n == 4:
            Mostrar_empleado(dic)
        elif n == 5:
            Mostrar_empleados_cumpleanos(dic)


if __name__ == "__main__":
    main()
