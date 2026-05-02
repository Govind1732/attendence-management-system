from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

DATABASE_URL = "mysql+pymysql://root:Loki%40132@localhost:3306/attendance_system"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 👇 ADD THIS
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()