

from models import db, Reporte
from datetime import datetime

########################### Servicios para Reportes#################33
# Crear un reporte
def crear_reporte(fecha, apellidos, ci):
    reporte = Reporte(
        fecha = fecha
    )
    db.session.add(reporte)
    db.session.commit()
    return reporte

# Obtener todos los reportes
def obtener_reporte():
    return Reporte.query.all()

# Obtener un reporte por ID
def obtener_reporte(id):
    return Reporte.query.get(id)

# Actualizar usuario
def actualizar_reporte(id, fecha=None):
    reporte = Reporte.query.get(id)
    if not reporte:
        return None
    if fecha: reporte.fecha = fecha
    db.session.commit()
    return reporte

# Eliminar usuario
def eliminar_reporte(id):
    reporte = Reporte.query.get(id)
    if reporte:
        db.session.delete(reporte)
        db.session.commit()
        return True
    return False