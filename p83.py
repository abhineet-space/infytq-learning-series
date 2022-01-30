'''Problem Statement
Write a python function to identify and return the number name of a given number. The number should be in the range 1 to 1000. If the number is invalid, return -1.

Example:

Sample input            Expected output

1                           one

15                          fifteen

45                          forty five

125                         one hundred and twenty five

999                         nine hundred and ninety nine

1000                        one thousand

1211                         -1
'''

#lex_auth_0127136373866577921209

def integer_to_english(number):
    #start writing your code here
    if number >=1 and number <= 1000:
        s=''
        digit = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
        comp = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety','hundred','thousand']
        if (len(str(number))) < 3:
            if number <= 20:
                s+=digit[number]
            else:
                s += comp[(number//10)] + ' ' + digit[(number%10)]
        elif len(str(number)) < 4:
            s += digit[(number//100)] + ' ' + comp[10] 
            if number%100 <= 20 :
                if number%100 != 0:
                    s += ' and ' + digit[number%100]
            else:
                s += ' and ' + comp[((number%100)//10)] + " " + digit[((number%100)%10)]
        else:
            s += digit[1] + " " + comp[11]
        return s
    else:
        return -1


number=999
print(integer_to_english(number))