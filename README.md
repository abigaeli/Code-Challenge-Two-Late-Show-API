# Code Challenge Two - Late Show API

## Overview
This project is a backend API for managing a Late Show application. It provides endpoints for user authentication, managing episodes, guests, and appearances. The API is built using Flask, SQLAlchemy, and Flask-JWT-Extended for authentication.

## Features
- User registration and login with JWT authentication
- CRUD operations for episodes
- Retrieval of guests and appearances
- Secure endpoints requiring authentication for modifications
- Database migrations with Flask-Migrate
- Unit tests covering key API endpoints

## Technologies Used
- Python 3.8
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- PostgreSQL (default, but can fallback to SQLite for testing)
- Pytest for testing

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL database (optional, SQLite used by default for testing)
- Git

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd Code-Challenge-Two-Late-Show-API
   ```

2. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   Create a `.env` file in the root directory and set the following variables:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/your_db_name
   JWT_SECRET_KEY=your_jwt_secret_key
   ```

   If `DATABASE_URL` is not set, the app will use an in-memory SQLite database by default.

5. Initialize the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Run the application:
   ```
   flask run
   ```

## Running Tests
Run the tests using pytest:
```
pytest server/tests
```

## API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and receive a JWT token

### Episodes
- `GET /episodes/` - Get all episodes
- `GET /episodes/<id>` - Get episode by ID
- `DELETE /episodes/<id>` - Delete episode by ID (requires JWT)

### Guests
- `GET /guests/` - Get all guests

### Appearances
- `GET /appearances/` - Get all appearances
- `POST /appearances/` - Create a new appearance (requires JWT)

## Notes
- Ensure the database credentials are correctly set in the environment variables.
- The app uses JWT for securing certain endpoints; include the token in the `Authorization` header as `Bearer <token>`.
- The project includes seed data and migration scripts for easy setup.

## License
This project is licensed under the MIT License.
