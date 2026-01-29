from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key= True, index = True)
    user_id = Column(Integer, ForeignKey("users.id"))         # ForeignKey to users.id
    restaurant_id = Column(Integer, ForeignKey("restaurants.id")) 
    total_amount = Column(Float)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)