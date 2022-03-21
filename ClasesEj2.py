# Código por Xoaquín Fabeiro Monteagudo

from datetime import date, datetime

# Definición de la clase Empleado


class Empleado:
    # Constructor de objetos
    def __init__(self, NIF, nombre, fecha_nacimiento, tipo, fecha_alta, sueldo):
        self.NIF = NIF
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.tipo = tipo
        self.fecha_alta = fecha_alta
        self.sueldo = sueldo

# Definición de la clase Empleado Temporal con herencia de la clase Empleado


class EmpleadoTemporal(Empleado):
    # Constructor de objetos
    def __init__(self, *args, fecha_baja):
        super().__init__(*args)
        self.fecha_baja = fecha_baja

    # Función para calcular el sueldo
    def calcular_sueldo(self):
        return self.sueldo


# Definición de la clase Empleado Fijo con herencia de la clase Empleado
class EmpleadoFijo(Empleado):
    # Constructor de objetos
    def __init__(self, *args, complemento_anual):
        super().__init__(*args)
        self.complemento_anual = complemento_anual

    # Función para calcular el sueldo
    def calcular_sueldo(self):
        dt = datetime.now()
        if self.fecha_alta.month <= dt.month:
            anosdif = dt.year - self.fecha_alta.year
        else:
            anosdif = dt.year - self.fecha_alta.year - 1
        return self.sueldo + self.complemento_anual * anosdif
