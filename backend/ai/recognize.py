import numpy as np

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def recognize_face(embedding, db_users, threshold=0.5):
    best_match = None
    best_score = 0

    for user in db_users:
        db_embedding = np.array(eval(user.embedding))
        score = cosine_similarity(embedding, db_embedding)

        if score > best_score:
            best_score = score
            best_match = user

    if best_score > threshold:
        return best_match

    return None