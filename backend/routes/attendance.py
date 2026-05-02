from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User, Attendance
from ai.train import get_embedding
from ai.recognize import find_match
from datetime import datetime
import os

router = APIRouter(prefix="/attendance", tags=["Attendance"])

@router.post("/recognize")
async def recognize(
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

    users = db.query(User).all()
    matched_user = find_match(embedding, users)

    if not matched_user:
        return {"message": "Unknown user"}

    now = datetime.now()

    # 🚨 Prevent duplicate attendance
    existing = db.query(Attendance).filter(
        Attendance.user_id == matched_user.id,
        Attendance.date == now.date()
    ).first()

    if existing:
        return {
            "message": "Already marked today",
            "user": matched_user.name
        }

    attendance = Attendance(
        user_id=matched_user.id,
        date=now.date(),
        time=now.time(),
        status="Present"
    )

    db.add(attendance)
    db.commit()

    return {
        "message": "Attendance marked",
        "user": matched_user.name
    }