"""
Given the names and grades for each student in a Physics class of n students, store them in a nested list and print the
name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new
line.

Input Format:
The first line contains an integer, n, the number of students.
The 2n subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second
line contains their grade.

Constraints:
There will always be one or more students having the second lowest grade.

Output Format:
Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order
their names alphabetically and print each one on a new line.

Sample Input 0:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0:
Berry
Harry

"""
if __name__ == '__main__':
    all_student_scores = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        all_student_scores.append([name, score])

        # sort list by index=1 (score)
        all_student_scores.sort(key=lambda x: x[1])

    # get 2nd lowest score
    scores_only = []
    for score in all_student_scores:
        scores_only.append(score[1])
    my_arr = [x for x in map(float, set(scores_only))]
    sorted_set_arr = sorted(my_arr)
    runner_up_score = sorted_set_arr[1]

    # sort list by index=0 (name)
    all_student_scores.sort(key=lambda x: x[0])

    # print students with 2nd lowest score
    for student_score in all_student_scores:
        if runner_up_score in student_score:
            print student_score[0]
