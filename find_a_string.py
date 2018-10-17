"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring
occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format:
The first line of input contains the original string. The next line contains the substring.

Constraints:
- 1 <= len(string) <= 200... if len(string) >=1 and len(string) <=200... if len(string) in xrange(1, 201)

- Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.
"""


def count_substring(string, sub_string):
    s = string.encode('ascii', 'ignore')
    if len(s) in xrange(1, 201):
        sub_string_match = 0
        for i in xrange(len(s)):
            string_iter = s[i:i+len(sub_string)]
            if string_iter == sub_string:
                sub_string_match +=1

        return sub_string_match
    else:
        raise ValueError("ERROR: string did not meet length requirements, len(string) = {}".format(len(string)))

print count_substring('DCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDCCDC', 'CDC')