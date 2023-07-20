from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import models, schemas
from hashPassword import Hash
from database import get_db

from sqlalchemy.orm import Session



router = APIRouter(
    prefix="/organization",
    tags=["Organization"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def company_register(request:schemas.CompanyCreation, db: Session=Depends(get_db)):
    """This function is Used for comapany Registeration"""
    company = models.Company(username=request.username,company_name=request.company_name, email=request.email, password=Hash.get_password_hash(request.password))
    db.add(company)
    db.commit()
    db.refresh(company)
    return "Register Successfully"


@router.post("/employee-register", status_code=status.HTTP_201_CREATED)
async def employee_register(request:schemas.EmployeeCreation, db:Session=Depends(get_db)):
    """This function is Used for comapany Registeration"""
    employee = models.Employee(username=request.username, email=request.email, password=Hash.get_password_hash(request.password), company_id=1)
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return "Employee Created Successfully"


@router.get("/companies", status_code=status.HTTP_200_OK)
async def get_all_companies(db:Session=Depends(get_db)):
    """Get All Registered Companies"""
    companies = db.query(models.Company).all()
    return companies
    

@router.get("/employees", status_code=status.HTTP_200_OK)
async def get_all_employees(db:Session=Depends(get_db)):
    """Get All Employess within a Orangization"""
    employees = db.query(models.Employee).all()
    return employees


