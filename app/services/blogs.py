from fastapi import HTTPException, status
from sqlmodel import select

from app.services import SessionDB
from app.models import UserApiOutput, BlogApiCreate, BlogApiOutput, BlogDB, BlogApiUpdate, BlogApiOutputAutor




def create_blog(user: UserApiOutput, blog: BlogApiCreate, db: SessionDB) -> BlogApiOutput:
    db_blog = BlogDB.model_validate(blog)
    db_blog.autor_id = user.id
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog



def get_all_user_blogs(user: UserApiOutput, db: SessionDB, offset: int, limit: int) -> list[BlogApiOutputAutor]:
    return db.exec(select(BlogDB).where(BlogDB.autor_id == user.id).offset(offset).limit(limit)).all()



def get_user_blog(user: UserApiOutput, db: SessionDB, id: int) -> BlogApiOutputAutor:
    blog = db.get(BlogDB, id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    if blog.autor_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="This Blog is not from this user")
    
    return blog



def update_user_blog(user: UserApiOutput, db: SessionDB, id: int, blog_update : BlogApiUpdate) -> BlogApiOutput:
    blog_db = db.get(BlogDB, id)
    if not blog_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    if blog_db.autor_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="This Blog is not from this user")
    
    blog_new = blog_update.model_dump(exclude_unset= True)
    blog_db.sqlmodel_update(blog_new)
    db.add(blog_db)
    db.commit()
    db.refresh(blog_db)
    return blog_db
    


def delete_user_blog(user: UserApiOutput, db: SessionDB, id: int):
    blog = db.get(BlogDB, id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    
    if not blog.autor_id == user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="This Blog is not from this user")
    
    db.delete(blog)
    db.commit()


