"""
You have a record of n students. Each record contains the student's name, and their percent marks in Maths,
Physics and Chemistry. The marks can be floating values. The user enters some integer n followed by the names and marks
for students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format:
The first line contains the integer n, the number of students. The next n lines contains the name and marks obtained by
that student separated by a space. The final line contains the name of a particular student previously listed.

Constraints:
2 <= n <= 10 #### n in range(2, 11)

Output Format:
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

"""
if __name__ == '__main__':
    n = int(raw_input("1st int input: "))

    if n in range(2, 11):
        student_marks = {}
        for _ in range(n):
            line = raw_input().split()
            name, scores = line[0], line[1:]
            scores = map(float, scores)
            student_marks[name] = scores
        query_name = raw_input("2nd string input: ")

        if query_name in student_marks.keys():
            avg = 0.00
            for mark in student_marks[query_name]:
                avg += mark
            avg = avg/len(student_marks[query_name])

            print format(avg, '.2f')
