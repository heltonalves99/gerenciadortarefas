# gerenciadortarefas

gerenciadortarefas is an API built with TDD for study purposes.

A simple task manager.

You can try the API in [console](https://still-plains-31476.herokuapp.com/) ([https://still-plains-31476.herokuapp.com/](https://still-plains-31476.herokuapp.com/))

***

## Endpoints

#### Todo Resources

```http
GET /todo/
```

## Responses

```javascript
[
    {
        "title" : string,
        "description" : string,
        "state" : bool
    }
]
```

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |

***

```http
GET /todo/<id_task>/
```

## Responses

```javascript
{
    "title" : string,
    "description" : string,
    "state" : bool
}
```

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |

***

```http
POST /todo/
```

## Data

```javascript
{
    "title" : string,
    "description" : string
}
```

| Status Code | Description |
| :--- | :--- |
| 201 | `CREATED` |

***

```http
PUT /todo/<id_task>/
```

## Data

```javascript
{
    "title" : string,
    "description" : string,
    "state" : bool
}
```

## Responses

```javascript
{
    "title" : string,
    "description" : string,
    "state" : bool
}
```

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |

***

```http
DELETE /todo/<id_task>/
```

| Status Code | Description |
| :--- | :--- |
| 204 | `NO CONTENT` |

***

```http
PUT /todo/<id_task>/done/
```

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |

***
