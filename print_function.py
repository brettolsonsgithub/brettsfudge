"""
Read an integer n.

Without using any string methods, try to print the following:

123...n

Note that "..." represents the values in between.

Input Format:
The first line contains an integer n.

Output Format:
Output the answer as explained in the task.

"""
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

    for i in xrange(1, n+1):
        print(i, end='')