from fastapi import FastAPI

from app.api import auth, users
from app.core.database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)

@app.get("/")
def root():
    return "Backend is running"


