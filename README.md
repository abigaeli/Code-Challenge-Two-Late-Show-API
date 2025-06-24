# Code-Challenge-Two-Late-Show-API# Code Challenge Two - Late Show API

This project is a Flask-based API for managing guests, episodes, appearances, and user authentication for the Late Show.

## Features

- User registration and login with JWT authentication
- CRUD operations for guests, episodes, and appearances
- Database integration with PostgreSQL using SQLAlchemy and Flask-Migrate
- API endpoints for managing show data

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables for database and JWT secret in `config.py`
4. Initialize and migrate the database
5. Run the Flask app: `flask run`

## API Endpoints

- `POST /register` - Register a new user
- `POST /login` - Login and receive JWT token
- `GET /guests` - List all guests
- `GET /episodes` - List all episodes
- `GET /episodes/<id>` - Get episode details
- `DELETE /episodes/<id>` - Delete an episode (requires JWT)
- `POST /appearances` - Add an appearance (requires JWT)
- `GET /` - Root route listing all endpoints

## Testing

Please test the API endpoints using tools like Postman or Curl.

## License

MIT License
