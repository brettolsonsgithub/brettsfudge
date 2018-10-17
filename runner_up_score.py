"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You
are given n scores. Store them in a list and find the score of the runner-up.

Input Format:
The first line contains n. The second line contains an array a[] of n integers each separated by a space.

Constraints:
2 <= n <=10... n >= 2 and n <=10... n in xrange(2,11)
-100 <= a[i] <= 100... a[i] >= -100 and a[i] <= 100... a[i] in xrange(-100, 101)

"""


def runner_up_score(n, arr):
    n_range = xrange(2, 11)
    if n not in n_range:
        return
    arr_range = xrange(-100, 101)
    my_arr = [x for x in map(int, set(arr)) if x in arr_range]
    sorted_set_arr = sorted(my_arr, reverse=True)

    print 'my_arr = {}'.format(my_arr)
    print 'sorted_set_arr = {}'.format(sorted_set_arr)

    return sorted_set_arr[1]


if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

    print runner_up_score(n, arr)
