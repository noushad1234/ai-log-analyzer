from fastapi import FastAPI, File, UploadFile
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Your FastAPI AI Log Analyzer is running!"}

@app.post("/upload-log/")
async def upload_log(file: UploadFile = File(...)):
    # Read the file content
    content = await file.read()
    text = content.decode("utf-8")

    # Split lines and prepare list for cleaned data
    cleaned_data = []
    lines = text.strip().split("\n")

    # Define regex pattern to extract data
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) User=(\S+) IP=(\S+) Event=(\S+)"

    for line in lines:
        match = re.search(pattern, line)
        if match:
            timestamp, user, ip, event = match.groups()
            cleaned_data.append({
                "timestamp": timestamp,
                "user": user,
                "ip": ip,
                "event": event
            })

    return {"parsed_logs": cleaned_data}
