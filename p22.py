'''
A teacher is conducting a camp for a group of five children. Based on their performance and behavior during the camp, the teacher rewards them with chocolates.

Write a Python function to

1. Find the total number of chocolates received by all the children put together.
Assume that each child is identified by an id and it is stored in a tuple and the number of chocolates given to each child is stored in a list.

2. The teacher also rewards a child with few extra chocolates for his/her best conduct during the camp.

If the number of extra chocolates is less than 1, an error message "Extra chocolates is less than 1", should be displayed.

If the given child Id is invalid, an error message "Child id is invalid" should be displayed. Otherwise, the extra chocolates provided for the child must be added to his/her existing number of chocolates and display the list containing the total number of chocolates received by each child.
'''
#lex_auth_01269442027919769669

#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    count = 0
    for i in chocolates_received:
        count +=i
    return count
        

    #Remove pass and write your logic here to find and return the total number of chocolates

def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates < 1:
        print("Extra chocolates is less than 1")
    elif child_id_rewarded not in child_id:
        print('Child id is invalid')
    else:
        for i in range(0,len(child_id),1):
            if child_id[i] == child_id_rewarded:
                chocolates_received[i] = chocolates_received[i] + extra_chocolates
                print(chocolates_received)
    '''else:
        length = len(child_id)
        for num in range(length-1):
            if child_id_rewarded == child_id[num]:
                chocolates_received[num] = chocolates_received[num] + extra_chocolates
        print(chocolates_received)
 '''

    #Remove pass and write your logic here


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("Extra chocolates is less than 1")
    #print("Child id is invalid")
    #print(chocolates_received)


print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(50,2)