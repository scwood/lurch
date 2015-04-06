#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help="increase output verbosity",
        action="store_true")
parser.add_argument("square", type=int, help="calculate the square")
args = parser.parse_args()
answer=args.square**2
if args.verbosity:
    print("The square of ", args.square, " is ", answer, ".", sep="")
else:
    print(answer)
