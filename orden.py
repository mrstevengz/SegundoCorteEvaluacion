from classes import Cola

# Crear instancia de la cola de pacientes
cola_pacientes = Cola()

while True:
    print("\n📌 MENU:")
    print("1️⃣ Mostrar pacientes en espera")
    print("2️⃣ Atender paciente")
    print("0️⃣ Salir")

    opcion = input("👉 Selecciona una opción: ")

    if opcion == "1":
        cola_pacientes.mostrar_cola()  # Usa la función de la clase ya definida
    
    elif opcion == "2":
        cola_pacientes.desencolar()  # Usa la función de la clase para atender al siguiente paciente

    elif opcion == "0":
        print("👋 Saliendo del sistema...")
        break

    else:
        print("⚠️ Opción inválida, intenta de nuevo.")

