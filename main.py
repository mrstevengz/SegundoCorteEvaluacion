from classes import Cola

cola = Cola()

while True:
    print("\nBienvenido al centro de salud")
    print("1. Agregar paciente")
    print("2. Atender paciente")
    print("3. Ver pacientes en espera")
    print("4. Consultar historial de recetas de un paciente")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del paciente: ")
        motivo = input("Motivo de consulta: ")
        cola.encolar(nombre, motivo)
    elif opcion == "2":
        if not cola.estavacia():
            paciente = cola.cola[0]
            receta = input(f"Agregue la receta para {paciente.nombre}: ")
            cola.desencolar(receta)
        else:
            print("No hay pacientes en espera")
    elif opcion == "3":
        cola.mostrar_cola()
    elif opcion == "4":
        nombre = input("Ingrese el nombre del paciente: ")
        paciente = cola.buscar_paciente(nombre)
        if paciente:
            print(f"Historial de recetas de {paciente.nombre}:")
            print(paciente.ver_historial())
        else:
            print("Paciente no encontrado.")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")