# services.py
from models import db, Archivos

from datetime import datetime

# Crear un archivo
def crear_archivo(nombre, formato, fecha_creacion, ubicacion):
    archivos = Archivos(
        nombre=nombre,
        formato=formato,
        fecha_creacion=fecha_creacion,
        ubicacion=ubicacion
    )
    db.session.add(archivos)
    db.session.commit()
    return archivos

# Obtener todos los archivos
def obtener_archivos():
    return Archivos.query.all()

# Obtener un archivo por ID
def obtener_archivos(id):
    return Archivos.query.get(id)

# Actualizar archivo
def actualizar_archivos(id, nombre=None, formato=None, fecha_creacion=None, ubicacion=None):
    archivo = Archivos.query.get(id)
    if not archivo:
        return None
    if nombre: archivo.nombre = nombre
    if formato: archivo.formato = formato
    if fecha_creacion: archivo.fecha_creacion = fecha_creacion
    db.session.commit()
    return archivo

# Eliminar archivo
def eliminar_archivo(id):
    archivo = Archivos.query.get(id)
    if archivo:
        db.session.delete(archivo)
        db.session.commit()
        return True
    return False
