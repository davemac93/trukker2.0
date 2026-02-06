from typing import List

from pydantic import BaseModel, EmailStr

class SignUp(BaseModel):
    email: EmailStr
    password: str

class SignIn(BaseModel):
    email: EmailStr
    password: str

class SelectRole(BaseModel):
    role: str

class DriverProfile(BaseModel):
    first_name: str
    last_name: str 
    phone: str
    license: List[str]

class CompanyProfile(BaseModel):
    company_name: str
    phone: str

