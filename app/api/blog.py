from fastapi import APIRouter, Query, Path, status
from typing import Annotated


from app.services import SessionDB, CurrentUser, create_blog, get_all_user_blogs, get_user_blog, update_user_blog, delete_user_blog
from app.models import BlogApiCreate, BlogApiOutput, BlogApiUpdate, BlogApiOutputAutor



router = APIRouter(prefix= ("/post"), tags=["Blog"])


@router.post("/", status_code= status.HTTP_201_CREATED, summary= "Criar um blog desse usuario")
def post_create_blog(user: CurrentUser, blog: BlogApiCreate, db: SessionDB) -> BlogApiOutput:
    return create_blog(user, blog, db)



@router.get("/", summary= "Pega todos os blogs do usuario")
def get_all_blogs(user: CurrentUser, db: SessionDB, offset: Annotated[int, Query(ge=0)] = 0, limit: Annotated[int, Query(le=100)] = 100) -> list[BlogApiOutputAutor]:
    return get_all_user_blogs(user, db, offset, limit)



@router.get("/{id}", summary= "Pega *um* blog do usario")
def get_blog(user: CurrentUser, db: SessionDB, id: Annotated[int, Path(ge= 0)]) -> BlogApiOutputAutor:
    return get_user_blog(user, db, id)



@router.patch("/{id}", status_code= status.HTTP_202_ACCEPTED, summary= "Atualiza o blog do usuario")
def update_blog(user: CurrentUser, db: SessionDB, id: Annotated[int, Path(ge=0)], blog_update : BlogApiUpdate) -> BlogApiOutput:
    return update_user_blog(user, db, id, blog_update)
    

    
@router.delete("/{id}", status_code= status.HTTP_204_NO_CONTENT, summary= "Deleta o blog do usuario")
async def delete_blog(user: CurrentUser, db: SessionDB, id: Annotated[int, Path(ge= 0)]):
    delete_user_blog(user, db, id)
