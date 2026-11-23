import re


def clean_extracted_text(text: str) -> str:

    # Step 1: Validate input
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    if not text.strip():
        return ""

    # Step 2: Normalize line endings
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Step 3: Remove unnecessary tabs and spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Step 4: Remove spaces around line breaks
    text = re.sub(r" *\n *", "\n", text)

    # Step 5: Reduce excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Step 6: Remove leading and trailing whitespace
    text = text.strip()

    return text