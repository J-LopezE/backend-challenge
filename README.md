# Backend Challenge

![CI](https://github.com/TU_USUARIO/backend-challenge/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-pending-yellow)

## Description
REST API built with Flask and Flask-RESTX following Clean Architecture principles.
Includes Swagger documentation, SQLAlchemy ORM, Docker support and automated testing.

## Tech Stack
- **Flask** — lightweight web framework for Python
- **Flask-RESTX** — REST API framework with automatic Swagger UI
- **SQLAlchemy** — ORM for database management
- **Flask-Migrate** — database migrations with Alembic
- **pytest** — testing framework
- **Docker** — containerization for consistent deployment
- **SQLite** — development database

## Architecture
This project follows Clean Architecture with 4 layers:

- **Presentation** (`routes/`) — HTTP endpoints and DTOs
- **Service** (`services/`) — business logic
- **Repository** (`repositories/`) — database access
- **Domain** (`models/`) — entity definitions

```
app/
├── routes/         # Presentation layer
├── services/       # Service layer  
├── repositories/   # Repository layer
├── models.py       # Domain layer
└── exceptions/     # Custom exceptions
```
## Prerequisites
- Python 3.12+
- Docker and Docker Compose (optional)
- Git

## Getting Started

### Recommended — Docker (no installation required)
```bash
git clone https://github.com/TU_USUARIO/backend-challenge.git
cd backend-challenge
docker-compose up --build
```
API available at: `http://localhost:5000/`
Swagger UI at: `http://localhost:5000/`

### Alternative — Local development
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
flask --app app db upgrade
python -m app.main
```

## Environment Variables
| Variable | Description | Example |
|---|---|---|
| `DATABASE_URL` | Database connection URL | `sqlite:///app.db` |
| `FLASK_ENV` | Environment name | `development` |
| `FLASK_DEBUG` | Debug mode | `1` |

## API Documentation
Swagger UI available at: `http://localhost:5000/`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health/` | Health check |
| GET | `/api/users/` | List all users |
| POST | `/api/users/` | Create user |
| GET | `/api/users/{id}` | Get user by id |
| PUT | `/api/users/{id}` | Update user |
| DELETE | `/api/users/{id}` | Delete user |

## Running Tests
### All tests
```bash
pytest -v
```

### Unit tests only
```bash
pytest tests/unit/ -v
```

### Integration tests only
```bash
pytest tests/integration/ -v
```

# Run in background
docker-compose up -d

# Stop
docker-compose down
```

## Known Limitations & Future Improvements
- [ ] JWT authentication not implemented
- [ ] Pagination not implemented for list endpoints
- [ ] PostgreSQL not configured for production
- [ ] Test coverage could be expanded
- [ ] Rate limiting not implemented

## License
MIT