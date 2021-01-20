import argparse
import os

from .bottom import from_bottom, to_bottom

parser = argparse.ArgumentParser(
    description='Tool for translating between bottom and human readable text'
)
parser.add_argument(
    '--from-bottom',
    default=False,
    const=True,
    action='store_const'
)
if os.isatty(0):
    parser.add_argument('text')

args = parser.parse_args()

while True:
    try:
        text = args.text or input()

        if args.from_bottom:
            print(from_bottom(text))
        else:
            print(to_bottom(text))

        if os.isatty(0):
            break
    except EOFError:
        break
