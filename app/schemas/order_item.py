from pydantic import BaseModel

# Base with common fields
class OrderItemBase(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int
    price_at_order: float

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemResponse(OrderItemBase):
    id: int        

    class Config:
        from_attributes = True
