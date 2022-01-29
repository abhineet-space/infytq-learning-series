'''Problem Statement
Given a string, write a python function to return True if the strings "mat" and "jet" appear the same number of times in the given string, else return False.

Note: Perform case insensitive string comparison wherever necessary.

Sample Input                            Expected Output

Jet on the Mat but mat is too long          False

mat jet Jet Mat                             True

'''


#lex_auth_0127136253311385601197

def check_occurence(string):
    #start writing your code here
    if string.lower().count('mat') == string.lower().count('jet'):
        return True
    else:
        return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))