# Author :- Biresashis Das

# Conditional Dictionary Comprehension
'''
        Basic Format
            new_dict = {new_key:new_value for item in list if test}
'''

import random
names = ["Amit","Vijay","Rajesh","Erik","Jason","Jeremy","Matthew"]
student_scores = {student:random.randint(1,100) for student in names}   # Dictionary Comprehension
print(student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
print(passed_students)


# Expected Output

# {'Amit': 52, 'Vijay': 66, 'Rajesh': 70, 'Erik': 64, 'Jason': 23, 'Jeremy': 98, 'Matthew': 27}
# {'Vijay': 66, 'Rajesh': 70, 'Erik': 64, 'Jeremy': 98}


