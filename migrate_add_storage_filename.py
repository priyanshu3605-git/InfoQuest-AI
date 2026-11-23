from sqlalchemy import inspect, text

from infoquest.database.connection import engine


inspector = inspect(engine)

columns = [
    column["name"]
    for column in inspector.get_columns("documents")
]

if "storage_filename" not in columns:

    with engine.begin() as connection:

        connection.execute(
            text(
                "ALTER TABLE documents "
                "ADD COLUMN storage_filename VARCHAR(255)"
            )
        )

    print("storage_filename column added successfully!")

else:
    print("storage_filename column already exists!")