import sqlite3

connection = sqlite3.connect("database/infoquest.db")
cursor = connection.cursor()

document_id = "doc_c9a5df25032048bab86605e2585d89b7"

cursor.execute("""
    SELECT COUNT(*)
    FROM document_chunks
    WHERE document_id = ?
""", (document_id,))

count = cursor.fetchone()[0]

print("Total chunks stored:", count)

cursor.execute("""
    SELECT chunk_index, LENGTH(chunk_text)
    FROM document_chunks
    WHERE document_id = ?
    ORDER BY chunk_index
""", (document_id,))

for row in cursor.fetchall():
    print("Chunk index:", row[0], "| Characters:", row[1])

connection.close()