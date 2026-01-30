from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Restaurant
from app.schemas import RestaurantCreate, RestaurantResponse
router = APIRouter()

@router.post("/", response_model = RestaurantResponse)
def create_restaurant(restaurant:  RestaurantCreate, db: Session = Depends(get_db)):
    db_restaurant = Restaurant(
        name=restaurant.name,
        address=restaurant.address,
        cuisine_type = restaurant.cuisine_type,
        is_open = restaurant.is_open
    )

    db.add(db_restaurant) #Addtodb

    db.commit() #commit

    db.refresh(db_restaurant)

    return db_restaurant

@router.get("/")
def get_restaurants(db: Session = Depends(get_db)):
    return db.query(Restaurant).all()

@router.get("/{restaurant_id}")
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):        
    return db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

@router.put("/{restaurant_id}", response_model=RestaurantResponse)    
def update_restaurant(restaurant_id: int, restaurant: RestaurantCreate, db: Session = Depends(get_db)):

    db_restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

    # Step B: Check if exists
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    db_restaurant.name = restaurant.name    
    db_restaurant.address = restaurant.address      
    db_restaurant.cuisine_type = restaurant.cuisine_type 
    db_restaurant.is_open = restaurant.is_open  

    db.commit()

    db.refresh(db_restaurant)

    return db_restaurant

@router.delete('/{restaurant_id}')
def delete_restaurant(restaurant_id: int, db:  Session = Depends(get_db)):
    db_restaurant = db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

    if db_restaurant is None:
        raise HTTPException(status_code=404,  detail ="Restaurant not Found")

    db.delete(db_restaurant)
    db.commit()

    return{"message": "Restaurant deleted Successfully"}        
