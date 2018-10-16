"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

"""
if __name__ == '__main__':
    mylist = []
    for i in xrange(int(raw_input())):
        operations = str(raw_input())

        all_operations = operations.split()
        if len(all_operations) == 3:
            arg1, arg2, arg3 = (all_operations[0], int(all_operations[1]), int(all_operations[2]))
            if arg1 == 'insert':
                mylist.insert(arg2, arg3)
        elif len(all_operations) == 2:
            arg1, arg2 = (all_operations[0], int(all_operations[1]))
            if arg1 == 'append':
                mylist.append(arg2)
            elif arg1 == 'remove':
                mylist.remove(arg2)
        elif len(all_operations) == 1:
            arg1 = all_operations[0]
            if arg1 == 'print':
                print mylist
            elif arg1 == 'sort':
                mylist = sorted(mylist)
            elif arg1 == 'pop':
                mylist.pop(-1)
            elif arg1 == 'reverse':
                mylist = mylist[::-1]
        else:
            raise ValueError('ERROR: received invalid arg = {}'.format(all_operations))

"""
29
append 1
append 6
append 10
append 8
append 9
append 2
append 12
append 7
append 3
append 5
insert 8 66
insert 1 30
insert 6 75
insert 4 44
insert 9 67
insert 2 44
insert 9 21
insert 8 87
insert 1 75
insert 1 48
print
reverse
print
sort
print
append 2
append 5
remove 2
print

"""