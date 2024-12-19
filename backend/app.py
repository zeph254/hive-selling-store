from fastapi import FastApi

app = FastApi()

@app.get("/")
def index():
    return {"message":"Welcome to Hive!"}

@app.get("/products")
def products():
    return []

@app.post("/products")
def add_product():
    return{"message":"product added successfully"}

@app.get("/products/{product_id}")
def get_products(product_id: int):
    print(product_id)
    return{"message":"product retrived successfully"}

   

@app.patch("/products/{product_id}")
def update_products(product_id :int):
    print(product_id)
    return{"message":"product updated successfully"}

@app.delete("/products/{products_id}")
def delete_products(product_id :int):
    print(product_id)
    return{"message":"product deleted successfully"}