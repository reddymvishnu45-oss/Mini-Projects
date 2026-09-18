from sqlalchemy import Column,Integer,String,Float,Boolean,Date
from database import Base

class Record(Base):
    __tablename__ = 'student'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String, nullable = False)
    email = Column(String ,nullable=False)
    age = Column(Integer,nullable=True)
    department = Column(String,nullable=True)