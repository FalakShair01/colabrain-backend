"""This file schemas.py handle the all post request data for e.g: User will see these fields when making post creating"""
from pydantic import BaseModel
from typing import List

class CompanyCreation(BaseModel):
    username : str
    company_name : str
    email: str
    password : str


class EmployeeCreation(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode: True


class Login(BaseModel):
    email: str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None