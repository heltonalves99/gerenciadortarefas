from flask import Blueprint, jsonify

# bp = Blueprint('task_manager', __name__, url_prefix='/todo')
bp = Blueprint("task_manager", __name__)

TASKS = []

@bp.route("/")
def listar():
    return jsonify(TASKS)
