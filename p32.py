'''Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.

Rules:

The word should have the largest frequency.

In case multiple words have the same frequency, then choose the word that has the maximum length.

Assumptions:

The text has no special characters other than space.

The text would begin with a word and there will be only a single space between the words.

Perform case insensitive string comparisons wherever necessary.

Sample Input

Expected Output

"Work like you do not need money love like you have never been hurt and dance like no one is watching"

like 3

"Courage is not the absence of fear but rather the judgement that something else is more important than fear"

fear 2

'''

#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word=""
    frequency=0

    #start writing your code here
    #Populate the variables: word and frequency
    data= data.split()

    newData = []
    for i in data:
        if i not in newData:
            newData.append(i)    
    list1=[]
    list2=[]
    for i in newData:
        count = 0
        for j in data:
            if i.lower() == j.lower():
                count += 1
        list1.append(i)
        list2.append(count)
    a = list2.index(max(list2))
    word = list1[a]
    frequency = list2[a]




    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print(word,frequency)


#Provide different values for data and test your program.
data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)