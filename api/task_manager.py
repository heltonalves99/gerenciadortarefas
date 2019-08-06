from operator import itemgetter

from flask import Blueprint, jsonify, request, abort

bp = Blueprint("task_manager", __name__)

TASKS = []


@bp.route("/")
def listar():
    return jsonify(sorted(TASKS, key=itemgetter("state")))


@bp.route("/", methods=["POST"])
def create():
    
    if not request.data \
    or not request.json.get("title") \
    or not request.json.get("description"):
        abort(400)

    task = {
        "id": len(TASKS) + 1,
        "title": request.json.get("title"),
        "description": request.json.get("description"),
        "state": False,
    }
    TASKS.append(task)
    return jsonify(task), 201


@bp.route("/<int:id_task>/", methods=["DELETE"])
def delete(id_task):
    task = [task for task in TASKS if task['id'] == id_task]

    if not task:
        abort(404)

    TASKS.remove(task[0])
    return "", 204
