#lex_auth_012693819159732224162

def check_palindrome(word):
    temp=''
    #Remove pass and write your logic here
    for i in range (-1, -len(word)-1,-1):
        temp = temp+word[i]
    if temp == word:
        return True
    else:
        return False

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")