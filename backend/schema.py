from pydantic import BaseModel
from typing import Optional

class CreateProductSchema(BaseModel):
    product_name: str
    product_type: str
    product_price: float

class UpdateProductSchema(BaseModel):
    product_name: Optional[str]
    product_type: Optional[str]
    product_price: Optional[float]