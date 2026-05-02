from fastapi import FastAPI
from database import engine, Base
from routes import users, attendance, auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(attendance.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Attendance API running"}