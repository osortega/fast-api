from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/time") 
def get_time():
    return {"time": datetime.now()}