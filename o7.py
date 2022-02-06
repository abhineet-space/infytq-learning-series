'''Problem Statement
Write a Python program to generate tickets for online bus booking, based on the class diagram given below.



Method description:

Initialize static variable counter to 0
validate_source_destination(): Validate source and destination. source must always be Delhi and destination can be either Mumbai, Chennai, Pune or Kolkata. If both are valid, return true. Else return false
generate_ticket():
Validate source and destination
If valid, generate ticket id and assign it to attribute, ticket_id.Ticket id should be generated with the first letter of source followed by first letter of destination and an auto-generated value starting from 01 (Ex: DM01, DP02,.. ,DK10,DC11)
Else, set ticket_id as None
Note: Perform case insensitive string comparison


For testing:

Create objects of Ticket class
Invoke generate_ticket() method on Ticket object
Display ticket id, passenger name, source, destination
In case of error/invalid data, display appropriate error message'''

#lex_auth_012748317267525632347
#Start writing your code here
class Ticket:
    counter = 0
    def __init__(self,passenger_name, source, destination):
        self.__passenger_name = passenger_name
        self.__source = source
        self.__destination = destination
        self.__ticket_id = None
        Ticket.counter += 1
    
    def validate_source_destination(self):
        destination_list = ['Mumbai', 'Chennai', 'Pune', 'Kolkata']
        if self.__source.capitalize() == 'Delhi' and self.__destination.capitalize() in destination_list:
            return True
        else:
            return False
    def generate_ticket(self):
        if self.validate_source_destination():
            if Ticket.counter <10:
                self.__ticket_id = str(self.__source[0]) + str(self.__destination[0]) + '0' + str(Ticket.counter)
            else:
                self.__ticket_id = str(self.__source[0]) + str(self.__destination[0]) + str(Ticket.counter)
        else:
            self.__ticket_id = None



    def get_ticket_id(self):
        return self.__ticket_id
    def get_passenger_name(self):
        return self.__passenger_name
    def get_source(self):
        return self.__source
    def get_destination(self):
        return self.__destination
