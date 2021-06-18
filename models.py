import db
from sqlalchemy import Column, Integer, String, Boolean, Date, DATETIME


"""
 Creamos una clase llamada Tarea 
 Esta clase va ser nuestro modelo de datos de la tarea ( el cual nos servirá luego para la base de datos)
 Esta clase va a almacenar toda la información referente a una tarea
 
"""

class Tarea(db.Base):
    __tablename__ = "Tarea"
    id = Column(Integer, primary_key=True)
    # id, por eso es primary key.
    contenido = Column(String(200), nullable=False)
    hecha = Column(Boolean)
    fecha_creada = Column(Date)
    hora = Column(DATETIME)
    fecha_entrega = Column(Date)

    def __init__(self, contenido, hecha, fecha_creada, hora, fecha_entrega):
        self.contenido = contenido
        self.hecha = hecha
        self.fecha_creada = fecha_creada
        self.hora = hora
        self.fecha_entrega = fecha_entrega

    def __repr__(self):
        return "Tarea {}: {} {} {} {} {}".format(self.id, self.contenido, self.hecha, self.fecha_creada, self.hora, self.fecha_entrega)

    def __str__(self):
        return "Tarea {}: {} {} {} {} {}".format(self.id, self.contenido, self.hecha, self.fecha_creada, self.hora, self.fecha_entrega)
