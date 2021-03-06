'''Problem Statement
Write a python function which accepts a sentence and returns a list in which first value is the count of upper case letters and second value is the count of lower case letters in the sentence. Ignore spaces, numbers and other special characters if any.

Sample Input            Expected Output

Hello world!                [1,9]

Welcome to Mysore           [2,13]

'''

#lex_auth_0127136021907046401165

def find_upper_and_lower(sentence):
    #start writing your code here
    result_list = [0,0]
    for i in range(0,len(sentence)):
        if sentence[i].isupper():
            result_list[0] += 1
        if sentence[i].islower():
            result_list[1] += 1
    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))