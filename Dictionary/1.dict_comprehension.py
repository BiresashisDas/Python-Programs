# Author :- Biresashis Das

# Note :- We use this "{}" to make a dictionary.

# Dictionary Comprehension

'''
            Basic Format :        
                new_dict = {new_key:new_value for item in list}
'''

sentence = "There is some good in this world, and it’s worth fighting for."
result = {line:len(line) for line in sentence.split()}
print(result)


# Expected Output

# {'There': 5, 'is': 2, 'some': 4, 'good': 4, 'in': 2, 'this': 4, 'world,': 6, 'and': 3, 'it’s': 4, 'worth': 5, 'fighting': 8, 'for.': 4}


