from datetime import date

class Ingrediente:
    def __init__(self, nombre, unidad_medida):
        self.id = nombre.lower().replace(" ", "_")
        self.nombre = nombre
        self.unidad_medida = unidad_medida

class IngredienteEnReceta:
    def __init__(self, ingrediente, cantidad):
        self.ingrediente = ingrediente
        self.cantidad = cantidad

class Receta:
    def __init__(self, nombre, instrucciones, ingredientes, imagen_path, dificultad, tiempo_prep, categoria):
        self.nombre = nombre
        self.instrucciones = instrucciones
        self.ingredientes = ingredientes
        self.imagen_path = imagen_path
        self.dificultad = dificultad
        self.tiempo_prep = tiempo_prep
        self.categoria = categoria