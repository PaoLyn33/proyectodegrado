from flask import Blueprint, request, jsonify
import services.celular_service as celular_service

celular_bp = Blueprint("celular_bp", __name__)

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


@celular_bp.route("/celulares", methods=["GET"])
def get_celular():
    celulares = celular_service.get_all_celulares()
    return jsonify([{"id": c.id, "nombre_dispositivo": c.nombre_dispositivo, "modelo": c.modelo, "version": c.version, 
    "cpu":c.cpu, "ram":c.ram, "rom":c.rom, "bateria":c.bateria, "versionhios":c.versionhios, "numero_compilacion":c.numero_compilacion} for u in celulares])

@celular_bp.route("/celulares/<int:id>", methods=["GET"])
def get_celular(id):
    celular = celular_service.get_celular_by_id(id)
    if not celular:
        return jsonify({"error": "Celular no encontrado"}), 404
    return jsonify({"id": celular.id, "nombre_dispositivo": celular.nombre_dispositivo, "modelo": celular.modelo, "version": celular.version, 
    "cpu":celular.cpu, "ram":celular.ram, "rom":celular.rom, "bateria":celular.bateria, "versionhios":celular.versionhios, "numero_compilacion":celular.numero_compilacion})

@celular_bp.route("/celulares", methods=["POST"])
def create_celular():
    data = request.json
    nuevo = celular_service.create_celular(data)
    return jsonify({"id": nuevo.id, "nombre_dispositivo": nuevo.nombre_dispositivo, "modelo": nuevo.modelo, "version": nuevo.version, 
    "cpu":nuevo.cpu, "ram":nuevo.ram, "rom":nuevo.rom, "bateria":nuevo.bateria, "versionhios":nuevo.versionhios, "numero_compilacion":nuevo.numero_compilacion}), 201

@celular_bp.route("/celulares/<int:id>", methods=["PUT"])
def update_celular(id):
    data = request.json
    actualizado = celular_service.update_celular(id, data)
    if not actualizado:
        return jsonify({"error": "Celular no encontrado"}), 404
    return jsonify({"id": actualizado.id, "nombre_dispositivo": actualizado.nombre_dispositivo, "modelo": actualizado.modelo, "version": actualizado.version, 
    "cpu":actualizado.cpu, "ram":actualizado.ram, "rom":actualizado.rom, "bateria":actualizado.bateria, "versionhios":actualizado.versionhios, "numero_compilacion":actualizado.numero_compilacion})

@celular_bp.route("/celulares/<int:id>", methods=["DELETE"])
def delete_celular(id):
    eliminado = celular_service.delete_celular(id)
    if not eliminado:
        return jsonify({"error": "Celular no encontrado"}), 404
    return jsonify({"message": "Celular eliminado"})
