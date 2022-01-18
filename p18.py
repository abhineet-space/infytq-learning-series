#lex_auth_012693795044450304151

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    count =0
    for i in reqd_gems:
        for j in gems_list:
            if i == j:
                count +=1
    if count != len(reqd_gems):
        bill_amount = -1
        return bill_amount
    #Write your logic here
    else:
        for i in range(0,len(reqd_gems),1):
            for j in range (0,len(gems_list),1):
                if reqd_gems[i] == gems_list[j]:
                    bill_amount += price_list[j]*reqd_quantity[i]
                    #list1.append(j)
        #print(list1)
        if bill_amount > 30000:
            bill_amount = bill_amount - (0.05*bill_amount)
        if bill_amount == 0:
            bill_amount = -1
        return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)