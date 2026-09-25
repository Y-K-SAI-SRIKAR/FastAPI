from fastapi import FastAPI
from data import products
from model import Products

app = FastAPI()

@app.get("/")
def health():
    return "FetchAll method is running"

@app.get("/products")
def get_all_prods():
    return products

@app.get("/products/{Id}")
def get_by_id(Id:int):
    for product in products:
        if product.Id == Id:
            return product
    return "Product Not Found"

@app.post("/add")
def add_product(product:Products):
    products.append(product)
    return product