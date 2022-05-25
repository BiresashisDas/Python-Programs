# Author :- Biresashis Das

#Create a Dataframe from Scratch

data_dict_new = {
    "Students": ["Ronak", "Abhishek", "Udit"],
    "Scores": [54, 76, 83]
}
data_new = pandas.DataFrame(data_dict_new)
print(data_new)




#   EXPECTED OUTPUT


#        Students  Scores
#     0     Ronak      54
#     1  Abhishek      76
#     2      Udit      83




