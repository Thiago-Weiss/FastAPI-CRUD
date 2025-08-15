import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer


from app.services.utils.database import SessionDB
from app.secret import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from app.models import UserApiOutput, UserDB, Token








def create_access_token(user: UserDB) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    encoded_jwt = jwt.encode({"sub": str(user.id), "exp": expire}, SECRET_KEY, algorithm= ALGORITHM)
    return Token(access_token= encoded_jwt, token_type= "bearer")





oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

def get_current_user_by_token(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: SessionDB
    ) -> UserApiOutput:
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id = int(data.get("sub"))

        if user_id is None:
            raise credentials_exception

    except InvalidTokenError:
        raise credentials_exception

    user = db.get(UserDB, user_id)
    if user is None:
        raise credentials_exception

    return user




CurrentUser = Annotated[UserApiOutput, Depends(get_current_user_by_token)]
