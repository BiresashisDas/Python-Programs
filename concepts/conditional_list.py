# Author :- Biresashis Das

# Conditional List Comprehension
'''
        Basic Format :
            list = []
            new_list = [new_item for item in list if test]
'''
          
#for integers
numbers = [1,2,3]
new_num = [num for num in numbers if num < 3]
print(new_num)

#for strings
name = ["abhi", "ronak", "Ankita", "bIr", "ash"]
new_name = [names.upper() for names in name if len(names) < 5]
print(new_name)



