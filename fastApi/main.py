from os import name
from fastapi import status
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Sample dataset with id, name, and risk_score
customers = [
    {"id": 101, "name": "Rahul Sharma", "risk_score": 15.5},
    {"id": 102, "name": "Priya Verma", "risk_score": 82.0},
    {"id": 103, "name": "Amit Patel", "risk_score": 45.2},
    {"id": 104, "name": "Neha Gupta", "risk_score": 90.8},
    {"id": 105, "name": "Vikas Singh", "risk_score": 12.3}
]

@app.get("/")
def homePage():
    return {
        "message":"this is the home page"
    }

@app.get("/risk_score")
def risk_score():
    high_risk = []
    for customer in customers:
        if customer["risk_score"]>50:
            high_risk.append(customer)
    return{
        "message":f"the high risk custormer is {high_risk}"
    }
    raise HTTPException(status_code=404,detail="there are no high risk custormer")

@app.get("/filter-risk")
def filter_risk(min_score: float):
    min_scoree = []
    for risk in customers:
        if risk["risk_score"] >= min_score:
            min_scoree.append(risk)
    return {
        "filtered_customers": min_scoree
    }

@app.get("/userid/{users}")
def userDetails(users: int):
    for user in customers:
        if user["id"] == users:
            return user

    # Loop khatam hone ke baad agar koi match nahi mila tab return karein
    return {"error": "user not found"}


@app.get("/query_parameter")
def query_parameter(age: int):
    return {
        "user_age": age
    }
