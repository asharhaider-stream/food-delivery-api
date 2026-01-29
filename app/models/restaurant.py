from sqlalchemy import Integer, String, Column, Boolean 
from app.database import Base

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer,  primary_key= True, index = True)
    name = Column(String)
    address = Column(String)
    cuisine_type = Column(String)
    is_open = Column(Boolean)