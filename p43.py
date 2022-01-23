'''Problem Statement
Consider that the human tower is to be performed on a stage and the stage has a maximum weight limit. 

Write a python program to find the maximum number of people at the base level such that the total weight of tower does not exceed the maximum weight limit of the stage. 

Assume that:
1. Each person weighs 50 kg 
2. There will always be odd number of men at the base level of the human tower.'''


#lex_auth_01269437527007232044

def human_pyramid(no_of_people):
    #pass #remove pass and place the recursive code the you had written earlier for this function
    if no_of_people == 1:
        return 1*50 
    return no_of_people*50 + human_pyramid(no_of_people-2)

def find_maximum_people(max_weight):
    no_of_people=1
    #write your logic here. You may invoke recursive function human_pyramid() wherever applicable 
    while (max_weight >= human_pyramid(no_of_people)):
        no_of_people += 2
    return no_of_people-2

#Provide different values for max_weight and test your program
max_people=find_maximum_people(1000)
print(max_people)