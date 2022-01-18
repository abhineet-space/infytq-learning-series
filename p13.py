#lex_auth_012693763253788672132

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    newlist= [airline[:2]+':'+source[:3]+':'+destination[:3]+":"]
    for i in range(1,no_of_passengers+1,1):
        num = str(100+i)
        ticket_number_list+=[newlist[0]+num]
        #print(newlist[0][-1:])

    #Use the below return statement wherever applicable
    return ticket_number_list[-5:]

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))