# services.py
from models import db, Usuario

from datetime import datetime

# Crear un usuario
def crear_usuario(nombres, apellidos, ci):
    usuario = Usuario(
        nombres=nombres,
        apellidos=apellidos,
        ci=ci,
        timestamp=datetime.utcnow()
    )
    db.session.add(usuario)
    db.session.commit()
    return usuario

# Obtener todos los usuarios
def obtener_usuarios():
    return Usuario.query.all()

# Obtener un usuario por ID
def obtener_usuario(id):
    return Usuario.query.get(id)

# Actualizar usuario
def actualizar_usuario(id, nombres=None, apellidos=None, ci=None):
    usuario = Usuario.query.get(id)
    if not usuario:
        return None
    if nombres: usuario.nombres = nombres
    if apellidos: usuario.apellidos = apellidos
    if ci: usuario.ci = ci
    db.session.commit()
    return usuario

# Eliminar usuario
def eliminar_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return True
    return False


