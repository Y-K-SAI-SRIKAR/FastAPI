from fastapi import FastAPI
from data import products

app = FastAPI()

@app.get("/")
def health():
    return "FetchAll method is running"

@app.get("/products")
def get_all_prods():
    return products