from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

# 1. Define the blueprint for APIs
class Numbers(BaseModel):
    x: int
    y: int

# 2. Create the API endpoint
@app.post("/add")
def add_numbers_api(numbers: Numbers):
    return {"result": add_numbers(numbers.x, numbers.y)}


def add_numbers(x, y):
    return x + y