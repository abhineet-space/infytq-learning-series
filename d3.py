class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node

'''add(data)
1. Create a new node with the data
2. If the linked list is empty (head node is not referring to any other node), 
   make the head node and the tail node refer to the new node
3. Otherwise,
   a. Make the tail node’s link refer to new node
   b. Call the new node as tail node
'''
"""display()
1. Call the head node as temp
2. While temp is not None,
   a. Display temp’s data
   b. Make the next node as temp
"""
class LinkedList:
    def __init__(self):
        self.__head= None
        self.__tail= None
    def get_head(self):
        return self.__head
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        #pass
        #Remove pass and write the logic to add an element
        new_node = Node(data)
        if self.__head == None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node
    def display(self):
        #pass
        #Remove pass and write the logic to display the elements
        temp = self.__head
        while temp != None:
            print(temp.get_data())
            temp = temp.get_next()

    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg

list1=LinkedList()
list1.add("Sugar")
list1.add("Sugar")
list1.add("Sugar")
list1.add("Sugar")
list1.add("Apple")
print("Element added successfully")
list1.display()