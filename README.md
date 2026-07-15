# DevTrack Backend: Django REST API

The DevTrack backend is a REST API built with Django and Django REST Framework.
It provides authentication, project management, task management, dashboard analytics, and relational data modeling for the DevTrack SaaS application.

## Features

### Authentication

* JWT authentication with access and refresh tokens
* Secure login endpoint
* Protected API routes

### Projects API

* Create, update, and delete projects
* User scoped project filtering
* Automatic owner assignment

### Tasks API

* Full CRUD support
* Tasks linked to projects with ForeignKey
* Status, priority, and due date fields
* Filtering by project and status

### Dashboard Analytics

* Total projects
* Total tasks
* Tasks grouped by status

### Tech Stack

* Python 3
* Django
* Django REST Framework
* SimpleJWT
* PostgreSQL recommended

## Running the full stack locally

### Start the backend

```powershell
cd backend
.\env\Scripts\Activate.ps1
python manage.py runserver
```

### Start the frontend

```powershell
cd frontend
npm install
npm run dev
```

## Project Structure

```text
devtrack/
  accounts/
  projects/
  tasks/
  devtrack/
  manage.py
```

## Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/devtrack-backend.git
cd devtrack-backend
```

### Create a virtual environment

```bash
python -m venv venv
```

For macOS or Linux:

```bash
source venv/bin/activate
```

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply migrations

```bash
python manage.py migrate
```

### Create a superuser

```bash
python manage.py createsuperuser
```

### Run the server

```bash
python manage.py runserver
```

## API Endpoints

### Auth

```text
POST /api/token/
POST /api/token/refresh/
```

### Projects

```text
GET    /api/projects/
POST   /api/projects/
PUT    /api/projects/:id/
DELETE /api/projects/:id/
```

### Tasks

```text
GET    /api/tasks/?project=<id>&status=<status>
POST   /api/tasks/
PUT    /api/tasks/:id/
DELETE /api/tasks/:id/
```

### Dashboard Analytics

```text
GET /api/dashboard-stats/
```

## Models Overview

### Project Model

* owner ForeignKey to User
* name
* description
* created_at

### Task Model

* project ForeignKey to Project
* title
* description
* status: todo, in_progress, done
* priority: low, medium, high
* due_date
* created_at

## Example token request

```powershell
curl.exe -v -X POST http://127.0.0.1:8000/api/token/ -H "Content-Type: application/json" --data-raw '{"username":"admin","password":"123456"}'
```

## Author

**Mohammad Eslamifar**
Full Stack Developer
Rome, Italy

## Why This Backend Matters

This backend demonstrates professional API engineering:

* JWT authentication
* Protected routes
* Relational database modeling
* REST API design
* Analytics endpoints
* Clean Django app structure
* DRF best practices
* Filtering, querying, and serialization

If you like this project, consider starring the repo.
