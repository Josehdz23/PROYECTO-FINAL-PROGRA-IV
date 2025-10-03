class Ingrediente:
    def __init__(self,nombre,cantidad,unidad,fecha):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad = unidad
        self.fecha = fecha

class GestionIngredientes:
    def __init__(self):
        self.ingredientes = {}

