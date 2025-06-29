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

## Usage

1. **Adding Data**:
   - Use the "Add New User" or "Add New Book" buttons to create new entries
   - Fill in the required information in the forms

2. **Querying Data**:
   - Use the query form at the top of the page
   - Select the table you want to query
   - Choose a field and operator
   - Enter the value to search for
   - Click "Search" to see the results

3. **Managing Data**:
   - Edit or delete entries using the buttons in the tables
   - View all entries in both the Users and Books tables
   - Link books to users through the "Liked Books" field

## Admin Interface

Access the admin interface at `/admin` to:
- Manage users and books
- View and modify relationships between users and books
- Handle database operations directly 