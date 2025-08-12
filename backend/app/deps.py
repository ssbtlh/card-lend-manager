from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, create_engine
from jose import jwt, JWTError
from app.models import User

DATABASE_URL = "postgresql://pguser:pgpass@db:5432/cardlend"
engine = create_engine(DATABASE_URL, echo=True)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

SECRET_KEY = "troque_essa_chave"
ALGORITHM = "HS256"

def get_session():
    with Session(engine) as session:
        yield session

def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    user = session.get(User, int(user_id))
    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return user
