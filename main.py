from fastapi import FastAPI
from Schemas.request_schema import Register

app = FastAPI()

@app.post("/register")
def register_entry(register: Register):
    return {"mensaje": "Entry registered successfully", "id": register.register_id}

@app.get("/hello world")
def hello_world():
    return {"mensaje": "Hello World"}
