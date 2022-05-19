# Author :- Biresashis das

# In this program we will print the name of the Student who score the second lowest score.

if __name__ == '__main__':
    score_list = []
    score_1 = []
    no_of_students = int(input("Enter the number of students : "))
    for _ in range(no_of_students):
        name = input("Enter the name of Student : ").title()
        score = float(input(f"Enter the score of {name} : "))
        score_list.append([name, score])
        score_1.append(score)
        score_1 = list(set(score_1))
        score_1.sort()
        score_list.sort()
    second_lowest = score_1[1]
    for name,score in score_list:
        if score == second_lowest:
            print(f"The second lowest score is {score_1[1]} and the Student who got this score is : {name}")
            
            
            
            
            
