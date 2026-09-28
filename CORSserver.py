from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:5173"],
    allow_methods=["*"]
)

@app.get("/")
def home():
    return "Fast API running with CORS Configuration"

"""
CORS means Cross Origin Resource Sharing , which allows the applications to communicate with eachother.

The applications running on the same server can communicate and share resources for completion,
without any deviation.

But, for the applications running on different servers, the sharing origins must be configured to 
establish communication path. so thats why we configure CORS middleware.

"""