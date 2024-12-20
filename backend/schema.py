from pydantic import BaseModel


class CreateProductSchema(BaseModel):
    Product_name: str
    Product_type: str
    Product_price: float