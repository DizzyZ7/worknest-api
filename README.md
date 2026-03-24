# WorkNest API (Skeleton)

This is a minimal skeleton for the WorkNest API project using FastAPI. It includes:

- **FastAPI** application (`app/main.py`)
- **Dockerfile** to build a container
- **docker-compose.yml** to run the service
- **requirements.txt** for Python dependencies

Run the API locally with:

```bash
uvicorn app.main:app --reload
```

Or build and run with Docker:

```bash
docker-compose up --build
```

Visit `http://localhost:8000` for the root endpoint and `http://localhost:8000/health` for a healthcheck.
