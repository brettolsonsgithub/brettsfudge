"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com -> wWW.hACKERrANK.COM
Pythonist 2 -> pYTHONIST 2

Input Format:
A single line containing a string s.

Constraints
0 <= len(s) <= 1000... if len(s) >= 0 and len(s) <= 1000... if len(s) in xrange(0, 1001)

Output Format

Print the modified string s.

"""


def swap_case(s):
    swap_string = ""
    if len(s) in xrange(0, 1001):
        for char in s:
            if char.isupper():
                swap_string += char.lower()
            else:
                swap_string += char.upper()
    else:
        raise ValueError('ERROR: the length of s is {}'.format(len(s)))

    return swap_string

print swap_case('HackerRank.com presents "Pythonist 2".')