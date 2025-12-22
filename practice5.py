class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price > ord2.price

ord1 = Order("chips",20)
ord2 = Order("nachos",40)

print(ord1  >  ord2)

# __gt__ dunder function for comparision