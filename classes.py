class Paciente:
    def __init__(self, nombre, motivo):
        self.nombre = nombre
        self.motivo = motivo
        self.historial_recetas = []
      
    def agregar_receta(self, receta):
        self.historial_recetas.append(receta)

    def ver_historial(self):
        if not self.historial_recetas:
            return "Sin recetas registradas."
        return "\n".join(reversed(self.historial_recetas)) 

class Cola:
    def __init__(self):
        self.cola = []
        self.pacientes_atendidos = []

    def encolar(self, nombre, motivo):
        paciente = self.buscar_paciente(nombre)
        if paciente is None:
            paciente = Paciente(nombre, motivo)
        self.cola.append(paciente)
        print(f"Se agregó el paciente {nombre} por {motivo}")

    def desencolar(self, receta):
        if not self.estavacia():
            paciente = self.cola.pop(0)
            paciente.agregar_receta(receta)
            self.pacientes_atendidos.append(paciente)
            print(f"Se ha atendido a {paciente.nombre}. Receta: {receta}")
        else:
            print("No hay pacientes en espera")

    def estavacia(self):
        return len(self.cola) == 0

    def size(self):
        return len(self.cola)

    def mostrar_cola(self):
        if self.estavacia():
            print("No hay pacientes en espera.")
        else:
            print("Pacientes en espera:")
            for p in self.cola:
                print(f"- {p.nombre}: {p.motivo}")

    def buscar_paciente(self, nombre):
        for paciente in self.cola + self.pacientes_atendidos:
            if paciente.nombre.lower() == nombre.lower():
                return paciente
        return None
