# RESTful MVC FastAPI Server

This is a __template project__ for building a RESTful API using the FastAPI framework in a Model-View-Controller (MVC) architecture. The project includes features like Pydantic for data validation, Jinja2 for HTML templating, and a static file server for serving static assets.

## Table of Contents

- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [Run](#run)
- [Usage](#usage)


## Project Structure

### File Structure
```
root_base_project/
|-- app/
|   |-- __init__.py
|   |-- models/
|       |-- __init__.py
|       |-- task.py
|   |-- controllers.py
|   |-- views.py
|-- templates/
|   |-- index.html
|-- config.py
|-- requirements.txt
|-- main.py
```
```
• app: Contains the main application logic.
• models: Pydantic models for data validation.
• controllers.py: Core business logic and interaction with data models.
• views.py: Routing and handling HTTP requests.
• templates: HTML templates for rendering views.
• config.py: Configuration file for application settings.
• requirements.txt: List of project dependencies.
• main.py: Main entry point for running the FastAPI application.
```

### HTML Templates
The HTML templates are located in the templates folder.
Customize the templates in index.html based on your project requirements.

### Static Assets
The static directory inside the templates folder is meant for serving static assets (CSS, JavaScript, images, etc.).
You can add your static assets to this folder.

## API Endpoints
```
• GET /api/tasks: Get a list of tasks.
• POST /api/tasks: Create a new task.
• GET /api/tasks/{task_id}: Get details of a specific task.
• PUT /api/tasks/{task_id}: Update details of a specific task.
• DELETE /api/tasks/{task_id}: Delete a specific task.
```

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/Grrr1337/Python-Projects.git
   ```

2. Ensure you have Python installed (version 3.x recommended).
3. Use an appropriate IDE such as VS Code or a Python-specific IDE like PyCharm.
4. Set up a virtual environment for the project:
    ```bash
    python -m venv .venv
    ```
5. Activate the virtual environment:
    On Windows:
    ```bash
    .venv\Scripts\activate
    ```
    On macOS/Linux:
    ```bash
    source .venv/bin/activate
    ```
6. Install the project dependencies using the provided requirements.txt file:
    ```bash
    pip install -r requirements.txt
    ```

## Run
To run the server, just call the main module:

```bash
python main.py
```


## Usage
The server listens under the following address: *http://127.0.0.1:8000* - In order to try out the endpoints:

Access the __Swagger__ documentation: http://127.0.0.1:8000/docs

Access the __ReDoc__ documentation: http://127.0.0.1:8000/redoc
