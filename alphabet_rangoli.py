"""
The center of the rangoli has the first alphabet letter a, and the boundary has the nth alphabet letter
(in alphabetical order).

Input Format:
Only one line of input containing n, the size of the rangoli.

Constraints:
0 < n < 27... if n > 0 and n < 27... if n not in xrange(1, 28)

Output Format:
Print the alphabet rangoli in the format explained above.

"""
import string


def print_rangoli(size):
    if size not in xrange(1, 28):
        raise ValueError('ERROR arg = size does not meet length requirements')

    # slice a reversed list of the alphabet
    letters = [x for x in string.ascii_lowercase]
    letter_slice = ''.join(letters[:size][::-1])

    # create a list of raw values, create a list of raw value strings separated by '-'
    all_lists = []
    all_strings = []
    for i in xrange(0, size):
        last_val = letter_slice[:i+1]
        if i:
            w_pad = list(letter_slice[:i+1] + last_val[::-1][1:])
        else:
            w_pad = list(letter_slice[:i + 1])
        all_lists.append(w_pad)
        all_strings.append('-'.join(w_pad))

    # build a new list with '-' padding while the new value is < raw value string
    new_all_list = []
    for i in xrange(len(all_strings)):
        new_list = [x for x in all_strings[i]]
        while len(new_list) < len(all_strings[-1]):
            new_list.append('-')
            new_list.insert(0, '-')
        new_all_list.append(''.join(new_list))

    # print values up to size parameter
    for line in new_all_list:
        print line

    # print values up to size parameter-1, in reverse
    for line in new_all_list[::-1][1:]:
        print line


print_rangoli(8)