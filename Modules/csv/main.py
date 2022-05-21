# Author :- Biresashis Das

import csv

with open("student.csv") as student:
    data = csv.reader(student)
    for line in data:
        print(line)
