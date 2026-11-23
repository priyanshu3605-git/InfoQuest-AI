def split_text(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> list[str]:

    # 1. Validate input
    if not isinstance(text, str):
        raise TypeError("Text must be a string")

    if not text.strip():
        return []

    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive")

    if chunk_overlap < 0:
        raise ValueError("Chunk overlap cannot be negative")

    if chunk_overlap >= chunk_size:
        raise ValueError(
            "Chunk overlap must be smaller than chunk size"
        )

    # 2. Define recursive separators
    separators = [
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
    ]

    # 3. Recursively split the text
    def recursive_split(
        text: str,
        separators: list[str]
    ) -> list[str]:

        if len(text) <= chunk_size:
            return [text]

        if not separators:
            return [text[i:i + chunk_size]
                    for i in range(0, len(text), chunk_size)]

        separator = separators[0]
        remaining_separators = separators[1:]

        if separator:
            if separator not in text:
                return recursive_split(
                    text,
                    remaining_separators
                )

            parts = text.split(separator)

            # Preserve the separator
            splits = [
                part + separator
                for part in parts[:-1]
            ]

            if parts[-1]:
                splits.append(parts[-1])

        else:
            # Last resort: split character by character
            splits = list(text)

        final_splits = []

        for part in splits:

            if len(part) <= chunk_size:
                final_splits.append(part)

            else:
                smaller_parts = recursive_split(
                    part,
                    remaining_separators
                )

                final_splits.extend(smaller_parts)

        return final_splits

    # 4. Merge smaller splits into chunks
    def merge_splits(
        splits: list[str]
    ) -> list[str]:

        chunks = []
        current_chunk = []
        current_length = 0

        for split in splits:

            split_length = len(split)

            if (
                current_length + split_length > chunk_size
                and current_chunk
            ):

                chunk = "".join(current_chunk).strip()

                if chunk:
                    chunks.append(chunk)

                # Maintain overlap
                while current_chunk and (
                    current_length > chunk_overlap
                    or current_length + split_length > chunk_size
                ):

                    removed = current_chunk.pop(0)
                    current_length -= len(removed)

            current_chunk.append(split)
            current_length += split_length

        # Add the remaining text
        if current_chunk:

            chunk = "".join(current_chunk).strip()

            if chunk:
                chunks.append(chunk)

        return chunks

    # 5. Execute the complete chunking pipeline
    smaller_splits = recursive_split(
        text,
        separators
    )

    final_chunks = merge_splits(
        smaller_splits
    )

    return final_chunks