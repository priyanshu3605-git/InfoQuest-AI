import sqlite3

connection = sqlite3.connect("database/infoquest.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT document_id, LENGTH(extracted_text), extracted_text
    FROM documents
    ORDER BY created_at DESC
    LIMIT 1
""")

result = cursor.fetchone()

print("Document ID:", result[0])
print("Text Length:", result[1])
print("Extracted Text Preview:")
print(result[2][:1000])

connection.close()