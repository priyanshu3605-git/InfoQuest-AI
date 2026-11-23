from infoquest.services.chunking import split_text


# TEST 1: Normal paragraph splitting

sample_text = """
Artificial Intelligence is transforming industries.

Machine Learning is a subset of Artificial Intelligence.

Deep Learning uses neural networks to learn complex patterns.

Natural Language Processing helps computers understand human language.
"""

chunks = split_text(
    sample_text,
    chunk_size=100,
    chunk_overlap=20
)

print("\n========== TEST 1: NORMAL TEXT ==========")

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}:")
    print(chunk)
    print("Length:", len(chunk))


# TEST 2: Check maximum chunk size

print("\n========== TEST 2: CHUNK SIZE ==========")

for chunk in chunks:
    assert len(chunk) <= 100

print("PASS: All chunks are within the size limit.")


# TEST 3: Empty text

print("\n========== TEST 3: EMPTY TEXT ==========")

result = split_text("")

assert result == []

print("PASS: Empty text handled correctly.")


# TEST 4: Very large text without spaces

print("\n========== TEST 4: LARGE TEXT ==========")

large_text = "A" * 500

large_chunks = split_text(
    large_text,
    chunk_size=100,
    chunk_overlap=20
)

for chunk in large_chunks:
    assert len(chunk) <= 100

print("Original text length:", len(large_text))
print("Number of chunks:", len(large_chunks))
print("Largest chunk:", max(map(len, large_chunks)))


# TEST 5: Invalid chunk size

print("\n========== TEST 5: INVALID INPUT ==========")

try:
    split_text("Hello World", chunk_size=0)
except ValueError:
    print("PASS: Invalid chunk size detected.")


# TEST 6: Invalid overlap

try:
    split_text(
        "Hello World",
        chunk_size=100,
        chunk_overlap=100
    )
except ValueError:
    print("PASS: Invalid overlap detected.")

# TEST 7: Chunk Overlap

print("\n========== TEST 7: CHUNK OVERLAP ==========")

long_text = "".join(str(i % 10) for i in range(500))

overlap_chunks = split_text(
    long_text,
    chunk_size=100,
    chunk_overlap=20
)

if len(overlap_chunks) >= 2:
    assert overlap_chunks[0][-20:] == overlap_chunks[1][:20]

print("PASS: Consecutive chunks contain overlapping text.")


# TEST 8: Text Preservation

print("\n========== TEST 8: TEXT PRESERVATION ==========")

reconstructed_text = overlap_chunks[0]

for chunk in overlap_chunks[1:]:
    reconstructed_text += chunk[20:]

assert reconstructed_text == long_text

print("PASS: Original text preserved successfully.")
print("\n========== ALL TESTS COMPLETED ==========")