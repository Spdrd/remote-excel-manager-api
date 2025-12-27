from pydantic import BaseModel

class Register(BaseModel):
    register_id: int
    file_name: str
    register: dict

    def get_column_names(self):
        return list(self.register.keys())