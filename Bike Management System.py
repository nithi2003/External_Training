class showroom:
    def __init__(self):
        self.bikes = {
            'thunder':[2,'200cc',200000],
            'twins':[4,'250cc',400000],
            'gt':[1,'300cc',500000]
            }
class manager(showroom):
    def display(self):
        return self.bikes
    def specificbike(self,bikename):
        return self.bikes[bikename]
    def sellbikes(self,bikename):
        if bikename in self.bikes:
            if self.bikes[bikename][0]>=1:
                return True
        else:
            return False
    def updatebike(self,bikename):
        if self.sellbikes(bikename)==True:
            if self.bikes[bikename][0]>=1:
                self.bikes[bikename][0]-=1
        return self.bikes
class customer(manager):
    def bikes(self):
        print(self.display())
    def ask(self,bikename):
        print(self.specificbike(bikename))
    def buybike(self,bikename):
        v = self.sellbikes(bikename)
        if v==True:
            print("bought",bikename,self.bikes[bikename])
            return True
        else:
            print("bike not available")
            return False
m = manager()
c = customer()
bikename = input()
c.ask(bikename)
x = c.buybike(bikename)
if x==True:
    y = m.updatebike(bikename)
    print("Available bikes",y)

