from sqlalchemy import inspect, text
from infoquest.database.connection import engine


inspector = inspect(engine)

columns = [
    column["name"]
    for column in inspector.get_columns("documents")
]

with engine.begin() as connection:

    if "title" not in columns:
        connection.execute(
            text(
                "ALTER TABLE documents "
                "ADD COLUMN title VARCHAR(255)"
            )
        )
        print("Title column added successfully!")

    if "author" not in columns:
        connection.execute(
            text(
                "ALTER TABLE documents "
                "ADD COLUMN author VARCHAR(255)"
            )
        )
        print("Author column added successfully!")


print("PDF metadata migration completed!")