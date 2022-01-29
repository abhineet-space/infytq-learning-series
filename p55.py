'''Problem Statement
Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number. 

Sample Input        Expected Output

12300               12321

12331               12421

'''
# Using another check function
#lex_auth_01269443664174284882
def check_palindrome(number):
    c = 0
    for i in range(0,len(number)):
        if number[i] == number[-(i+1)]:
            c += 1 
    if c == len(number):
        return True
    else:
        return False
    
def nearest_palindrome(number):
    #start writitng your code here
    while True:
        number += 1
        if check_palindrome(str(number)) == True:
            break
    return number

number=12300
print(nearest_palindrome(number))

# using recursion
def nearest_palindrome(number):
    #start writitng your code here
    number += 1
    number =str(number)
    if number == number[::-1]:
        return int(number)
    else:
        return nearest_palindrome(int(number))

number=12300
print(nearest_palindrome(number))


# using iteration
def nearest_palindrome(number):
    #start writitng your code here
    number += 1
    new_num = str(number)
    while new_num != new_num[::-1]:
        number += 1
        new_num = str(number)
    return number

number=12300
print(nearest_palindrome(number))