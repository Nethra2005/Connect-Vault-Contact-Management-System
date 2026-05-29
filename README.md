# Connect-Vault

## Contact Management System using Flask and MongoDB

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen)
![License](https://img.shields.io/badge/License-Educational-orange)

---

## Project Overview

Connect-Vault is a full-stack Contact Management System developed using Python Flask and MongoDB. The application allows users to securely store, manage, search, update, and delete contact information through an intuitive web interface.

The project demonstrates database integration, authentication, CRUD operations, session management, and full-stack web development concepts.

---

## Features

- User Registration
- User Login and Logout
- Secure Password Hashing
- Add New Contacts
- View All Contacts
- Search Contacts by Name
- Update Existing Contacts
- Delete Contacts
- MongoDB Database Integration
- Session Management
- Responsive User Interface

---

## Technology Stack

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Flask

### Database
- MongoDB

### Libraries
- Flask
- PyMongo
- Werkzeug

---

## Project Structure

```text
Connect-Vault/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── index.html
│   ├── add_contact.html
│   └── edit_contact.html
│
└── static/
    └── style.css
```

---

## Installation Guide

### Clone Repository

```bash
git clone https://github.com/your-username/connect-vault.git
cd connect-vault
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## MongoDB Setup

Start MongoDB Service:

```bash
mongod
```

or

```bash
net start MongoDB
```

---

## Run the Application

```bash
python app.py
```

Open Browser:

```text
http://127.0.0.1:5000
```

---

## Database Schema

### Users Collection

```json
{
  "_id": "ObjectId",
  "username": "user123",
  "password": "hashed_password"
}
```

### Contacts Collection

```json
{
  "_id": "ObjectId",
  "name": "John Doe",
  "phone": "9876543210",
  "email": "john@example.com",
  "address": "Chennai"
}
```

---

## System Workflow

```text
User
 ↓
Flask Frontend
 ↓
Flask Backend
 ↓
MongoDB Database
 ↓
Response to User
```

---

## Learning Outcomes

- Flask Web Development
- MongoDB Integration
- CRUD Operations
- User Authentication
- Session Management
- Password Security
- Full Stack Development

---

## Future Enhancements

- Contact Photo Upload
- Export Contacts to CSV
- Export Contacts to PDF
- MongoDB Atlas Cloud Deployment
- REST API Integration
- Email Notifications
- Mobile App Support
- Advanced Search Filters

---

## Resume Description

Developed Connect-Vault, a full-stack contact management application using Python Flask and MongoDB. Implemented secure user authentication, CRUD operations, search functionality, session management, and database integration for efficient contact management.

---

## Author

### Nethra B V

Bachelor of Engineering

---

## License

This project is developed for educational and academic purposes. Feel free to use and modify it for learning purposes.
