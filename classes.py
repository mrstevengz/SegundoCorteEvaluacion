class Paciente:
    def __init__(self, nombre, motivo):
        self.nombre = nombre
        self.motivo = motivo

class Cola:
    def __init__(self):
        self.cola = []

    def encolar(self, nombre, motivo):
        paciente = Paciente(nombre, motivo)
        self.cola.append(paciente)
        print(f"Se agregó el paciente {nombre} por {motivo}")

    def desencolar(self):
        if not self.estavacia():
            paciente = self.cola.pop(0)
            receta = self.generar_receta(paciente)
            print(f"Se ha atendido a {paciente.nombre}. Receta: {receta}")
        else:
            print("No hay pacientes en espera")

    def estavacia(self):
        return len(self.cola) == 0

    def size(self):
        return len(self.cola)

    def generar_receta(self, paciente):
        return "Paracetamol x 5 días"

    def mostrar_cola(self):
        print("Pacientes en espera:")
        for p in self.cola:
            print(f"- {p.nombre}: {p.motivo}")