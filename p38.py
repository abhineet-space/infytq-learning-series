'''Problem Statement
Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.

The number and its double should have exactly the same number of digits.

Both the numbers should have the same digits ,but in different order.

Otherwise it should return False.

Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.'''


#lex_auth_01269441810970214471

def check_double(number):
    #pass
    #Remove pass and write your logic here
    count = 0
    new_num = number * 2
    for i in str(new_num):
        if i in str(number):
            pass
        else:
            count += 1
    if count > 0:
        return False
    else:
        return True

#Provide different values for number and test your program
print(check_double(125874))