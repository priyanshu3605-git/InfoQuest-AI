from infoquest.database.connection import Base, engine
from infoquest.database.models import DocumentModel, ChunkModel

# Create any missing database tables
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")