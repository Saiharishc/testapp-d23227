from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/api/ping")
def ping():
    return {"message": "pong"}

@app.get("/")
def serve_index():
    return FileResponse("index.html")
