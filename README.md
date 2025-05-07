# Digital Digitizers

## Overview
Digital Digitizers is a Django-based web application designed to help businesses grow digitally. It provides services like SEO, Google Ads, and Meta Ads, along with a user-friendly dashboard for managing services.

## Features
- **Home Page**: A welcoming landing page with a "Get Started" button to explore services.
- **Services Page**: Displays a list of services in a grid layout.
- **Add/Edit Services**: Allows users to add or edit services via a form.
- **Dashboard**: Manage services and view details.
- **Login Page**: Secure login for accessing the dashboard.

## Project Structure
```
Django_Test/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── landing/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       ├── common/
│       │   └── header.html
│       ├── landing/
│       │   ├── add_service.html
│       │   ├── dashboard.html
│       │   ├── delete_service.html
│       │   ├── index.html
│       │   ├── login.html
│       │   └── service.html
├── Test/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```

## Installation

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. Open the application in your browser:
   ```
   http://127.0.0.1:8000/
   ```

## Usage
- Navigate to the home page to explore services.
- Use the "Login" button to access the dashboard.
- Add, edit, or delete services from the dashboard.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Font Awesome
- **Database**: SQLite

## Folder Details
- **landing/**: Contains the main app logic, including models, views, and templates.
- **templates/**: Contains HTML templates for the application.
- **Test/**: Contains project-level settings and configurations.

## License
This project is licensed under the MIT License.