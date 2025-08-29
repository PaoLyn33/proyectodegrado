# services.py
from models import db, Celular

from datetime import datetime

  id = db.Column(db.Integer, primary_key=True)
    nombre_dispositivo = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    version =  db.Column(db.String(50), nullable=False)
    cpu =  db.Column(db.String(50), nullable=False)
    ram =  db.Column(db.String(50), nullable=False)
    rom =  db.Column(db.String(50), nullable=False)
    bateria =  db.Column(db.String(50), nullable=False)
    versionhios =  db.Column(db.String(50), nullable=False)
    numero_compilacion =  db.Column(db.String(50), nullable=False)
    
# Crear un celular
def crear_archivo(nombre_dispositivo, modelo, version, cpu, ram, rom, bateria, versionhios, numero_compilacion):
    celular = Celular(
        nombre_dispositivo=nombre_dispositivo,
        modelo=modelo,
        version= version,
        cpu= cpu,
        ram= ram,
        rom= rom,
        bateria= bateria,
        versionhios= versionhios,
        numero_compilacion=numero_compilacion
    )
    db.session.add(celular)
    db.session.commit()
    return celular

# Obtener todos los celulares
def obtener_celulares():
    return Celular.query.all()

# Obtener un celular por ID
def obtener_celulares(id):
    return Celular.query.get(id)

# Actualizar celular
def actualizar_celulares(id, nombre=None,modelo=None,version=None, cpu=None, ram=None, rom=None, bateria=None, versionhios=None, numero_compilacion=None):
    celular = Celular.query.get(id)
    if not celular:
        return None
    if nombre: celular.nombre = nombre
    if modelo: celular.modelo = modelo
    if version: celular.version = version
    if cpu: celular.cpu = cpu
    if ram: celular.ram = ram
    if rom: celular.rom = rom
    if bateria: celular.bateria = bateria
    if versionhios: celular.versionhios =versionhios
    if numero_compilacion: celular.numero_compilacion = numero_compilacion
    
    db.session.commit()
    return celular

# Eliminar celular
def eliminar_celular(id):
    celular = Celular.query.get(id)
    if celular:
        db.session.delete(celular)
        db.session.commit()
        return True
    return False
