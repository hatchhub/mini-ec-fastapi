from sqlmodel import SQLModel, Field
from typing import Optional 

class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    price: int
    description: Optional[str] = None
