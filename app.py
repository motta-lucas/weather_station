from fastapi import FastAPI
from datetime import datetime
from pathlib import Path
import json

app = FastAPI()

DATA_FILE = Path("sensor_data.jsonl")


@app.post("/sensors")
def receive_sensor_data(data: dict):
    record = {
        "timestamp": datetime.now().astimezone().isoformat(),
        "data": data,
    }

    with DATA_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record) + "\n")

    return {"status": "success"}
