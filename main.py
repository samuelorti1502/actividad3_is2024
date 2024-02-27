class Persona:
                print("Opción inválida.")


# Ejemplo de uso

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
            self.nit = nit

# Ejemplo de uso:
cliente1 = Cliente("Juan", "Perez", "Calle A, No. 123", "123456789", "01/01/1990", "123456789X")

# Mostrar información
print("Información inicial:")
cliente1.mostrar_informacion()

# Actualizar información
cliente1.actualizar_informacion(apellidos="López", telefono="987654321", nit="987654321Y")

print("\nInformación actualizada:")
cliente1.mostrar_informacion()
