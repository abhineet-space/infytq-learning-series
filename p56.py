'''Problem Statement
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

Write a python program to find and display the number of circular primes less than the given limit.'''

#lex_auth_01269446157664256093

def check_prime(number):
    #pass #remove pass and write your logic here. if the number is prime return true, else return false
    flag = True
    if number> 1:
        for i in range(2,number):
            if number%i == 0:
                flag = False
    else:
        flag = False
    return flag

def rotations(num):
    #pass #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]
    i = 0
    s = []
    num =str(num)
    while i < len(num):
        ss = ''
        for x in range(i,len(num)):
            ss += num[x]
        for x in range(0,i):
            ss += num[x]
        i += 1
        s.append(int(ss))
    return s

def get_circular_prime_count(limit):
    #pass #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
    count =  0
    for i in range(1,limit):
        if check_prime(i) == True:
            s = rotations(i)
            c = 0
            for x in s:
                if check_prime(x) == True:
                    c += 1 
            if c == len(s):
                count += 1
    return count

#Provide different values for limit and test your program
print(get_circular_prime_count(1000))