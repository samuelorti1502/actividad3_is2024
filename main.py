class Persona:
    def __init__(self):
        self._nombre = input("Ingrese su nombre: ")
        self._apellidos = input("Ingrese sus apellidos: ")
        self._direccion = input("Ingrese su dirección: ")
        self._telefono = input("Ingrese su teléfono: ")
        self._fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, value):
        self._apellidos = value

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value):
        self._fecha_nacimiento = value

    def __str__(self):
        return f"Persona: {self.nombre} {self.apellidos}\n" \
               f"Dirección: {self.direccion}\n" \
               f"Teléfono: {self.telefono}\n" \
               f"Fecha de nacimiento: {self.fecha_nacimiento}"

    def ver_informacion(self):
        print(self)

    def modificar_informacion(self):
        while True:
            opcion = input("¿Qué desea modificar?\n"
                           "1. Nombre\n"
                           "2. Apellidos\n"
                           "3. Dirección\n"
                           "4. Teléfono\n"
                           "5. Fecha de nacimiento\n"
                           "0. Salir\n"
                           "Ingrese su opción: ")
            if opcion == "0":
                break
            elif opcion == "1":
                self.nombre = input("Ingrese su nuevo nombre: ")
            elif opcion == "2":
                self.apellidos = input("Ingrese sus nuevos apellidos: ")
            elif opcion == "3":
                self.direccion = input("Ingrese su nueva dirección: ")
            elif opcion == "4":
                self.telefono = input("Ingrese su nuevo teléfono: ")
            elif opcion == "5":
                self.fecha_nacimiento = input("Ingrese su nueva fecha de nacimiento (YYYY-MM-DD): ")
            else:
                print("Opción inválida.")


persona1 = Persona()

while True:
    opcion = input("¿Qué desea hacer?\n"
                   "1. Ver información\n"
                   "2. Modificar información\n"
                   "0. Salir\n"
                   "Ingrese su opción: ")
    if opcion == "0":
        break
    elif opcion == "1":
        persona1.ver_informacion()
    elif opcion == "2":
        persona1.modificar_informacion()
    else:
        print("Opción inválida.")

class Cliente:
    def __init__(self, nit):
        self.nit = nit

    def mostrar_informacion(self):
        print(f"NIT: {self.nit}")

    def actualizar_informacion(self, nit):
        self.nit = nit

nit = input("Ingrese el NIT del cliente: ")

cliente1 = Cliente(nit)

print("Información ingresada:")
cliente1.mostrar_informacion()

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self._codigo_empleado = input("Ingrese el código de empleado: ")
        self._cargo = input("Ingrese el cargo del empleado: ")
        self._salario = float(input("Ingrese el salario del empleado: "))

    @property
    def codigo_empleado(self):
        return self._codigo_empleado

    @codigo_empleado.setter
    def codigo_empleado(self, value):
        self._codigo_empleado = value

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        self._cargo = value

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, value):
        self._salario = value

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Código de empleado: {self.codigo_empleado}\n" \
               f"Cargo: {self.cargo}\n" \
               f"Salario: {self.salario}"

    def ver_informacion(self):
        super().ver_informacion()
        print(f"Código de empleado: {self.codigo_empleado}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: {self.salario}")

    def modificar_informacion(self):
        super().modificar_informacion()
        while True:
            opcion = input("¿Qué desea modificar?\n"
                           "6. Código de empleado\n"
                           "7. Cargo\n"
                           "8. Salario\n"
                           "0. Salir\n"
                           "Ingrese su opción: ")
            if opcion == "0":
                break
            elif opcion == "6":
                self.codigo_empleado = input("Ingrese el nuevo código de empleado: ")
            elif opcion == "7":
                self.cargo = input("Ingrese el nuevo cargo: ")
            elif opcion == "8":
                self.salario = float(input("Ingrese el nuevo salario: "))
            else:
                print("Opción inválida.")

persona1 = Empleado()

while True:
    opcion = input("¿Qué desea hacer?\n"
                   "1. Ver información\n"
                   "2. Modificar información\n"
                   "0. Salir\n"
                   "Ingrese su opción: ")
    if opcion == "0":
        break
    elif opcion == "1":
        persona1.ver_informacion()
    elif opcion == "2":
        persona1.modificar_informacion()
    else:
        print("Opción inválida.")
