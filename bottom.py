import io

__all__ = ("to_bottom", "from_bottom")


CHARACTER_VALUES = {
    200: "🫂",
    50: "💖",
    10: "✨",
    5: "🥺",
    1: ",",
    0: "❤️",
}

SECTION_SEPERATOR = "👉👈"


def to_bottom(text: io.TextIOWrapper) -> str:
    out = io.BytesIO()

    for char in text.read().encode():
        while char != 0:
            for value, emoji in CHARACTER_VALUES.items():
                if char >= value:
                    char -= value
                    out.write(emoji.encode())
                    break

        out.write(SECTION_SEPERATOR.encode())

    return out.getvalue().decode("utf-8")


def from_bottom(text: io.TextIOWrapper) -> str:
    out = io.BytesIO()
    bottom = "".join(text.read().strip().split(SECTION_SEPERATOR))

    if not all(
        c in CHARACTER_VALUES.values() for c in bottom.replace(SECTION_SEPERATOR, "")
    ):
        raise TypeError(f"Invalid bottom text: {text}")

    for char in bottom.split(SECTION_SEPERATOR):
        rev_mapping = {v: k for k, v in CHARACTER_VALUES.items()}

        sub = 0
        for emoji in char:
            sub += rev_mapping[emoji]

        out.write(sub.to_bytes(1, "big"))

    return out.getvalue().decode()
