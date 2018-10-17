"""
You are given a string s and width w.
Your task is to wrap the string into a paragraph of width w.

Input Format:
The first line contains a string, s.
The second line contains the width, w.

Constraints:
- 0 < len(s) < 1000... if len(s) > 0 and len(s) < 1000... if len(s) in xrange(1, 1000)
- 0 < w < len(s)... if w > 0 and w < len(s)... if w not in xrange(1, len(s))

Output Format:
Print the text wrapped paragraph.

"""
import textwrap


def wrap(string, max_width):
    if len(string) not in xrange(1, 1000):
        raise ValueError('ERROR: arg = "string" did not meet length requirements')
    if max_width not in xrange(1, len(string)):
        raise ValueError('ERROR: arg = "max_width" did not meet length requirements')

    #for each in [string[i:i + max_width] for i in range(0, len(string), max_width)]:
    #    print each
    print '\n'.join(textwrap.wrap(string, max_width))


wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)

