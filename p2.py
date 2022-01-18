def find_sum_of_digits(number):
    sum_of_digits=0
    #Write your logic here
    temp = number
    while(temp>0):
        sum_of_digits =sum_of_digits + (temp%10)
        temp = temp//10
    
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
                                          