# Flask To-Do List Application

This project implements a full-stack RESTful API and a dynamic frontend using the **Flask** microframework. It demonstrates the ability to build lightweight, scalable web applications with proper routing, HTTP method handling, and seamless frontend-backend integration.

## Project Overview

The goal of this project is to create a robust task management system that bridges a Python backend with a responsive HTML/JavaScript frontend.

**Key Features:**
* **RESTful API:** Backend endpoints to `GET`,`POST`, and `DELETE` tasks, adhering to standard REST principles.
* **Interactive Frontend:** A responsive HTML/CSS/JS interface that allows users to add and remove tasks dynamically without page reloads.
* **Real-time DOM Manipulation:** The UI updates instantly using vanilla JavaScript `fetch()` calls.
* **Input Validation:** Server-side checks to ensure data integrity and prevents empty task submissions.
* **MVC Architecture:** clear separation of concersn between Data (Model), UI (View), and Logic (Controller).

## Prerequisites

* **Python 3.8+**
* **Web Browser** (Chrome, Firefox, Edge)

## Setup & Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/shivamgravity/flask-to-do-list-app
    cd flask-demo-app
    ```
2. **Set Up Virtual Environment**
    ```bash
    # create venv
    python -m venv venv

    # activate venv (Windows)
    venv\Scripts\activate

    # activate venv (Mac/Linux)
    source venv/bin/activate
    ```
3. **Install Dependencies**
    ```bash
    pip install flask
    ```

## How to Run

1. **Start the Server:** Run the main python script.
    ```bash
    python app.py
    ```
    *The server will start at `http://127.0.0.1:5000`*
2. **Access the Application:** Open your web browser and go to `http://127.0.0.1:5000`.
3. **Use the App:**
    * **Add Task:** Type a task name and press "Enter" or click the "Add Task" button.
    * **Delete Task:** Click the red "X" button next to any task to remove it.

## Solution Architecture

This project follows a standard **MVC (Model-View-Controller)** pattern adapted for Flask:
* **Backend (Controller):**
    * `app.py` initializes the Flask app and defines the routes.
    * It handles HTTP requests:
        * `GET /todos`: Returns the current list of tasks as JSON.
        * `POST /todos`: Accepts JSON data to create a new task.
        * `DELETE /todos/<id>`: Removes a task by its unique ID.
* **Frontend (View):**
    * `templates/index.html`: The main user interface structure.
    * `static/style.css`: Provides a modern, clean look for the application.
    * **JavaScript logic:** Handles the `fetch()` calls to the API, manipulating the DOM to update the task list dynamically.
* **Data (Model):**
    * For this demo, the data is stored in an in-memory Python list(`todos`), simulating a database connection.

## API Endpoints Reference

| **Method** | **Endpoint** | **Description** | **Request Body** | **Response (Success)** |
|:----------:|:------------:|:---------------:|:----------------:|:----------------------:|
| `GET` | `/todos` | Retrieve all tasks | N/A | `200 OK` JSON list |
| `POST` | `/todos` | Create a new task | `{"task": "Buy milk"}` | `201 Created` JSON object |
| `DELETE` | `/todos/<id>` | Delete a task | N/A | `200 OK` Success message |

## Testing

You can start the application by `python app.py` and test on the development server at `http://127.0.0.1:5000`. This method is much better and interactive since it shows the frontend part.

The CLI way to test the API endpoints directly is to use `curl` or Postman:

1. **Get all tasks:**
    ```bash
    curl http://127.0.0.1:5000/todos
    ```
2. **Add a new task:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d "{\"task\": \"Learn Django"}" http://127.0.0.1:5000/todos
    ```

## Future Improvements

To scale this application for production, the following enhancements are planned:

1. **Persistent Storage:** Replace the in-memory list with a persistent database like **SQLite** or **PostgreSQL** using SQLAlchemy.
2. **User Authentication:** Implement login/signup functionality to allow users to manage their own private task lists.
3. **Task Status:** Add a feature to mark tasks s "Completed" (toggle done/undone) instead of just deleting them.