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

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        #pass
        #Remove pass and copy the code you had written to add an element.
        new_node = Node(data)
        if self.__head == None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node
    
    def display(self):
        #pass
        #Remove pass and copy the code you had written to display the element(s).
        temp = self.__head
        while temp != None:
            print(temp.get_data())
            temp = temp.get_next()
    
    def find_node(self,data):
        #pass
        #Remove pass and copy the code you had written to find the node containing the element.
        temp = self.__head
        while temp != None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None
    
    def insert(self,data,data_before):
        #pass
        #Remove pass and write the logic to insert an element.
        new_node = Node(data)
        if data_before is None:
            self.__head = self.__tail = new_node
        else:
            temp = LinkedList.find_node(self,data_before)
            if temp != None:
                new_node.set_next(temp.get_next())
                temp = temp.set_next(new_node)
            else:
                print("Node not Found")
                                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


#list1=LinkedList()
#Add all the required element(s)
#Insert the element in the required position
#list1.insert("NewItem","Sugar")
#list1.display()

list1=LinkedList()
#Add all the required element(s)
list1.add("Milk")
list1.add("Salt")
list1.add("Biscuit")
list1.add("Apple")
list1.add("Sugar")
list1.add("Juice")
list1.add("Pomegranate")
list1.add("Watermelon")
list1.display()
list1.insert("NewItem","Sugar")
#Search for the required node
print("-----------------")
list1.display()
print("-----------------")
list2=LinkedList()
list2.display()
list2.insert("NewItem","Sugar")
list2.display()
print("-----------------")
list2.insert("NewItem","Sugar")
list2.display()
                                              