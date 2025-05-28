from classes import Cola

cola = Cola()

while True:
    print("Bienvenido al centro de salud")
    print("1. Agregar paciente")
    print("2. Atender paciente")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del paciente: ")
        motivo = input("Motivo de consulta: ")
        cola.encolar(nombre, motivo)
    elif opcion == "2":
        cola.desencolar()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")