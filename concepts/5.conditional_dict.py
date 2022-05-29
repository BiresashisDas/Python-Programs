# Author :- Biresashis Das

# Conditional Dictionary Comprehension
'''
        Basic Format
            new_dict = {new_key:new_value for item in list if test}
'''

import random
names = ["Amit","Vijay","Rajesh","Erik","Jason","Jeremy","Matthew"]
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
print(passed_students)


