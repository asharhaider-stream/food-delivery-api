from fastapi import FastAPI
from app.database import Base, engine
from app.models import User, Restaurant, MenuItem, Order, OrderItem
from app.routes import user 

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Connect user router
app.include_router(user.router, prefix="/users", tags=["Users"])  

@app.get('/')
def greet():
    return {'message': 'Welcome to Food Delivery API'}