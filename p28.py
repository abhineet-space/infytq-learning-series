'''Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 

Assume that the sentence would begin with a word and there will be only a single space between the words.

Perform case sensitive string operations wherever necessary.

Sample Input

Expected Output

the sun rises in the east

eht snu sesir ni eht stea'''


#lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    #start writing your code here
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    new =[]
    new_list = sentence.split()
    for i, word in enumerate(new_list):
        if (i)%2 == 0:
            new.append(word[::-1])
        else:
            v=[] # to store vowel 
            temp=[] # to store the rest letters temporily
            for x in word:
                if x in vowel:
                    v.append(x)
                else:
                    temp.append(x)
            temp.extend(v)
            new.append("".join(temp))
    return " ".join(new)

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
