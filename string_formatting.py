"""
Given an integer, n, print the following values for each integer i from 1 to n:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

The four values must be printed on a single line in the order specified above for each from i to n.
Each value should be space-padded to match the width of the binary value of n.

Input Format:
A single integer denoting n.

Constraints:
1 <= n <= 99... if n >= 1 and n <= 99... if n in xrange(1, 99)

Output Format:
Print n lines where each line i (in the range 1 <= i <= n) contains the respective decimal, octal, capitalized
hexadecimal, and binary values of i. Each printed value must be formatted to the width of the binary value of n.

"""


def print_formatted(number):
    if number not in xrange(1, 100):
        raise ValueError('ERROR arg = number does not meet length requirements')

    # this is the largest possible binary length
    max_binary_len = len('{:b}'.format(number))

    for i in xrange(1, number+1):
        print '{:{}d}'.format(i, max_binary_len), \
            '{:{}o}'.format(i, max_binary_len), \
            '{:{}X}'.format(i, max_binary_len), \
            '{:{}b}'.format(i, max_binary_len)


if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
