from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Router import routes

app = FastAPI(title="MVC APP")

app.add_middleware(CORSMiddleware,
                   allow_origins=["https://localhost:5173"],
                   allow_methods=["*"]
                   )

app.include_router(routes)


#Here we are importing endpoints from a router instead of declaring the routes in main function.