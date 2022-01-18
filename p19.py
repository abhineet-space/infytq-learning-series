#lex_auth_01269441913243238467

def create_largest_number(number_list):
    num=""
    number_list.sort()
    for i in range(-1,-len(number_list)-1,-1):
        num+=str(number_list[i])
    return int(num)
number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)