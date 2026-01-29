from pydantic import BaseModel

class MenuItemBase(BaseModel):
    name: str
    price: float
    description: str
    is_available: bool
    restaurant_id: int

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemResponse(MenuItemBase):
    id : int

    class Config:
        from_attributes = True        