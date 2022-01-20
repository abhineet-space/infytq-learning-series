'''Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.

Sample Input

Expected output

"I like Python"
"Java is a very popular language"          -        lieyon'''

#lex_auth_012693825794351104168

def find_common_characters(msg1,msg2):
    abc =''
    for i in range (0,len(msg1),1):
        if msg1[i] != ' ':
            for j in range(0,len(msg2),1):
                if msg2[j] != ' ':
                    if msg1[i] == msg2[j]:
                        if not msg1[i] in abc:
                            abc += msg1[i]
    if len(abc) >0:
        return abc
    else:
        return -1

    #pass #Remove pass and write your logic here

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
