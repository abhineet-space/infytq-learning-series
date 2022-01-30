'''Problem Statement
Given an integer n, write a python function to return true, if it is possible to represent it as a sum of the squares of two different integers, else return false.'''

#lex_auth_0127136357122129921205

def check_squares(number):
    #start writing your code here
    abc = False
    for i in range(1,number):
        for j in range(1,number):
            if i*i + j*j == number:
                abc = True
            if i*i +j*j >= number:
                break
    return abc


number=61
print(check_squares(number))