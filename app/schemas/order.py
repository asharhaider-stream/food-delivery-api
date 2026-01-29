from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    user_id: int
    restaurant_id: int
    total_amount: float
    status: str

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    created_at: datetime     

    class Config:
        from_attributes = True