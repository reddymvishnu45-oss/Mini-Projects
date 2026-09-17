from pydantic import BaseModel

class RecordCreated(BaseModel):
    name : str
    email : str
    age : int | None = None
    department : str = None

class RecordOut(RecordCreated):
    id : int
    class Config:
        from_attributes = True