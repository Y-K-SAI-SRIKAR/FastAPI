from pydantic import BaseModel

class Products(BaseModel):
    Id : int
    Name : str
    Desc : str
    Price : float 
    Qty : int


#pydantic is a python library which is used for data Validation in state tranfer and representation.
"""instead of representing the states/data retrieved from server as the boilerplate,
pydantic converts the data into a representational format such as JSON. """

#This Model file is like a entity file. In DataBase Language its like a Table "Products".