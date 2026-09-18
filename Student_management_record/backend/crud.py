from sqlalchemy.orm import Session
from model import Record
from schemas import RecordCreated

def create(db : Session ,data: RecordCreated):
    obj =  Record(name = data.name,email=data.email,age = data.age,department = data.department)
    db.add(obj);db.commit();db.refresh(obj)
    return obj

def get_all(db: Session):
    return db.query(Record).order_by(Record.id.desc()).all()

def get_one(db: Session,record_id:int):
    return db.query(Record).filter(Record.id == record_id).first()

def update(db:Session,record_id:int,data:RecordCreated):
    obj = get_one(db,record_id)
    if not obj : return None
    obj.name = data.name
    obj.email = data.email
    obj.age = data.age
    obj.department = data.department
    db.commit();db.refresh(obj)
    return obj

def delete(db:Session,record_id:int):
    print("DELETE ID RECEIVED:", record_id)
    obj = get_one(db,record_id)
    print("OBJECT FOUND:", obj)
    if not obj: return False
    db.delete(obj);db.commit()
    return True