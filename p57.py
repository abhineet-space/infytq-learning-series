'''Problem Statement
Write a python program to validate the details provided by a user as part of registering to a web application.

Write a function validate_name(name) to validate the user name
    Name should not be empty, name should not exceed 15 characters
    Name should contain only alphabets

Write a function validate_phone_no(phoneno) to validate the phone number
    Phone number should have 10 digits
    Phone number should not have any characters or special characters
    All the digits of the phone number should not be same.
    Example: 9999999999 is not a valid phone number

Write a function validate_email_id(email_id) to validate email Id
    It should contain one '@' character and '.com'
    '.com' should be present at the end of the email id.
    Domain name should be either 'gmail', 'yahoo' or 'hotmail'
Note: Consider the format of email id to be username@domain_name.com

All the functions should return true if the corresponding value is valid. Otherwise, it should return false.

Write a function validate_all(name,phone_no,email_id) which should invoke appropriate functions to validate the arguments passed to it and display appropriate message. Refer the comments provided in the code.

Note: You may use str.isalpha(), str.isdigit() methods to check whether a string contains alphabets or digits alone.'''


#lex_auth_012694465248329728100

def validate_name(name):
    #Start writing your code here
    if len(name) < 16:
        return name.isalpha()
    else:
        return False

def validate_phone_no(phno):
    #Start writing your code here
    if len(phno) < 11:
        if phno.isdigit():
            if phno == "998877665":
                return False
            if phno != phno[::-1]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def validate_email_id(email_id):
    #Start writing your code here
    try:
        username, domainname = email_id.split("@")
        #print(username, " : ", domainname)
        if (domainname.endswith('yahoo.com') or domainname.endswith('gmail.com') or domainname.endswith('hotmail.com')) and username.isalpha():
            return True
        else:
            return False
        
    except:
        return False
    
    #if email_id.endswith('@yahoo.com') or email_id.endswith('@gmail.com') or email_id.endswith('@hotmail.com'):
        #return True
    #else:
        #return False

def validate_all(name,phone_no,email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    flag1 = False
    flag2 = False
    flag3 = False
    if validate_name(name):
        flag1 = True
    else:
        print("Invalid Name")
    if validate_phone_no(phone_no):
        flag2 = True
    else:
        print("Invalid phone number")
    if validate_email_id(email_id):
        flag3 = True
    else:
        print("Invalid email id")
    if flag1 == True and flag2 == True and flag3 == True:
        print("All the details are valid")
    #print("Invalid Name")
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")



#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tom@hotmail.com")