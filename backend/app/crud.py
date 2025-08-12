from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.deps import get_session, get_current_user
from app.models import User, CardMaster, UserCollection, Loan
from app.schemas import CardCreate, LoanCreate, LoanRead
from datetime import date

router = APIRouter()

@router.post("/cards")
def create_card(card: CardCreate, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    db_card = CardMaster.from_orm(card)
    session.add(db_card)
    session.commit()
    session.refresh(db_card)
    return db_card

@router.post("/loans", response_model=LoanRead)
def create_loan(loan: LoanCreate, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    # Verifica se dono tem carta
    collection = session.exec(
        select(UserCollection).where(
            UserCollection.user_id == loan.owner_id,
            UserCollection.card_id == loan.card_id
        )
    ).first()
    if not collection or collection.quantity < loan.quantity:
        raise HTTPException(status_code=400, detail="Quantidade indisponível")

    db_loan = Loan(
        owner_id=loan.owner_id,
        borrower_id=loan.borrower_id,
        card_id=loan.card_id,
        quantity=loan.quantity,
        start_date=date.today(),
        due_date=loan.due_date
    )
    session.add(db_loan)
    session.commit()
    session.refresh(db_loan)
    return db_loan
