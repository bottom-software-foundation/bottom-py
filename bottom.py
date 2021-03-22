CHARACTER_VALUES = {
    200: "🫂",
    50: "💖",
    10: "✨",
    5: "🥺",
    1: ",",
    0: "❤️"
}

SECTION_SEPERATOR = '👉👈'


def byte_to_emoji(b: int) -> str:
    out = ""

    while True:
        for value, emoji in CHARACTER_VALUES.items():
            if b >= value:
                out += emoji
                b -= value
                break

        if b == 0:
            break;

    return out


# Dict[int, str]
BYTE_TO_EMOJI = {i: byte_to_emoji(i) for i in range(256)}


# Dict[str, str]
EMOJI_TO_BYTE = {v: k.to_bytes(1, 'big') for k, v in BYTE_TO_EMOJI.items()}


def encode(text: str) -> str:
    out = ""

    for char in text.encode('utf-8'):
        out += BYTE_TO_EMOJI[char] + SECTION_SEPERATOR

    return out


def decode(text: str) -> str:
    text = text.removesuffix(SECTION_SEPERATOR)

    out = bytearray()

    for char in text.split(SECTION_SEPERATOR):
        try:
            out += EMOJI_TO_BYTE[char]
        except KeyError:
            raise TypeError(f'Could not decode character: {char}') from None

    return out.decode('utf-8')
