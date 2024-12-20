from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import get_db, Product
from schema import CreateProductSchema


app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'])

@app.get("/")
def index():
    return {"message":"Welcome to Hive!"}

@app.get("/products")
def products(session:Session = Depends(get_db)):from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import get_db, Product
from schema import CreateProductSchema

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'])

@app.get("/")
def index():
    return {"message": "Welcome to Hive!"}

@app.get("/products")
def products(session: Session = Depends(get_db)):
    products = session.query(Product).all()
    return []

@app.post("/products")
def add_product(product_data: CreateProductSchema, session: Session = Depends(get_db)):
    new_product = Product(**product_data.model_dump())
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return {"message": "Product added successfully", "product": new_product}

@app.get("/products/{product_id}")
def get_product(product_id: int, session: Session = Depends(get_db)):
    print(product_id)
    product = session.query(Product).get(product_id)
    if product:
        return {"message": f"Product {product_id} retrieved successfully", "product": product}
    else:
        return {"message": f"Product {product_id} not found"}

@app.patch("/products/{product_id}")
def update_product(product_id: int, session: Session = Depends(get_db)):
    print(product_id)
    product = session.query(Product).get(product_id)
    if product:
        # Update the product data here
        session.commit()
        return {"message": f"Product {product_id} updated successfully"}
    else:
        return {"message": f"Product {product_id} not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int, session: Session = Depends(get_db)):
    print(product_id)
    product = session.query(Product).get(product_id)
    if product:
        session.delete(product)
        session.commit()
        return {"message": f"Product {product_id} deleted successfully"}
    else:
        return {"message": f"Product {product_id} not found"}
    products = session.query(Product).all()
    return []

@app.post("/products")
def add_product(Product:CreateProductSchema,session:Session = Depends(get_db)):
    new_product = Product(**Product.model_dump())
    session.add(new_product)
    session.commit()
    session.refresh(new_product)
    return{"message":"Product added successfully", "product": new_product }

@app.get("/products/{product_id}")
def get_products(product_id: int):
    print(product_id)
    return{"message":f"Product {product_id} retrived successfully"}

   

@app.patch("/products/{product_id}")
def update_products(product_id :int):
    print(product_id)
    return{"message":"Product updated successfully"}

@app.delete("/products/{products_id}")
def delete_products(product_id :int):
    print(product_id)
    return{"message":"Product deleted successfully"}