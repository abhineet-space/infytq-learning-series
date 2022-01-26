'''Problem Statement
Write a python function, check_anagram() which accepts two strings and returns True, if one string is a special anagram of another string. Otherwise returns False.

The two strings are considered to be a special anagram if they contain repeating characters but none of the characters repeat at the same position. The length of the strings should be the same.

Note: Perform case insensitive comparison wherever applicable.

Sample Input

Expected Output

eat, tea

True

backward,drawback

False 
(Reason: character 'a' repeats at position 6, not an anagram)

Reductions,discounter

True

About, table

False'''

#lex_auth_0127382206342184961397

def check_anagram(data1,data2):
    #start writing your code here
    c1=0
    c2=0
    if len(data1) == len(data2):
        for i in range(0,len(data1)):
            if data1[i]==data2[i]:
                return False
            if data1[i].upper() in data2 or data1[i].lower() in data2:
                c1 += 1
            else:
                return False
            if data2[i].upper() in data1 or data2[i].lower() in data1:
                c2 += 1
            else:
                return False
            if c1 != c2:
                return False
        if c1 == len(data1):
            return True
    else:
        return False

print(check_anagram("scller","resell"))