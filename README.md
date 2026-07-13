# solar-calculator-api

A Django REST API for calculating mounts and joints for a solar panel layout.

This project builds on [solar-calculator](https://github.com/JakubD02/solar-calculator), a pure Python service for solar panel layout calculations, wrapping it in a Django REST Framework API with PostgreSQL persistence, Docker support, and auto-generated OpenAPI documentation.

The service receives a list of panel top-left coordinates and returns calculated positions of:
- **mounts** - structural support locations attaching panels to rafters,
- **joints** - connector positions between adjacent panels.

Each returned item contains coordinates (x, y).

## Tech Stack

- Python 3.11+
- Django 5 + Django REST Framework
- PostgreSQL
- Docker & docker-compose
- pytest
- drf-spectacular (OpenAPI/Swagger documentation)
- ruff (linting)
- GitHub Actions (CI)

## Requirements

- Docker & Docker Compose (recommended, no local Python setup needed)

or, for local development without Docker:
- Python 3.11 or newer
- pip
- PostgreSQL (or adjust settings to use SQLite)

## Setup (Docker - recommended)

```bash
git clone https://github.com/JakubD02/solar-calculator-api.git
cd solar-calculator-api
docker-compose up --build
```

Apply database migrations (in a separate terminal, once containers are running):

```bash
docker-compose exec web python manage.py migrate
```

The API will be available at `http://127.0.0.1:8000/`.

## Setup (local, without Docker)

```bash
git clone https://github.com/JakubD02/solar-calculator-api.git
cd solar-calculator-api
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\Activate.ps1
pip install -e ".[dev]"
python manage.py migrate
python manage.py runserver
```

By default this expects a PostgreSQL database; adjust `DATABASES` in `config/settings.py` or set the `DB_*` environment variables to match your local setup.

## API Endpoints

| Method | Endpoint              | Description                                  |
|--------|------------------------|-----------------------------------------------|
| POST   | `/api/calculate/`      | Calculate mounts and joints for panel coordinates, stores the result |
| GET    | `/api/calculations/`   | List all previously stored calculations       |
| GET    | `/api/docs/`            | Interactive Swagger UI documentation           |
| GET    | `/api/redoc/`           | Alternative ReDoc documentation                |

### Example request

```bash
curl -X POST http://127.0.0.1:8000/api/calculate/ \
  -H "Content-Type: application/json" \
  -d '[{"x": 0, "y": 0}, {"x": 45.05, "y": 0}, {"x": 90.1, "y": 0}]'
```

### Example output

```json
{
    "mounts": [
        {"x": 16, "y": 0},
        {"x": 32, "y": 0}
    ],
    "joints": [
        {"x": 44.88, "y": 0},
        {"x": 44.88, "y": 71.1}
    ]
}
```

## Run Tests

With Docker:
```bash
docker-compose exec web pytest
```

Without Docker (inside the activated virtual environment):
```bash
pytest
```

Tests verify:
- input validation,
- rafter generation,
- mount placement rules,
- joint calculation,
- main service flow.

## Linting

```bash
ruff check .
```

## Continuous Integration

Every push and pull request triggers a GitHub Actions workflow that installs dependencies, runs the test suite, and lints the code with ruff.
