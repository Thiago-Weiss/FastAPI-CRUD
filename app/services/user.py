from fastapi import HTTPException, status
from app.services import SessionDB, Hash
from app.models import UserApiCreate, UserDB, UserApiOutput, UserApiOutputBlogs


def create_user(db: SessionDB, user: UserApiCreate) -> UserApiOutput:
    new_user = UserDB(
        name= user.name,
        email= user.email,
        password_hash= Hash.bcrypt(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def get_user_data(id: int, db: SessionDB) -> UserApiOutputBlogs:
    user = db.get(UserDB, id)
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

