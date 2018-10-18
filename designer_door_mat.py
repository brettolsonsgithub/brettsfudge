"""
Input Format:
A single line containing the space separated values of  and .

Constraints:
5 < n < 101... if n > 5 and n < 101... if n in xrange(5, 101)
15 < m < 303, if m > 15 and m < 303... if m in xrange(15, 303)

Output Format:
Output the design pattern.

"""


def door_mat(n, m, val='.|.', pad='-'):
    if n not in xrange(5, 101):
        raise ValueError('ERROR: arg n did not meet length requirement')
    if m not in xrange(15, 303):
        raise ValueError('ERROR: arg m did not meet length requirement')

    multiplier = 1
    for i in xrange(n):
        if i in xrange(n/2):
            my_list = [val * multiplier]
            multiplier += 2
            new_string = ''
            while len(new_string) != m:
                my_list.append(pad)
                my_list.insert(0, pad)
                new_string = ''.join(my_list)
            print new_string
        elif i == n/2:
            my_list = ['WELCOME']
            new_string = ''
            while len(new_string) != m:
                my_list.append(pad)
                my_list.insert(0, pad)
                new_string = ''.join(my_list)
            print new_string
        else:
            multiplier -= 2
            my_list = [val * multiplier]
            new_string = ''
            while len(new_string) != m:
                my_list.append(pad)
                my_list.insert(0, pad)
                new_string = ''.join(my_list)
            print new_string


if __name__ == '__main__':
    n, m = map(int, raw_input().split())
    door_mat(n, m)