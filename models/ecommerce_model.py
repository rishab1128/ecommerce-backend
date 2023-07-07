from pydantic import BaseModel
from datetime import datetime
from typing import List


class Product(BaseModel):
    Name: str
    Price: int
    Qty: int

class UserAddress(BaseModel):
    city: str
    country: str
    zip_code: str

class Item(BaseModel):
    product_id: int
    bought_quantity: int


class Order(BaseModel):
    timestamp: datetime = datetime.now()
    items: List[Item] = []
    total_amount: float
    user_address: UserAddress

