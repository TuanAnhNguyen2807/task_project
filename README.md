Task Project - Django project (Task Manager)

Author: Tuan Tran

The goal is to help each developer gain hands-on experience with:

- Django REST Framework (DRF)
- PostgreSQL database integration
- Local API testing
- Collaborative backend development
- Structure folder:
  ```
  task_project/
  │
  ├── manage.py
  ├── requirements.txt
  │
  ├── task_project/
  │   ├── settings.py
  │   ├── urls.py
  │   ├── wsgi.py
  │   └── asgi.py
  │
  └── task_manager/
      ├── models.py
      ├── serializers.py
      ├── views.py
      ├── urls.py
      └── tests.py
  ```

How to use:

**1. Create virtualenv and install requirements:**

   `git clone https://github.com/AkaTVT711/task_project.git`

   `python -m venv venv`

   `source venv/bin/activate`

   `pip install -r requirements.txt`

**2. Configure .env for Postgres. You can run Postgres locally or via Docker:**

   `docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres`

   Then create database if needed:

   `psql -h localhost -U postgres -c "CREATE DATABASE task_db;"`
**3. Run migrations and start server:**

   `python manage.py makemigrations`

   `python manage.py migrate`

   `python manage.py createsuperuser`

   `python manage.py runserver`

API endpoint: http://127.0.0.1:8000/api/tasks/

Admin: http://127.0.0.1:8000/admin/

**4. API endpoints**

| Method | Endpoint         | Description      |
|--------|------------------|------------------|
| GET    | /api/tasks/      | List all tasks   |
| POST   | /api/tasks/      | Create a new task |
| PUT    | /api/tasks/{id}/ | Update task       |
| DELETE | /api/tasks/{id}/ | Delete task      |
| GET    | /api/tasks/{id}/ | Retrieve one task |

Example POST body:

```
{
  "title": "Finish Django tutorial",
  "description": "Complete CRUD exercises",
  "is_completed": false
}
```

**5. Practice Tasks**

**#1: Authentication & User Management**

**Goal: Secure the API and support multi-user access.**
Tasks:
- Install and configure djangorestframework-simplejwt.
- Add registration and login endpoints.
- Restrict task access — each user sees only their tasks.
- Endpoints:
   ```
   POST /api/register/

   POST /api/login/
   
   GET /api/me/
   ```
  
**#2: Search & Filter Features**
Goal: Improve task discoverability.

Tasks:

- Add query parameters for:
  - Keyword search (?q=learn)
  - Completion filter (?is_completed=true)
- Use django-filter or manual filtering in the view.

Example:
```GET /api/tasks/?is_completed=true&q=django```

**#3: Pagination & Sorting**

Goal: Improve performance for large data sets.

Tasks:

Add pagination (page + page_size query params)

Add sorting by created or updated date

Example:

```GET /api/tasks/?page=2&page_size=10&ordering=-created_at```

_Use DRF’s built-in PageNumberPagination and OrderingFilter._