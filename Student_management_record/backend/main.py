from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from .database import Base,engine,get_db
from .schemas import RecordCreated,RecordOut
from . import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Student Record Manager Api')

@app.get('/')
def hone():
    return {'message':"Student Record Manager is running"}

@app.post('/records',response_model = RecordOut)
def create(data:RecordCreated,db:Session = Depends(get_db)):
    return crud.create(db,data)

@app.get('/records',response_model = list[RecordOut])
def get_all(db: Session = Depends(get_db)):
    return crud.get_all(db)

@app.get('/records/{record_id}',response_model = RecordOut)
def get_one(record_id:int,db:Session = Depends(get_db)):
    obj = crud.get_one(db,record_id)
    if not obj: raise HTTPException(404,"Record Not Founded")
    return obj

@app.put('/records/{record_id}',response_model = RecordOut)
def update(record_id:int,data : RecordCreated,db: Session=Depends(get_db)):
    obj = crud.update(db,record_id,data)
    if not obj : raise HTTPException(404,"Record Not Founded")
    return obj

@app.delete('/records/{record_id}')
def delete(record_id:int,db:Session = Depends(get_db)):
    if not crud.delete(db,record_id) : raise HTTPException(404,"Record Not Founded")
    return {"message":"Deleted"}