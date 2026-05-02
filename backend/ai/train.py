import cv2
from insightface.app import FaceAnalysis
import numpy as np

face_app = FaceAnalysis()
face_app.prepare(ctx_id=0)

def get_embedding(image_path):
    img = cv2.imread(image_path)
    faces = face_app.get(img)

    if not faces:
        return None

    return faces[0].embedding.tolist()