from fastapi import HTTPException, status
from sqlmodel import select
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from app.models import UserDB
from app.services.utils.hashing import Hash



def autenticar_credenciais(db: Session, credenciais : OAuth2PasswordRequestForm) -> UserDB:
    usuario = db.exec(select(UserDB).where(UserDB.email == credenciais.username)).first()
    if not usuario:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "Username não cadastrado")

    if not Hash.verify(credenciais.password, usuario.password_hash):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "Senha errada")
    
    return usuario