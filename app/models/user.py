from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr


 

class UserBase(SQLModel):
    name: str
    email: EmailStr = Field(index= True, nullable=False)
 

class UserApiCreate(UserBase):
    password: str


class UserDB(UserBase, table= True):
    id: Optional[int] = Field(default=None, primary_key= True)
    password_hash: str
    blogs: list["BlogDB"] = Relationship(back_populates="autor") 


class UserApiOutput(UserBase):
    id:int

class UserApiOutputBlogs(UserApiOutput):
    blogs: list["BlogApiOutput"] = []


from app.models.blog import BlogDB, BlogApiOutput


