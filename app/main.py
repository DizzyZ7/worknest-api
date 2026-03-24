from fastapi import FastAPI

app = FastAPI(title="WorkNest API")

@app.get("/")
def read_root():
    return {"message": "Welcome to WorkNest API"}

@app.get("/health")
def healthcheck():
    return {"status": "ok"}
