class a():
    def __init__(self):
        print('A')
    def display(self):
        print('u are in clas a')
class b():
    def __init__(self):
        super().__init__
        print('B')
    def display(self):
        print('u are in B ')

class c(b,a):
    def __init__(self):
        super().__init__
        print('C')
    def display(self):
        print('u are in C ')

ob=c()
ob.display()