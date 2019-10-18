import argparse
import sys


# String Formatting
##names = ['Jeff', 'Gary', 'Jill', 'Samantha']

# for name in names:
#     #print('Hello there, ' + name)
#     print(' '.join(['Hello there', name]))

#print(', '.join(names))


# who = 'Gary'
# how_many = 12

# # sentence
# print(who, 'bought', how_many, 'apples')

# # correct way of doing string formatting
# print('{} bought{} apples today!'.format(who, how_many))

# argparse for CLI (part) 3
# convert to argparse for cli

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="What is the first number?"
                        )
    parser.add_argument('--y', type=float, default=1.0,
                        help="What is the second number?"
                        )
    parser.add_argument('--operation', type=str, default='add',
                        help="What operation? (add,sub,mul, or div)"
                        )
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y


if __name__ == '__main__':
    main()


# so much  fun
