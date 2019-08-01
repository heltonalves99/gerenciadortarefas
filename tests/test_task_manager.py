from api.task_manager import TASKS


def test_list_tasks_return_status_200(client):
    """
        should return status code 200 in GET list tasks.
    """

    resp = client.get("/todo/")
    assert resp.status_code == 200


def test_list_tastks_return_json_format(client):
    """
        should return a response with JSON format.
    """

    resp = client.get("/todo/")
    assert resp.content_type == "application/json"


def test_list_tasks_return_empty_list(client):
    """
        should return a empty list.
    """

    resp = client.get("/todo/")
    assert resp.json == []


def test_list_tasks_return_not_empty_list(client):
    """
        should return a list with todo task.
    """
    task = {"id": 1, "titulo": "tarefa 1",
            "descricao": "tarefa de numero 1", "estado": False}
    
    TASKS.append(task)

    resp = client.get("/todo/")
    assert resp.json == [task]

    TASKS.clear()
