#lex_auth_012693813706604544157
def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    if ((num1 and num2) > 9) and ((num1 and num2) < 100):
        if num1 < num2:
            if num1 % 5 == 0 and num2 % 5 == 0:
                if ((num1//10) + (num1%10))%3 == 0 and ((num2//10) + (num2%10))% 3 ==0:
                    max_num = num2
            

    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)

def find_max(num1, num2):
    max_num=-1
    if(num1!=num2):
        for i in range(num1,num2+1,1):
            if(i%5==0 and i/100<1):
                sum_digit=0
                num=i
                while(num!=0):
                    rem=num%10
                    sum_digit+=rem
                    num//=10
                if(sum_digit%3==0):
                    max_num=i
                    
    return max_num