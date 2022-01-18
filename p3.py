#lex_auth_012693711503400960120
'''
def find_product(num1,num2,num3):
    product=0
    #write your logic here
    if (num1 == 7 or num2 ==7 or num3 == 7):
        if(num1 ==7):
            product = num2 * num3
        elif(num2 == 7):
            product = num3
        else:
            product = -1
        pass
    else:
        product = num1 * num2 * num3
        pass
        
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(1,7,5)
print(product)
'''
#lex_auth_012693711503400960120

def find_product(num1,num2,num3):
    product=0
    #write your logic here
    if num3 == 7:
        product = -1
    elif(num2 == 7):
        product = num3 
    elif(num1 == 7):
        product = num3 * num2
    else:
        product = num2*num3*num1
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(7,6,2)
print(product)