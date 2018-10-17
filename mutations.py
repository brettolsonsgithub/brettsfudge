"""
Task:
Read a given string, change the character at a given index and then print the modified string.

Input Format:
The first line contains a string, s.
The next line contains an integer i, denoting the index location and a character c separated by a space.

Output Format:
Using any of the methods explained above, replace the character at index i with character c.

"""


def mutate_string(string, position, character):
    mutated = ""
    s = list(string)
    for i in xrange(len(s)):
        if i != position:
            mutated += s[i]
        else:
            mutated += character
    return mutated

print mutate_string('abracadabra', 5, 'k')