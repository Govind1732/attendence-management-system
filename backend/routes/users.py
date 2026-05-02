from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User
from ai.train import get_embedding
import json
import os

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
async def register_user(
    name: str = Form(...),
    email: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    os.makedirs("temp", exist_ok=True)
    file_path = f"temp/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    embedding = get_embedding(file_path)

    if embedding is None:
        return {"error": "No face detected"}

    # Check duplicate email
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        return {"error": "User already exists"}

    user = User(
        name=name,
        email=email,
        embedding=json.dumps(embedding)
    )

    db.add(user)
    db.commit()

    return {"message": "User registered successfully"}