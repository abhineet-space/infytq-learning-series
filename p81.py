'''Problem Statement
Tom is working in a shop where he labels items. Each item is labelled with a number between num1 and num2(both inclusive). Since Tom is also a natural mathematician, he likes to observe patterns in numbers. Tom could observe that some of these label numbers are divisible by other label numbers.

Write a Python function to find out those label numbers that are divisible by another label number and display how many such label numbers are there totally.

Note:- Consider only the distinct label numbers. The list of those label numbers should be considered as a set.'''

#lex_auth_0127136209566679041189

def check_numbers(num1,num2):
    #start writing your code here
    new_list = []
    num_list =[]
    for i in range(num1,num2+1):
        new_list.append(i)
    for i in range(0,len(new_list)):
        for j in range(0,(len(new_list))):
            if new_list[i] == new_list[j]:
                continue
            if new_list[i]%new_list[j] == 0:
                num_list.append(new_list[i])
    return [set(num_list),len(set(num_list))]

num1=2
num2=20
print(check_numbers(num1, num2))