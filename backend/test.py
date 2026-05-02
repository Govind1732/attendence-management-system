from insightface.app import FaceAnalysis
import cv2
import os

app = FaceAnalysis()
app.prepare(ctx_id=0)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR, "test.jpg")

img = cv2.imread(img_path)

if img is None:
    raise Exception("Image not found")

faces = app.get(img)

print("Faces detected:", len(faces))