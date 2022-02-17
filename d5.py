'''Problem Statement
Given two lists, both having String elements, write a python program using python lists to create a new string as per the rule given below:
The first element in list1 should be merged with last element in list2, second element in list1 should be merged with second last element in list2 and so on. If an element in list1/list2 is None, then the corresponding element in the other list should be kept as it is in the merged list. 

Sample Input	Expected Output
 list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']

 list2=['y','tor','e','eps','ay',None,'le','n']

 "An apple a day keeps the doctor away"'''


#lex_auth_0127426166978887681375

def merge_list(list1, list2):
    merged_data=""
    #write your logic here
    le = len(list1)
    for x in range(0,le):
        if list1[x] == None:
            merged_data += list2[-(x+1)]
        elif list2[-(x+1)] == None:
            merged_data += list1[x]
        else:
            merged_data += list1[x] + list2[-(x+1)]
        if x < le-1:
            merged_data += " "

    return merged_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)
