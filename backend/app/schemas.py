from typing import Optional
from datetime import date
from sqlmodel import SQLModel

class UserCreate(SQLModel):
    name: str
    email: str
    password: str

class UserRead(SQLModel):
    id: int
    name: str
    email: str

class CardCreate(SQLModel):
    name: str
    set_code: Optional[str] = None
    rarity: Optional[str] = None
    image_url: Optional[str] = None

class LoanCreate(SQLModel):
    owner_id: int
    borrower_id: int
    card_id: int
    quantity: int
    due_date: Optional[date] = None

class LoanRead(SQLModel):
    id: int
    owner_id: int
    borrower_id: int
    card_id: int
    quantity: int
    start_date: date
    due_date: Optional[date]
    status: str
