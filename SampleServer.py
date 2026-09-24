from fastapi import FastAPI

app = FastAPI() #creating an object of FastAPI to expose the Application to Internet.

@app.get("/greet") #enables the endpoint to access the state from the server.
def greet():
    return "Hello From Sample Server"



#To Run this use, uvicorn SampleServer:app --reload and in the browser use, localhost:8000/greet.
#Here, uvicorn is a server side framework which establishes the connection between the app in server and Client
# SampleServer is the Object file of the Application.
# app is the object of FastAPI
# --reload refreshes the server before initiating the Application to avoid data/state management problems. 
