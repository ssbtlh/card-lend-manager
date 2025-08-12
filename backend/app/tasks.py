from sqlmodel import Session, select
from datetime import date
from app.models import Loan
from app.deps import engine

def check_expired_loans():
    with Session(engine) as session:
        loans = session.exec(
            select(Loan).where(Loan.status == "active", Loan.due_date < date.today())
        ).all()
        for loan in loans:
            loan.status = "overdue"
        session.commit()
        if loans:
            print(f"[TASK] {len(loans)} empréstimos vencidos foram atualizados para 'overdue'.")
