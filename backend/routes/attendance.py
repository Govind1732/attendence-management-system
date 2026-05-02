from fastapi import APIRouter, UploadFile, File
from database import SessionLocal
from models import Attendance, User
from datetime import datetime
import cv2
from insightface.app import FaceAnalysis
from ai.recognize import recognize_face

router = APIRouter(prefix="/attendance", tags=["Attendance"])

face_app = FaceAnalysis()
face_app.prepare(ctx_id=0)

@router.post("/mark")
async def mark_attendance(file: UploadFile = File(...)):
    db = SessionLocal()

    file_path = f"temp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    img = cv2.imread(file_path)
    faces = face_app.get(img)

    if not faces:
        return {"error": "No face detected"}

    embedding = faces[0].embedding

    users = db.query(User).all()

    matched_user = recognize_face(embedding, users)

    if not matched_user:
        return {"message": "Unknown user"}

    now = datetime.now()

    attendance = Attendance(
        user_id=matched_user.id,
        date=now.date(),
        time=now.time(),
        status="Present"
    )

    db.add(attendance)
    db.commit()

    return {"message": f"Attendance marked for {matched_user.name}"}