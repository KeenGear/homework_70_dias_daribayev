API Readme

This API provides CRUD (Read, Update, Delete) functionality for a Project model.

Endpoints

GET /api/projects/<int:pk>/
This endpoint returns the Project object with the given pk (primary key).


Example Response:
{
    "id": 1,
    "name": "Project 1",
    "description": "This is the first project",
    "start_date": "2022-01-01",
    "end_date": "2022-06-01",
    "is_completed": false
}

PUT /api/projects/<int:pk>/
This endpoint updates the Project object with the given pk (primary key).

Example Request:
{
    "name": "Project 1 updated",
    "description": "This is the first project updated",
    "start_date": "2022-01-01",
    "end_date": "2022-07-01",
    "is_completed": true
}

Example Response:
{
    "id": 1,
    "name": "Project 1 updated",
    "description": "This is the first project updated",
    "start_date": "2022-01-01",
    "end_date": "2022-07-01",
    "is_completed": true
}

DELETE /api/projects/<int:pk>/
This endpoint deletes the Project object with the given pk (primary key).

Example Response:
HTTP 204 No Content

