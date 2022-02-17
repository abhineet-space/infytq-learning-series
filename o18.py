# Not Complete
'''________________________________________________________'''
#lex_auth_0127475574441738242319
#Start writing your code here
class rider:
    def __init__(self,trained_status,experience):
        self.__trained_status = trained_status
        self.__experience = experience
    def rides_vehicle(self):
        if self.__trained_status == True and self.__experience > 0:
            return True
        else:
            return False

class bikeRider(rider):
    def __init__(self,trained_status,experience,race_license):
        super().__init__(self,trained_status,experience)
        self.__race_license = race_license

    def rides_in_dome(self):
        pass
class cycleRider(rider):
    def rides_blindfolded(self):
        pass
'''________________________________________________________'''