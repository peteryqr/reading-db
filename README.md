# Reading Database

A Django-based web application for managing and querying a library database.

## Database Query Implementation
The database query logic is implemented in `reading-db/library/views.py`.

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Apply database migrations:
```bash
python manage.py migrate
```

4. Create superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```

## Running the Application

1. Start the server:
```bash
python manage.py runserver
```

2. Access:
- Application: http://localhost:8000
- Admin interface: http://localhost:8000/admin

## Admin Interface

Access the admin interface at `/admin` to:
- Manage users and books
- View and modify relationships between users and books
- Handle database operations directly 