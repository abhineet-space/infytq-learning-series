'''Problem Statement
Go through the algorithm for solving the Tower of Hanoi problem. 
'''

def tower_of_hanoi(n, source,destination,temp):
    if n==0:  #stopping condition
        return
    tower_of_hanoi(n-1,source,temp,destination) # moving from source to temp using dest
    data = source.pop(0)        # moving from source to dest
    destination.insert(0,data)
    tower_of_hanoi(n-1,temp,destination,source) #moving from temp to dest using start as temp
    #return


source=["blue","green","orange","red","yellow","black"]
destination=[]
temp=[]
tower_of_hanoi(6, source, destination, temp)
print("Source:",source)
print("Destination:",destination)