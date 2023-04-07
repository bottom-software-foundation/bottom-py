import argparse
import io
import os

from .bottom import from_bottom, to_bottom

parser = argparse.ArgumentParser(
    description="Tool for translating between bottom and human readable text"
)
parser.add_argument("--from-bottom", default=False, const=True, action="store_const")
parser.add_argument("text", nargs="*", default=None, help="Text to translate")

args = parser.parse_args()

while True:
    try:
        text = "".join(args.text) if args.text else input()

        if args.from_bottom:
            print(from_bottom(io.StringIO(text)))
        else:
            print(to_bottom(io.StringIO(text)))

        if os.isatty(0):
            break
    except EOFError:
        break
