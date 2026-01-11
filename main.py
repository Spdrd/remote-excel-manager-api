from fastapi import FastAPI
from Schemas.request_schema import Register
from Service.excel_service import ExcelService

app = FastAPI()
excel_service = ExcelService()

@app.post("/register")
def register_entry(register: Register):
    excel_service.add_record(register.file_name, register.register)
    return {"mensaje": "Entry registered successfully", "id": register.register_id}

@app.get("/hello world")
def hello_world():
    return {"mensaje": "Hello World"}
