# Author :- Biresashis Das

# List Comprehension
'''         
            Basic Format :
                list = []
                new_list = [new_item for item in list]
'''

#for numbers
numbers = [1,2,3]
new_num = [(n+1) for n in numbers]
print(new_num)

#for strings
name = "Fredrik"
new_name = [n for n in name]
print(new_name)

#Range
new_num = [(n*2) for n in range(1,5)]
print(new_num)



