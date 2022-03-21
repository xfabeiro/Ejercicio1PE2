# Código por Xoaquín Fabeiro Monteagudo

from datetime import date, datetime
from socket import TIPC_CONN_TIMEOUT


class Empleado():

    def __init__(self, NIF, nombre, fecha_nacimiento, sueldo):
        self.NIF = NIF
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.sueldo = sueldo


class EmpleadoTemporal(Empleado):

    def __init__(self, *args, tipo, fecha_alta, fecha_baja):
        super().__init__(*args)
        tipo = 'Temporal'
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja

    def calcular_sueldo(self):
        return self.sueldo


class EmpleadoFijo(Empleado):

    def __init__(self, *args, tipo, fecha_alta, complemento_anual):
        super().__init__(*args)
        tipo = 'Fijo'
        self.fecha_alta = fecha_alta
        self.complemento_anual = complemento_anual

    def calcular_sueldo(self):
        dt = datetime.now()
        if self.fecha_alta.month <= dt.month:
            anosdif = self.fecha_alta.year - dt.year
        else:
            anosdif = self.fecha_alta.year - dt.year - 1
        return (self.sueldo + self.complemento_anual * anosdif)


def Anadir_empleado(diccionario):
    print('Introduzca los datos del empleado')
    tipo = input('Tipo de empleado (fijo/temporal): ')
    while tipo != 'temporal' or tipo != 'fijo':
        tipo = input(
            'Respuesta errónea, debe introducir tipo fijo (fijo) o  tipo temporal (temporal): ')
    nif = input('Introduzca el NIF del nuevo empleado: ')
    nombre = input("Introduzca el nombre del nuevo empleado: ")
    fechanazaux = input(
        'Introduzca la fecha de nacimiento del nuevo empleado con formato dd/mm/aaaa: ').split('/')
    fechanaz = date(int(fechanazaux[2]), int(
        fechanazaux[1]), int(fechanazaux[0]))
    fechaaltaux = input(
        'Introduzca la fecha de alta del nuevo empleado con formato dd/mm/aaaa: ').split('/')
    fechaalta = date(int(fechaaltaux[2]), int(
        fechaaltaux[1]), int(fechaaltaux[0]))
    sueldo = input('Introduzca el sueldo base mensual del nuevo empleado: ')
    if tipo == 'f':
        comp = input(
            'Introduzca el complemento anual del sueldo del nuevo empleado: ')
        diccionario[nif] = EmpleadoFijo(
            nif, nombre, fechanaz, sueldo, fechaalta, comp)
    elif tipo == 't':
        fechabajaaux = input(
            'Introduzca la fecha de baja del nuevo empleado con formato dd/mm/aaaa: ').split('/')
        fechabaja = date(int(fechabajaaux[2]), int(
            fechabajaaux[1]), int(fechabajaaux[0]))
        diccionario[nif] = EmpleadoTemporal(
            nif, nombre, fechanaz, sueldo, fechaalta, fechabaja)


def Borrar_empleado(diccionario):
    nif = input('Introduzca el NIF del usuario que se desea borrar: ')
    del diccionario[nif]


def Listar_empleados(diccionario):
    print("Nombre\tTipo")
    print('--------------------------------------')
    for clave in diccionario:
        print(diccionario[clave].nombre, '\t', diccionario[clave].tipo)


def Mostrar_empleado(diccionario):
    nif = input('Introduzca el NIF del empleado: ')
    print('NIF:\t\t\t\t\t', diccionario[nif].NIF)
    print('Nombre:\t\t\t\t\t', diccionario[nif].nombre)
    print('Fecha de nacimiento:\t', diccionario[nif].fecha_nacimiento.day, '/',
          diccionario[nif].fecha_nacimiento.month, '/', diccionario[nif].fecha_nacimiento.year)
    print('Sueldo mensual:\t\t\t', diccionario[nif].calcular_sueldo())
    print('Tipo:\t\t\t\t\t', diccionario[nif].tipo)
    if diccionario[nif].tipo == 'Temporal':
        print('Fecha de alta:\t\t\t', diccionario[nif].fecha_alta.day, '/',
              diccionario[nif].fecha_alta.month, '/', diccionario[nif].fecha_alta.year)
        print('Fecha de baja:\t\t\t', diccionario[nif].fecha_baja.day, '/',
              diccionario[nif].fecha_baja.month, '/', diccionario[nif].fecha_baja.year)
    else:
        print('Fecha de alta:\t\t\t', diccionario[nif].fecha_alta.day, '/',
              diccionario[nif].fecha_alta.month, '/', diccionario[nif].fecha_alta.year)
        print('Complemento anual:\t\t', diccionario[nif].complemento_anual)


def Mostrar_empleados_cumpleanos(diccionario):
    mes = int(input(
        'Introduzca el mes deseado en un número del 1-12 (1:Enero,...,12:Diciembre): '))
    print('Lista de empleados de cumpleaños:')
    for clave in diccionario:
        if diccionario[clave].fecha_nacimiento.month == mes:
            print(diccionario[clave].nombre, '\t',
                  diccionario[clave].fecha_nacimiento)


'''
NIF:                    78801576B
Nombre:                 Xoaquín Fabeiro
Fecha de nacimiento:    02/05/1997
Sueldo mensual:         4098,50€
Tipo:                   Temporal
Fecha de alta:          02/05/1997
Fecha de baja:          02/05/1997
Complemento anual:      2%

'''
