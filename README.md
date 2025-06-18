# HealthCare_Backend


```markdown
# 🏥 Healthcare Backend API

This is a backend system for a healthcare management application built using Django, Django REST Framework, and PostgreSQL. It allows user registration, login via JWT, and authenticated management of patients, doctors, and patient-doctor assignments.


## 🚀 Features

- 🔐 JWT-based user authentication (login & register)
- 🧑‍⚕️ Add, view, update, delete doctors
- 👨‍👩‍⚕️ Add, view, update, delete patients
- 🔗 Assign doctors to patients with full mapping APIs
- 🔐 Secure access to patient & doctor data via JWT
- 💾 PostgreSQL as the database (configured via `.env`)



## 🧑‍💻 Tech Stack

| Tech                  | Usage                                |
|-----------------------|---------------------------------------|
| Python 3.11           | Backend language                      |
| Django 5.2.3          | Web framework                         |
| Django REST Framework | REST API layer                        |
| PostgreSQL            | Relational database                   |
| SimpleJWT             | Authentication (access/refresh token)|
| Python Decouple       | Secure environment variable handling  |


## 📁 Folder Structure



HealthCare_Backend/
├── core/               # Main app: models, views, serializers
├── config/             # Project settings and URLs
├── manage.py           # Django CLI entry point
├── requirements.txt    # All required Python packages





## 🔧 Environment Variables

Create a `.env` file in the root folder:
env
SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=healthcare
DB_USER=postgres
DB_PASSWORD=your-db-password
DB_HOST=localhost
DB_PORT=5432


## 📦 Installation & Setup

### 🔁 Step 1: Clone the Repository

bash
git clone https://github.com/your-username/HealthCare_Backend.git
cd HealthCare_Backend


### 🔁 Step 2: Create Virtual Environment

bash
python -m venv venv
.\venv\Scripts\activate   # On Windows


### 🔁 Step 3: Install Dependencies

bash
pip install -r requirements.txt


### 🔁 Step 4: Add `.env` File

Create `.env` in the root directory and copy the required environment variables.

### 🔁 Step 5: Run Migrations

bash
python manage.py makemigrations
python manage.py migrate


### 🔁 Step 6: Run the Development Server

bash
python manage.py runserver

By default, the project runs locally on:


http://127.0.0.1:8000/
Note: This address works only on your local machine for testing purposes.
If you deploy the project online (e.g., Render, Railway), you’ll get a public URL.


## 🧪 API Endpoints

### 🔐 Auth Endpoints

| Method | URL                   | Description         |
| ------ | --------------------- | ------------------- |
| POST   | `/api/auth/register/` | Register a new user |
| POST   | `/api/auth/login/`    | Get JWT token       |

### 🩺 Patient Endpoints

| Method | URL                   | Description            |
| ------ | --------------------- | ---------------------- |
| GET    | `/api/patients/`      | List all your patients |
| POST   | `/api/patients/`      | Create a new patient   |
| GET    | `/api/patients/<id>/` | Get patient details    |
| PUT    | `/api/patients/<id>/` | Update a patient       |
| DELETE | `/api/patients/<id>/` | Delete a patient       |

### 👨‍⚕️ Doctor Endpoints

| Method | URL                  | Description         |
| ------ | -------------------- | ------------------- |
| GET    | `/api/doctors/`      | List all doctors    |
| POST   | `/api/doctors/`      | Create a new doctor |
| GET    | `/api/doctors/<id>/` | Get doctor details  |
| PUT    | `/api/doctors/<id>/` | Update a doctor     |
| DELETE | `/api/doctors/<id>/` | Delete a doctor     |

### 🔗 Mapping Endpoints

| Method | URL                                   | Description                           |
| ------ | ------------------------------------- | ------------------------------------- |
| POST   | `/api/mappings/add/`                  | Assign a doctor to a patient          |
| GET    | `/api/mappings/`                      | List all patient-doctor mappings      |
| GET    | `/api/mappings/patient/<patient_id>/` | Get all doctors assigned to a patient |
| DELETE | `/api/mappings/<id>/`                 | Remove a doctor from a patient        |

> 💡 All patient and doctor endpoints require a valid `JWT` token in the `Authorization` header:


Authorization: Bearer <your_access_token>



## 📬 Postman Testing

You can test the API using Postman

1. Register and log in
2. Copy the `access` token
3. Set it in the header:
   
   Authorization: Bearer your_token_here



