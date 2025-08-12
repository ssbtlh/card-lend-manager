# models.py
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    hashed_password: str

class CardMaster(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    external_id: Optional[str]
    name: str
    set_code: Optional[str]

class UserCollection(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    card_id: int = Field(foreign_key="cardmaster.id")
    quantity: int = 0

class Loan(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="user.id")
    borrower_id: int = Field(foreign_key="user.id")
    card_id: int = Field(foreign_key="cardmaster.id")
    quantity: int
    start_date: date
    due_date: Optional[date]
    returned_date: Optional[date]
    status: str = "active"
