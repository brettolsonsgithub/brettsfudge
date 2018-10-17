"""
Task:
You are given a string s.
Your task is to find out if the string s contains: alphanumeric characters, alphabetical characters, digits, lowercase
and uppercase characters.

Input Format:
A single line containing a string s.

Constraints
0 < len(s) < 1000... if len(s) > 0 and len(s) < 1000... if len(s) in xrange(1,1000)

Output Format:
In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
In the second line, print True if s has any alphabetical characters. Otherwise, print False.
In the third line, print True if s has any digits. Otherwise, print False.
In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
In the fifth line, print True if s has any uppercase characters. Otherwise, print False.

"""


def validate_alnum(s):
    for i in s:
        if i.isalnum():
            return True
    return False


def validate_alpha(s):
    for i in s:
        if i.isalpha():
            return True
    return False


def validate_digit(s):
    for i in s:
        if i.isdigit():
            return True
    return False


def validate_lower(s):
    for i in s:
        if i.islower():
            return True
    return False


def validate_upper(s):
    for i in s:
        if i.isupper():
            return True
    return False


if __name__ == '__main__':
    s = raw_input()

    print validate_alnum(s)
    print validate_alpha(s)
    print validate_digit(s)
    print validate_lower(s)
    print validate_upper(s)
