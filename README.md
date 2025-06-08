# Vaccination API

A Django REST API for managing vaccination appointments and user registrations.

## Features

- User registration & login (coming soon)
- Vaccine management (CRUD)
- Appointment scheduling (coming soon)
- Admin interface
- REST API (via Django REST Framework)
- Docker-ready setup (coming later)

## Technologies

- Python 3
- Django
- Django REST Framework
- SQLite (default, can be extended to PostgreSQL, MySQL etc.)

## Installation

```bash
git clone https://github.com/CusinM15/vaccination.git
cd vaccination-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
