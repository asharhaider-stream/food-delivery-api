from pydantic import BaseModel

# Base with common fields
class UserBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str


class UserCreate(UserBase):
    pass

# For response (adds id)
class UserResponse(UserBase):
    id: int
    
    class Config:
        from_attributes = True