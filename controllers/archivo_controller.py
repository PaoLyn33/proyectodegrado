from flask import Blueprint, request, jsonify
import services.archivo_service as archivo_service

archivo_bp = Blueprint("archivo_bp", __name__)

@archivo_bp.route("/archivos", methods=["GET"])
def get_archivo():
    archivos = archivo_service.get_all_archivos()
    return jsonify([{"id": a.id, "nombre": a.nombre, "formato": a.formato, "fecha_creacion": a.fecha_creacion, "ubicacion":a.ubicacion} for u in archivos])

@archivo_bp.route("/archivos/<int:id>", methods=["GET"])
def get_archivo(id):
    archivo = archivo_service.get_archivo_by_id(id)
    if not archivo:
        return jsonify({"error": "Archivo no encontrado"}), 404
    return jsonify({"id": archivo.id, "nombre": archivo.nombre, "formato": archivo.formato, "fecha_creacion": archivo.fecha_creacion, "ubicacion":archivo.ubicacion})

@archivo_bp.route("/archivos", methods=["POST"])
def create_archivo():
    data = request.json
    nuevo = archivo_service.create_archivo(data)
    return jsonify({"id": nuevo.id, "nombre": nuevo.nombre, "formato": nuevo.formato, "fecha_creacion": nuevo.fecha_creacion, "ubicacion": nuevo.ubicacion}), 201

@archivo_bp.route("/archivos/<int:id>", methods=["PUT"])
def update_archivo(id):
    data = request.json
    actualizado = archivo_service.update_archivo(id, data)
    if not actualizado:
        return jsonify({"error": "Archivo no encontrado"}), 404
    return jsonify({"id": actualizado.id, "nombre": actualizado.nombre, "formato": actualizado.formato, "fecha_creacion": actualizado.fecha_creacion, "ubicacion": actualizado.ubicacion})

@archivo_bp.route("/archivos/<int:id>", methods=["DELETE"])
def delete_archivo(id):
    eliminado = archivo_service.delete_archivo(id)
    if not eliminado:
        return jsonify({"error": "Archivo no encontrado"}), 404
    return jsonify({"message": "Archivo eliminado"})
