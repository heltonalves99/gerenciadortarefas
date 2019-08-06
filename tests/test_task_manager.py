import json

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

    task = {"id": 1, "title": "title 1",
            "description": "description 1", "state": False}
    
    TASKS.append(task)

    resp = client.get("/todo/")
    assert resp.json == [task]

    TASKS.clear()


def test_create_task_accept_post(client):
    """
        should accept post request in create task.
    """

    resp = client.post("/todo/")

    assert resp.status_code != 405


def test_create_task_return_created_task(client):
    """
        should create a task and return it.
    """

    TASKS.clear()
    mock_data = {
        "title": "my title",
        "description": "my description",
    }

    resp = client.post("/todo/", json=mock_data)

    data = json.loads(resp.data.decode("utf-8"))
    assert data["id"] == 1
    assert data["title"] == mock_data["title"]
    assert data["description"] == mock_data["description"]
    assert data["state"] is False


def test_create_task_return_status_code_201(client):
    """
        should return status code 201 when to create a task.
    """

    TASKS.clear()
    mock_data = {
        "title": "my title",
        "description": "my description",
    }

    resp = client.post("/todo/", json=mock_data)

    assert resp.status_code == 201


def test_create_task_insert_database(client):
    """
        should create a task and insert it in database.
    """

    TASKS.clear()
    mock_data = {
        "title": "my title",
        "description": "my description",
    }

    client.post("/todo/", json=mock_data)

    assert len(TASKS) > 0


def test_create_task_without_title(client):
    """
        should return status code 400 if data does not have title.
    """

    TASKS.clear()
    mock_data = {
        "description": "my description",
    }

    resp = client.post("/todo/", json=mock_data)

    assert resp.status_code == 400


def test_create_task_without_description(client):
    """
        should return status code 400 if data does not have description.
    """

    TASKS.clear()
    mock_data = {
        "title": "my title",
    }

    resp = client.post("/todo/", json=mock_data)

    assert resp.status_code == 400