"""
Task:
Read an integer n. For all non-negative integers i < n, print i^2. See the sample for details.

Input Format:

The first and only line contains the integer, n.

Constraints:
1 <= n <= 20

Output Format

Print  lines, one corresponding to each i.

"""
if __name__ == '__main__':
    n = int(raw_input())

    if n in xrange(21):
        for i in xrange(n):
            print i*i