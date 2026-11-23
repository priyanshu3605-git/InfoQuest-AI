from io import BytesIO

from fastapi import UploadFile

from infoquest.services.file_storage import save_uploaded_file


# Create a sample file for testing
sample_file = UploadFile(
    filename="sample.pdf",
    file=BytesIO(b"%PDF-1.4\nSample PDF content")
)


# Save the file
saved_filename = save_uploaded_file(sample_file)

print("File saved successfully!")
print("Generated filename:", saved_filename)