import numpy as np
import json

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def find_match(input_embedding, users, threshold=0.5):
    best_user = None
    best_score = 0

    for user in users:
        db_embedding = np.array(json.loads(user.embedding))
        score = cosine_similarity(input_embedding, db_embedding)

        if score > best_score:
            best_score = score
            best_user = user

    if best_score > threshold:
        return best_user

    return None