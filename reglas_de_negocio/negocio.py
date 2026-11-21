class Vehiculo:
    def __init__(self, __patente, __nombre_responsable, __contacto_responsable):
        self.patente = __patente
        self.nombre_responsable = __nombre_responsable
        self.contacto_responsabe = __contacto_responsable

    @property
    def get_patente(self):
        return self.patente

    def get_nombre_responsable(self):
        return self.nombre_responsable

    def get_contacto_responsable(self):
        return self.contacto_responsabe

    @patente.setter
    def set_patente(self, patente):
        if patente.strip() == None:
            raise ValueError("La patente no puede estar vacía")

            
        