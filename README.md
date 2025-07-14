# Complaint Portal

A modern Django-based Complaint Management System for organizations, featuring user registration, complaint submission with file uploads, admin analytics dashboard (with Chart.js), and more.

---

## Features

- **User Registration & Login**: Secure authentication for users and admins.
- **Complaint Submission**: Users can submit complaints with optional file attachments (images/screenshots).
- **User Dashboard**: Track your submitted complaints and their statuses.
- **Admin Dashboard**:
  - View, edit, resolve, and delete complaints.
  - Analytics charts (Chart.js) for complaints by status and priority.
- **File Uploads**: Attachments are stored and accessible via the portal.
- **Responsive UI**: Modern, mobile-friendly design.
- **(Optional/Planned)**: Email notifications when a complaint is resolved.

---

## Tech Stack

- **Backend**: Django 5.x, SQLite (default)
- **Frontend**: HTML5, Bootstrap, Chart.js
- **Other**: Python 3.11+ recommended

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd complaint_portal
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django
# (Add any other packages you use, e.g., Pillow for image support)
```

Or, if you have a `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## Usage

- **User**: Register, log in, and submit complaints with optional attachments.
- **Admin**: Log in at `/admin/login/` or `/admin/` to manage complaints and view analytics.
- **File Uploads**: Uploaded files are stored in the `media/` directory.

---

## Project Structure

```
complaint_portal/
├── complaint_portal/        # Django project settings
├── complaints/              # Main app (models, views, templates)
├── media/                   # Uploaded files
├── db.sqlite3               # SQLite database
├── manage.py
└── requirements.txt         # (If generated)
```

---

## Configuration

- **Media Files**: Ensure `MEDIA_URL` and `MEDIA_ROOT` are set in `settings.py`.
- **Static Files**: Handled by Django's staticfiles app.
- **Email**: Update email backend settings in `settings.py` for production use.

---

## Analytics

- Admin dashboard includes interactive charts for:
  - Complaints by Status (doughnut)
  - Complaints by Priority (pie)
- Powered by Chart.js (client-side).

---

## Security & Deployment

- Change `SECRET_KEY` and set `DEBUG = False` for production.
- Configure allowed hosts and secure your database and media files.

---

## License

MIT License (or your preferred license)

---

## Credits

- Built with Django, Bootstrap, and Chart.js.
- Developed by [Your Name/Team]. 