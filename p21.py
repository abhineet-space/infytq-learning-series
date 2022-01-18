''''
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program

Sample Input

Expected Output

AAAABBBBCCCCCCCC            -           4A4B8C

AABCCA                      -           2A1B2C1A
'''

#lex_auth_012693816331657216161

def encode(message):
    run_length = ''
    temp = message[0]
    count = 0
    #Remove pass and write your logic here
    for i in range(0,len(message),1):
        if message[i] == temp:
            count+=1
        else:
            run_length = run_length + str(count) + temp  
            temp = message[i]
            count = 1
    run_length = run_length + str(count) + temp  
    return run_length
    

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)