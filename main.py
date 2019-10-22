import argparse

from lib import *


def main():
  parser = argparse.ArgumentParser()
  op_group = parser.add_mutually_exclusive_group()
  op_group.add_argument('--half-add', '-ha', action='store_true')
  op_group.add_argument('--full-add', '-fa', action='store_true')
  op_group.add_argument('--half-subtract', '-hs', action='store_true')
  op_group.add_argument('--full-subtract', '-fs', action='store_true')
  parser.add_argument('--nums', '-n', metavar='N', type=int, nargs=2, help='2 integers for the accumulator')
  args = parser.parse_args()

  a = args.nums[0]
  b = args.nums[1]

  if args.half_add:
    ha = HalfAdder()
    ha.add(a, b)
  elif args.full_add:
    fa = FullAdder()
    fa.add(a, b)
  elif args.half_subtract:
    hs = HalfSubtractor()
    hs.subtract(a, b)
  elif args.full_subtract:
    fs = FullSubtractor()
    fs.subtract(a, b)


if __name__ == '__main__':
  main()
