"""This file schemas.py handle the all post request data for e.g: User will see these fields when making post creating"""
from pydantic import BaseModel
from typing import List

class CompanyCreation(BaseModel):
    name : str
    email: str
    password : str


class EmployeeCreation(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode: True