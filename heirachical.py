class dad():
    def phone (self):
        print("dad's phone")
class mom(dad):
    def sweet(self):
        print('sweet is tasty')
class son(dad):
    def lap(self):
        print("son's laptop")


ram=son()
mo=mom()
ram.lap()
ram.phone()
mo.sweet()