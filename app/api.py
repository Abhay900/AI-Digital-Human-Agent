from fastapi import FastAPI

app = FastAPI(
    title="AI Digital Human Agent",
    version="0.1.0",
)


@app.get("/")
def health_check():
    return {
        "status": "online",
        "message": "AI Digital Human Agent API is running",
    }