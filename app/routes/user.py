from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse

router = APIRouter()

@router.post("/", response_model = UserResponse)
def create_user(user:  UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        name=user.name,
        email=user.email,
        phone = user.phone,
        address = user.address
    )

    db.add(db_user) #Addtodb

    db.commit() #commit

    db.refresh(db_user)

    return db_user

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):        
    return db.query(User).filter(User.id == user_id).first()

@router.put("/{user_id}", response_model=UserResponse)    
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.id == user_id).first()

    # Step B: Check if exists
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.name = user.name    
    db_user.email = user.email
    db_user.phone = user.phone
    db_user.address = user.address

    db.commit()

    db.refresh(db_user)

    return db_user

@router.delete('/{user_id}')
def delete_user(user_id: int, db:  Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user is None:
        raise HTTPException(status_code=404,  detail ="User not Found")

    db.delete(db_user)
    db.commit()

    return{"message": "User deleted Successfully"}        
