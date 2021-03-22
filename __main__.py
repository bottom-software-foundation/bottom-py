import argparse
import os

from bottom import encode, decode

parser = argparse.ArgumentParser(
    description='Tool for translating between bottom and human readable text'
)
parser.add_argument(
    '--regress',
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

        if args.regress:
            print(decode(text))
        else:
            print(encode(text))

        if os.isatty(0):
            break
    except EOFError:
        break
