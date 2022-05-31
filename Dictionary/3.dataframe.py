# Author :- Biresashis Das

# Here I will show you how to use loops with pandas DataFrame and iterate over a pandas DataFrame.

import pandas

student = {
    "Name" : ["JACK", "MATHEW", "VIKAS"],
    "Score" : [45, 54, 76]
}

student_dataframe = pandas.DataFrame(student)
print(student_dataframe,"\n")


# Loop throughs row of a DataFrame
for (index, row) in student_dataframe.iterrows():
    print(row)
    
#     Expected Output

#          Name  Score
#     0    JACK     45
#     1  MATHEW     54
#     2   VIKAS     76 

#     Name     JACK
#     Score      45
#     Name: 0, dtype: object
#     Name     MATHEW
#     Score        54
#     Name: 1, dtype: object
#     Name     VIKAS
#     Score       76
#     Name: 2, dtype: object


