from typing import Optional
from sqlmodel import SQLModel, Field, Relationship




class BlogBase(SQLModel):
    title: str
    content: str

class BlogApiCreate(BlogBase):
    pass


class BlogApiUpdate(BlogApiCreate):
    title : Optional[str] = None
    content : Optional[str] = None


class BlogApiOutput(BlogBase):
    id: int

class BlogApiOutputAutor(BlogApiOutput):
    autor: Optional["UserApiOutput"]


class BlogDB(BlogBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    autor_id: Optional[int] = Field(default=None, foreign_key="userdb.id") 
    autor: Optional["UserDB"] = Relationship(back_populates="blogs")


from app.models.user import UserDB, UserApiOutput


