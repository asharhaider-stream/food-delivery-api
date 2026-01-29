from fastapi import APIRouter, Depends
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