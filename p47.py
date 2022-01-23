'''Problem Statement
Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors.
Handle the possible errors in the code written inside the function.

Sample Input

16

Expected Output

120

'''
#lex_auth_01269442760027340879
def factor(num2,num):
    fact = []
    for i in range(1,num2+1):
        if num2%i == 0 :
            fact.append(i)
    if len(fact) == num:
        return num

def find_smallest_number(num):
    #start writing your code here
    i=1
    while(factor(i,num) != num):
        i += 1 
    return i
        
    

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)