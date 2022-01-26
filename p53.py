'''Problem Statement
Write a python function to check whether the given number is a perfect number or not. The function should returns true if the number is a perfect number, else it should returns false.

Hint: Perfect number is a positive whole number that is equal to the sum of its proper divisors.
The first perfect number is 6 as the sum of its proper positive divisors, 1,2 and 3 is 6. Other perfect numbers are 28, 496, 8128 ...

Extend the program written for the above problem to write another function to find all perfect numbers in a given list of numbers. Populate the perfect numbers in a list and return the list. If no perfect numbers found, return an empty list.

Note- Reuse the code wherever possible.'''


#lex_auth_01269446533799116898

def check_perfect_number(number):
    #start writing your code here
    val = []
    sum = 0
    for i in range(1,number-1):
        if number%i == 0:
            val.append(i)
    for i in val:
        sum += i
    if sum == number and number != 0:
        return True
    else:
        return False
    

def check_perfectno_from_list(no_list):
    #start writing your code here
    new = []
    for i in no_list:
        if check_perfect_number(i) == True:
            new.append(i)
    return new

perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)