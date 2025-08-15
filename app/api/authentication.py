from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated


from app.models import Token
from app.services import gerar_token_usuario, SessionDB


router = APIRouter(tags= ["Authentication"])


@router.post(
        "/login", 
        description= "Rota para gerar o token JWT, que é usado em outras rotas como autenticação", 
        summary="Conseguir token JWT")
def get_token_JWT(
    db: SessionDB,
    credenciais: Annotated[OAuth2PasswordRequestForm, Depends()]
    ) -> Token:

    return gerar_token_usuario(db, credenciais)



