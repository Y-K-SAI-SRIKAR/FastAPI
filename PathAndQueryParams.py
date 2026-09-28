from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:5173"],
    allow_methods=["*"]
)

@app.get("/")
def home():
    return "Path and Query Params Demonstration"

@app.get("/path/{id}")
def path_param(id:int):
    return f"My Roll Number is : {id}"


@app.get("/query")
def query_param(request:Request):
    query_params = dict(request.query_params)
    return f"Hi, my name is {query_params.get('name')} and I am a {query_params.get('role')}"

"""
Parameters are the input or output units which can be provided from frontend or backend.

In Path Parameters, usually used to retrieve the states from DB or Model and to display on the Frontend.
Path Parameters are directly injected in the URL or endpoint of the api method that has been called.

In Query Parameters, usually used to capture the states from frontend and transferred to the backend.
Query parameters can not be injected like path parameters, they have a specific syntax to operate.

That is: {endpoint}/?q={field1}={value1}&{field2}={value2}&.....{filed n}={value n}. which is a complex process and 
may increase the load on the api call and could effect the state transferring.

To avoid this in Query parameters, we use "Request" which is nothing but a api call, but by creating an object for that query.
The object will look alike: INFO: 127.0.0.1:60204 - "GET /query?name=srikar&role=AIEngineer HTTP/1.1" 200 OK
In the above query_param module, I have mentioned request of Type Request which creates a object and then converts the query to 
key-value pair following JSON structure.

"""