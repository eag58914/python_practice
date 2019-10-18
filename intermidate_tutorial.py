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

def main():
    parser = argparse


def calc(x, y, operation):
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    elif operation == 'mul':
        return x * y
    elif operation == 'div':
        return x / y


operation = calc(7, 3, 'div')
print(operation)

# convert to argparse for cli
