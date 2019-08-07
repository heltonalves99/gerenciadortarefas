from operator import itemgetter

from flask import Blueprint, jsonify, request, abort

bp = Blueprint("task_manager", __name__)

TASKS = []


@bp.route("/")
def listar():
    return jsonify(sorted(TASKS, key=itemgetter("state")))


@bp.route("/<int:id_task>/")
def detail(id_task):
    for task in TASKS:
        if task["id"] == id_task:
            return jsonify(task)

    abort(404)


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


@bp.route("/<int:id_task>/", methods=["PUT"])
def update(id_task):
    if not request.data:
        abort(400)

    task = {}
    for item in TASKS:
        if item["id"] == id_task:
            task = item
            break

    if not task:
        abort(404)

    data = request.json
    task["title"] = data.get("title", task["title"])
    task["description"] = data.get("description", task["description"])
    task["state"] = data.get("state", task["state"])

    return jsonify(task)


@bp.route("/<int:id_task>/done/", methods=["PUT"])
def task_done(id_task):
    for task in TASKS:
        if task["id"] == id_task:
            task["state"] = True
            return "", 200

    abort(404)


@bp.route("/<int:id_task>/", methods=["DELETE"])
def delete(id_task):
    task = [task for task in TASKS if task['id'] == id_task]

    if not task:
        abort(404)

    TASKS.remove(task[0])
    return "", 204
