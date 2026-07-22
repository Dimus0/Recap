from app.db.session import Base, engine
from app.db.session import Base
from sqlalchemy import text

def init_db():
    with engine.connect() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector;"))
        connection.commit()
        print("✅ Розширення pgvector активовано.")

    Base.metadata.create_python = Base.metadata.create_all(bind=engine)
    print("✅ Усі таблиці успішно створені в БД!")

if __name__ == "__main__":
    init_db()