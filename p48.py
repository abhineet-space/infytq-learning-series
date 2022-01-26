'''A 10-substring of a number is a substring of its digits that sum up to 10.

For example, the 10-substrings of the number 3523014 are:
3523014, 3523014, 3523014, 3523014

Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that string.

Handle the possible errors in the code written inside the function.

Sample Input

'3523014'

Expected Output

['5230', '23014', '523', '352']

'''

#lex_auth_01269442545042227276

def find_ten_substring(num_str):
    #pass
    #Remove pass and write your logic here
    n = []
    for i in range(0,len(num_str)):
        sum = 0
        new = ''
        for j in range(i,len(num_str)):
            sum = sum + int(num_str[j])
            new = new + (num_str[j])
            if sum == 10:
                n.append(new)
    return n
    

num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)