from infoquest.services.text_cleaner import clean_extracted_text


# Test 1: Normal text with unnecessary spaces
text = "Artificial     Intelligence    is the future."

result = clean_extracted_text(text)

print("Test 1:", result)

assert result == "Artificial Intelligence is the future."


# Test 2: Multiple blank lines
text = "Machine Learning\n\n\n\nDeep Learning"

result = clean_extracted_text(text)

print("Test 2:", result)

assert result == "Machine Learning\n\nDeep Learning"


# Test 3: Tabs and spaces
text = "Python\t\tProgramming     Language"

result = clean_extracted_text(text)

print("Test 3:", result)

assert result == "Python Programming Language"


# Test 4: Empty text
text = ""

result = clean_extracted_text(text)

assert result == ""

print("Test 4: Empty text passed!")


# Test 5: Invalid input
try:
    clean_extracted_text(123)
except TypeError:
    print("Test 5: Invalid input handled successfully!")


print("\nAll text cleaning tests passed!")