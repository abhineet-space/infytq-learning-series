'''Write a python function to find out whether a number is divisible by the sum of its digits. If so return True,else return False.

Sample Input            Expected Output

42                           True

66                           False
'''
#lex_auth_0127136251125350401190

def divisible_by_sum(number):
    #start writing your code here
    sum = 0
    for i in str(number):
        sum += int(i)
    if number%sum == 0:
        return True
    else:
        return False

    
number=42
print(divisible_by_sum(number))