import math



class Item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        self.average=price/quantity
        self.discount=math.modf(price)
    # def calculate_Total_Price(self,price,quantity):
    #     return price * quantity
    # def calculate_Average(self,arr):
    #     sum=0
    #     for i in arr:
    #         sum+=i
    #     return sum/ len(arr)
    # pass is the key like when nothing presents
#print(item1.calculate_Total_Price(item1.price,item1.quantity))
# item2=Item('Clock')
# item2.price=400
# item2.quantity=20
# print(item2.calculate_Total_Price(item2.price,item2.quantity))
# print(item2.calculate_Average([0,00,0,00,0,0,0,0,0,0,1]))
# item3=Item("Car")
item1=Item("Phone",400,5)
item2=Item("Clock",300,90)

print(item1.name,item1.price,item1.quantity,round(item1.average,2),item1.discount)
print(item2.name,item2.price,item2.quantity,round(item2.average,2),item2.discount)

