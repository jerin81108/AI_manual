class phone():#type of vsriables
    def __init__(self,brand,model,price,chargertype='B TYPE'):
        self.brand=brand
        self.model=model
        self.price=price
        self.chargertype=chargertype

    def diplay(self):
        print('brand:',self.brand)
        print('model:',self.model)
        print('price',self.price)
        print('charger type',self.chargertype)

oneplus=phone('ONEPLUS','CE 3 LITE','22000')
samsung=phone('SAMSUNG','S24 ULTRA','124000') 
print(oneplus.model)
