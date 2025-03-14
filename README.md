# fastapi_todos

To view this project locally:

### `git clone git@github.com:AvrilMaleham/fastapi_todos.git`
Clone the app into the directory of your choice.

### `python -m venv venv`
Create a virtual environment (optional but recommended).

### `pip install -r requirements.txt`
Install dependencies.

Make sure **SQLite** is installed locally.

### `uvicorn main:app --reload`
Sets up the DB **and** Runs the app.\

Open [http://localhost:8000/docs](http://localhost:8000/docs) to view the Swagger the browser.

### `sqlite3 todos.db`
Open the SQLite command line to start interacting with DB.

# Key project skills:

- SQLite
- SQLAlchemy
- Authentication
- Authorization
- Hashing Passwords