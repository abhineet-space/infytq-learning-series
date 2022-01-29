'''Problem Statement
Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.

It should return a list in which the first value should be letter count and second value should be digit count. Ignore the spaces or any other special character in the sentence.

Sample Input            Expected Output

Infosys 123             [7,3]

ABCEFG                  [6,0]'''


#lex_auth_0127135838317445121147

def count_digits_letters(sentence):
    #start writing your code here
    result_list = [0,0]
    for i in range(0,len(sentence)):
        if sentence[i].isdigit():
            result_list[1] += 1
        elif sentence[i].isalpha():
            result_list[0] += 1
    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))