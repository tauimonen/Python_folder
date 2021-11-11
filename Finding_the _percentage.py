"""
Hackerrank challenge.

Print the average of the marks array for the student name
provided, showing 2 places after the decimal.

Printing the average of the marks obtained by the particular
student correct to 2 decimal places.
"""

from pip._vendor.distlib.compat import raw_input

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    l = list(student_marks[query_name])
    total = sum(student_marks[query_name])
    c = len(l)
    print(total, c)
    avg = total / c
    print("{:.2f}".format(avg))

