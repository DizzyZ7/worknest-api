# WorkNest API

Production-ready FastAPI service with incidents module, PostgreSQL-ready database wiring, Docker support, and a single canonical launch path.

## Stack
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Docker / Docker Compose
- Pytest

## Project run (local)
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Project run (production-like)
```bash
docker-compose -f docker-compose.prod.yml up --build
```

## API
- `GET /health`
- `GET /api/v1/info`
- `GET /api/v1/incidents`
- `POST /api/v1/incidents`

## Environment
Main environment variable:
- `DATABASE_URL`

Example for docker compose:
```env
DATABASE_URL=postgresql://worknest:worknest@db:5432/worknest
```

## Notes
- `app/main.py` is the only application entrypoint.
- `requirements.txt` is the only dependency file.
- `README.md` is the only project readme.
