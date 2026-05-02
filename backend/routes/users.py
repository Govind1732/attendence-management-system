from fastapi import APIRouter, UploadFile, File
from database import SessionLocal
from models import User
from ai.train import get_embedding

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register")
async def register_user(name: str, email: str, file: UploadFile = File(...)):
    db = SessionLocal()

    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    embedding = get_embedding(file_path)

    if embedding is None:
        return {"error": "Face not detected"}

    user = User(
        name=name,
        email=email,
        embedding=str(embedding)
    )

    db.add(user)
    db.commit()

    return {"message": "User registered"}