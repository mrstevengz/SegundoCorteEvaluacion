# Clase Paciente con pila de recetas
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



paciente1 = Paciente("Carlos", "Gripe")
paciente2= Paciente("Juan","Tos")
paciente3= Paciente("Maria","Ardor de garganta")

paciente1.agregar_receta("Paracetamol x 5 días")
paciente1.agregar_receta("Jarabe para la tos x 7 días")
paciente2.agregar_receta("Jarabe para la tos x 5 dias")
paciente3.agregar_receta("Paracetamol x 2 dias")


print("Historial de recetas de", paciente1.nombre)
print(paciente1.ver_historial())
