from fastapi import FastAPI

app = FastAPI(
    title="AI BlogNest API",
    description="A simple AI-powered Blog Management API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI BlogNest API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }