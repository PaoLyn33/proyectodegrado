from flask import Blueprint, request, jsonify
import services.usuario_service as usuario_service

usuario_bp = Blueprint("usuario_bp", __name__)

@usuario_bp.route("/usuarios", methods=["GET"])
def get_usuarios():
    usuarios = usuario_service.get_all_usuarios()
    return jsonify([{"id": u.id, "nombres": u.nombres, "apellidos": u.apellidos, "ci": u.ci} for u in usuarios])

@usuario_bp.route("/usuarios/<int:id>", methods=["GET"])
def get_usuario(id):
    usuario = usuario_service.get_usuario_by_id(id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"id": usuario.id, "nombres": usuario.nombres, "apellidos": usuario.apellidos, "ci": usuario.ci})

@usuario_bp.route("/usuarios", methods=["POST"])
def create_usuario():
    data = request.json
    nuevo = usuario_service.create_usuario(data)
    return jsonify({"id": nuevo.id, "nombres": nuevo.nombres, "apellidos": nuevo.apellidos, "ci": nuevo.ci}), 201

@usuario_bp.route("/usuarios/<int:id>", methods=["PUT"])
def update_usuario(id):
    data = request.json
    actualizado = usuario_service.update_usuario(id, data)
    if not actualizado:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"id": actualizado.id, "nombres": actualizado.nombres, "apellidos": actualizado.apellidos, "ci": actualizado.ci})

@usuario_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def delete_usuario(id):
    eliminado = usuario_service.delete_usuario(id)
    if not eliminado:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"message": "Usuario eliminado"})
