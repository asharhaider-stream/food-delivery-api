from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from app.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"
    
    id = Column(Integer, primary_key= True, index = True)
    name = Column(String)
    price = Column(Float)  # Use Float
    description = Column(String)
    is_available = Column(Boolean)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"))  # ForeignKey to restaurants.id