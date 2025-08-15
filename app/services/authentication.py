from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from .utils import create_access_token, autenticar_credenciais


def gerar_token_usuario(db: Session, credenciais : OAuth2PasswordRequestForm):
    usuario = autenticar_credenciais(db, credenciais)
    return create_access_token(usuario)