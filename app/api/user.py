from fastapi import APIRouter, Path, status
from typing import Annotated

from app.services import SessionDB, create_user, get_user_data

from app.models import UserApiCreate, UserApiOutput, UserApiOutputBlogs


router = APIRouter(prefix="/user", tags= ["User"])


@router.post("/", status_code= status.HTTP_201_CREATED)
def post_create_user(db: SessionDB, user: UserApiCreate,) -> UserApiOutput:
    return create_user(db, user)



@router.get("/{id}")
def get_user(id: Annotated[int, Path(ge= 0)], db: SessionDB) -> UserApiOutputBlogs:
    return get_user_data(id, db)

