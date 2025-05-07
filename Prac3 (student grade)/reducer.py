#!/usr/bin/env python
import sys

def get_grade(marks):
    marks = int(marks)
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    elif marks >= 50:
        return 'E'
    else:
        return 'F'

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    name, marks = line.split("\t")
    grade = get_grade(marks)
    print("{0}\t{1}".format(name, grade))
