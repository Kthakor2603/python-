# ✅ To-Do List Manager — Python Flask

A beginner-level To-Do List web app built with Python (Flask) backend.

## Features
- ✅ Add new tasks
- ✔️ Mark tasks as done / undone
- 🗑️ Delete tasks
- 📊 Task stats (Total / Done / Pending)
- 🔍 Filter by All / Pending / Done
- ⌨️ Press Enter to add task

## Tech Stack
- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Deployed on: Render

## Run Locally
```bash
pip install -r requirements.txt
python app.py
```
Open http://localhost:5000

## Project Structure
```
todo-app/
├── app.py
├── requirements.txt
├── render.yaml
├── README.md
└── templates/
    └── index.html
```

## API Routes
| Method | Route | Description |
|--------|-------|-------------|
| GET | / | Home page |
| GET | /tasks | Get all tasks |
| POST | /tasks | Add new task |
| PUT | /tasks/<id>/done | Toggle done |
| DELETE | /tasks/<id> | Delete task |

## Author
- University: Parul University
- Subject: Programming in Python with Full Stack Development (303105257)
- Semester: 4
