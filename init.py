class laptop():
    def __init__(self):
    
        self.prize=''
        self.Processor='' 
        self.ram=''
    def display(self):
        print('ram=',self.ram)
        print('processor=',self.Processor)
        print('prize=',self.prize)


hp=laptop()
dell=laptop()
lenovo=laptop()

hp.prize=55000
dell.prize=60000
lenovo.prize=45000

hp.Processor='i7'
dell.Processor='amd ryzen 5'
lenovo.Processor='i5'

hp.ram=16
dell.ram=16
lenovo.ram=8
hp.display()

#empty class creation
class ai():
    pass