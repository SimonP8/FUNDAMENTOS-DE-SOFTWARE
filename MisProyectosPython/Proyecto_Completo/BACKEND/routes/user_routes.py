
from flask import Blueprint, jsonify, request

from controllers import user_controller as controller

user_bp = Blueprint("usuarios", __name__)

@user_bp.route("/", methods=["GET"])
def listar():
    data, status = controller.listar_usuarios()
    return jsonify(data), status


