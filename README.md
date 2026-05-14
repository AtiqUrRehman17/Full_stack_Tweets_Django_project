# 🐦 Full Stack Tweets — Django Project

A full-stack Twitter-inspired web application built with **Django 6**, allowing users to create, view, edit, and delete tweets with optional image attachments. The project follows standard Django MVT architecture .

---

## 📋 Table of Contents

- [🐦 Full Stack Tweets — Django Project](#-full-stack-tweets--django-project)
  - [📋 Table of Contents](#-table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [Project Structure](#project-structure)
  - [Prerequisites](#prerequisites)
  - [Installation \& Setup](#installation--setup)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Create a Virtual Environment](#2-create-a-virtual-environment)
    - [3. Install Dependencies](#3-install-dependencies)
    - [4. Apply Database Migrations](#4-apply-database-migrations)
    - [5. Create a Superuser (for Admin Panel)](#5-create-a-superuser-for-admin-panel)
  - [Running the Project](#running-the-project)
  - [Usage](#usage)
  - [Database](#database)
  - [Admin Panel](#admin-panel)
  - [Dependencies](#dependencies)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)

---

## Overview

This project is a full-stack web application that mimics core tweet functionality. Users can write tweets (short text posts), optionally attach images, and manage (edit or delete) their posts. The application uses Django's built-in ORM for database management, Django's authentication system for user login/logout/registration, and server-rendered HTML templates for the frontend.

---

## Features

- ✅ **Create Tweets** — Post new tweets with text content
- 🖼️ **Image Uploads** — Optionally attach an image to any tweet
- ✏️ **Edit Tweets** — Update the content of existing tweets
- 🗑️ **Delete Tweets** — Remove tweets permanently
- 📋 **Tweet Listing** — View all tweets on a central feed
- 🔐 **User Authentication** — Register, log in, and log out (Django's built-in auth)
- 🛡️ **Admin Panel** — Django admin interface for managing all data
- 📱 **Responsive Frontend** — HTML templates for clean UI rendering

---

## Tech Stack

| Layer      | Technology               |
|------------|--------------------------|
| Backend    | Python, Django 6.0.5     |
| Frontend   | HTML (Django Templates)  |
| Database   | SQLite (default Django)  |
| Images     | Pillow 12.2.0            |
| Server     | Django Dev Server        |

---

## Project Structure

```
Full_stack_Tweets_Django_project/
│
├── chaiheadq/                  # Main Django project directory
│   ├── __init__.py
│   ├── settings.py             # Project settings (DB, installed apps, media, etc.)
│   ├── urls.py                 # Root URL configuration
│   ├── asgi.py                 # ASGI entry point
│   ├── wsgi.py                 # WSGI entry point
│   │
│   ├── tweets/                 # Tweets app (or similar app name)
│   │   ├── migrations/         # Database migrations
│   │   ├── templates/          # HTML templates for tweet views
│   │   ├── __init__.py
│   │   ├── admin.py            # Admin panel registration
│   │   ├── apps.py
│   │   ├── forms.py            # Django ModelForms for tweet creation/editing
│   │   ├── models.py           # Tweet model definition
│   │   ├── urls.py             # App-level URL patterns
│   │   └── views.py            # View functions (CRUD logic)
│   │
│   └── manage.py               # Django management script
│
└── requirements.txt            # Python dependencies
```

> **Note:** The exact sub-app folder name inside `chaiheadq` may vary (e.g., `tweets`, `tweet`, or similar). Refer to the source for the precise naming.

---

## Prerequisites

Make sure you have the following installed on your system:

- **Python 3.10+**
- **pip** (Python package manager)
- **Git**

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AtiqUrRehman17/Full_stack_Tweets_Django_project.git
cd Full_stack_Tweets_Django_project
```

### 2. Create a Virtual Environment

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
cd chaiheadq
python manage.py migrate
```

### 5. Create a Superuser (for Admin Panel)

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

---

## Running the Project

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## Usage

Once the server is running:

1. **Register / Log in** using the authentication pages.
2. **Create a Tweet** by navigating to the tweet creation form, entering text, and optionally uploading an image.
3. **View All Tweets** on the main feed/listing page.
4. **Edit a Tweet** by clicking the edit button on any tweet you own.
5. **Delete a Tweet** by clicking the delete button on any tweet you own.

---

## Database

The project uses **SQLite** (Django's default database), so no additional database setup is required. The database file (`db.sqlite3`) is auto-generated when you run migrations.

To reset the database:

```bash
# Delete the db.sqlite3 file, then re-run migrations
python manage.py migrate
```

---

## Admin Panel

Django's built-in admin interface is available at:

```
http://127.0.0.1:8000/admin/
```

Log in with the superuser credentials you created. From here you can manage all tweets, users, and other model data directly.

---

## Dependencies

Listed in `requirements.txt`:

| Package      | Version   | Purpose                                      |
|--------------|-----------|----------------------------------------------|
| Django       | 6.0.5     | Core web framework                           |
| Pillow       | 12.2.0    | Image processing for tweet image uploads     |
| asgiref      | 3.11.1    | ASGI compatibility layer for Django          |
| sqlparse     | 0.5.5     | SQL query formatting (used internally by Django) |
| tzdata       | 2026.2    | Timezone data for datetime handling          |

Install all at once:

```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## License

This project is open-source and available for learning and personal use. No explicit license file is included — please reach out to the author for clarification before commercial use.

---

## Acknowledgements
- Powered by the **[Django Web Framework](https://www.djangoproject.com/)**.

---

> **Author:** [AtiqUrRehman17](https://github.com/AtiqUrRehman17)