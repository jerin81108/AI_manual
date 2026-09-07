class laptop(): #insatnce method
    def __init__(self):
        self.brand=''
        self.price=34
    def setprice(self,price):
        self.price=price
        print(self.price)
    def setbrand(self,brand):
        self.brand=brand
        print(self.brand)
hp=laptop()

hp.setprice(55000)
hp.setbrand('asus')