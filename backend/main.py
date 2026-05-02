from fastapi import FastAPI
from database import engine, Base
from routes import users, attendance, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(attendance.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Attendance API running"}