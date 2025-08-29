from flask import Blueprint, request, jsonify
import services.reporte_service as reporte_service

reporte_bp = Blueprint("reporte_bp", __name__)

@reporte_bp.route("/reportes", methods=["GET"])
def get_reportes():
    reportes = reporte_service.get_all_usuarios()
    return jsonify([{"id": r.id, "fecha": r.fecha, } for u in reportes])

@reporte_bp.route("/reportes/<int:id>", methods=["GET"])
def get_reportes(id):
    reporte = reporte_service.get_reporte_by_id(id)
    if not reporte:
        return jsonify({"error": "Reporte no encontrado"}), 404
    return jsonify({"id": reporte.id, "fecha": reporte.fecha})

@reporte_bp.route("/reportes", methods=["POST"])
def create_reposte():
    data = request.json
    nuevo = reporte_service.create_usuario(data)
    return jsonify({"id": nuevo.id, "fecha": nuevo.fecha}), 201

@reporte_bp.route("/reportes/<int:id>", methods=["PUT"])
def update_reporte(id):
    data = request.json
    actualizado = reporte_service.update_reporte(id, data)
    if not actualizado:
        return jsonify({"error": "Reporte no encontrado"}), 404
    return jsonify({"id": actualizado.id, "fecha": actualizado.fecha})

@reporte_bp.route("/reportes/<int:id>", methods=["DELETE"])
def delete_reporte(id):
    eliminado = reporte_service.delete_reporte(id)
    if not eliminado:
        return jsonify({"error": "Reporte no encontrado"}), 404
    return jsonify({"message": "Reporte eliminado"})
