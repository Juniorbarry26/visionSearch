from fastapi import FastAPI

app = FastAPI(
    title="VisionSearch API",
    description="Backend API for VisionSearch",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "VisionSearch API is running"
    }