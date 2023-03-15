# HyperSchool

HyperSchool is a Django-based project designed to manage an online school's registration, course management, and scheduling. The application allows users to sign up, log in, view course offerings, get details about courses and instructors, and apply for courses.

## Features

- User authentication system for signup and login.
- Dynamic course listing page with search functionality.
- Detailed views for courses and teachers.
- Application form for enrolling in courses.
- Admin interface for managing teachers, courses, and students.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

1. **Clone the Repository**

   Open a terminal and run:
   ```
   git clone https://github.com/SonikSeven/hyperschool.git
   ```

2. **Navigate to the project directory**
   ```
   cd hyperschool
   ```

3. **Install Dependencies**

   It is recommended to use a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # For Unix/macOS
   venv\Scripts\activate  # For Windows
   ```
   Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. **Set Up Django**
   
   Navigate to the project root directory (`hyperschool`) where `manage.py` is located, then run migrations to prepare your database.
   ```
   python manage.py migrate
   ```

5. **Start the Server**
   ```
   python manage.py runserver
   ```
   This command starts a local server. By default, the application runs at `http://127.0.0.1:8000/`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.
