from fastapi import FastAPI
from data import products
from model import Products

app = FastAPI()

@app.get("/")
def health():
    return "Server is running"

@app.get("/products/all")
def get_all_prods():
    return products

@app.get("/products/{Id}")
def get_by_id(Id:int):
    for product in products:
        if product.Id == Id:
            return product
    return "Product Not Found"

@app.post("/products/add")
def add_product(product:Products):
    products.append(product)
    return product

@app.put("/products/update")
def update_product(Id:int, product:Products):
    for i in range(len(products)):
        if products[i].Id == Id:
            products[i] = product
            return "Product Updated Successfully"
    return "No such product exists"

@app.delete("/products/delete")
def delete_product(Id:int):
    for i in range(len(products)):
        if products[i].Id == Id:
            products.pop(i)
            return "Product removed Successfully"
    return "No such Product Exists"