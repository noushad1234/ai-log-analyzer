main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Your FastAPI AI Log Analyzer is running!"}
