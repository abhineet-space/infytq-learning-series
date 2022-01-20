'''Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
Assume that the words contain only uppercase letters and the maximum word length is 10.

Sample Input                                    --------                                        Expected Output

{"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}  ----    [2, 2, 1]

'''


#lex_auth_01269444890062848087

def find_correct(word_dict):
    #start writing your code here
    good = 0
    average = 0 
    wrong = 0 
    list = [good,average,wrong]
    for key,value in word_dict.items():
        count = 0
        if len(key) == len(value):
            if key == value:
                good += 1
            else:
                for i in range(0,len(key),1):
                    if len(key) == len(value):
                        if key[i] != value[i]:
                            count += 1
            
                if count > 2:
                    wrong += 1 
                else:
                    average += 1

        else:
            wrong += 1
    list = [good,average,wrong]                
    return list
                
word_dict = {'CHECK': 'CHEK', 'MIND': 'MUND', 'ALWAYS': 'ALLISWELL', 'VENDOR': 'VENDING', 'RADIO': 'RADICAL'}
#word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))