from infoquest.database.connection import engine, Base
from infoquest.database.models import DocumentModel


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")


if __name__ == "__main__":
    init_db()