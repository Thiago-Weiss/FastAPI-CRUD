from pydantic import BaseModel, EmailStr




class Login(BaseModel):
    username: EmailStr
    password: str
 

