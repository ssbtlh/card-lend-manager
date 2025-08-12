from fastapi import FastAPI
from sqlmodel import SQLModel
from app.deps import engine
from app import tasks
from apscheduler.schedulers.background import BackgroundScheduler

from app import auth, crud

app = FastAPI(title="Card Lending API")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
    scheduler = BackgroundScheduler()
    scheduler.add_job(tasks.check_expired_loans, "interval", hours=1)
    scheduler.start()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(crud.router, tags=["CRUD"])
