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


