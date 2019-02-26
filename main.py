import argparse

from lib.full_adder import FullAdder


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--add', '-a', action='store_true', help='add operation')
    parser.add_argument('--nums', '-n', metavar='N', type=int, nargs=2, help='an integer for the accumulator')
    args = parser.parse_args()
    
    if args.add:
        a = args.nums[0]
        b = args.nums[1]

        fa = FullAdder()
        fa.add(a, b)


if __name__ == '__main__':
    main()
