from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Admin.Router import Adminroutes

app = FastAPI(title="MVC APP")

app.add_middleware(CORSMiddleware,
                   allow_origins=["https://localhost:5173"],
                   allow_methods=["*"]
                   )

app.include_router(Adminroutes)

@app.get("/")
def greet():
    return "Welcome to TaskManager APP"


#Here we are importing endpoints from a router instead of declaring the routes in main function.