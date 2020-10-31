#Dang Nguyen
#ID 1861688

class ItemToPurchase:

    def __init__(self, item_name='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        string = '{0} {1} @ ${2} = ${3}'.format(self.item_name, self.item_quantity, self.item_price, (self.item_quantity * self.item_price))
        cost = self.item_quantity * self.item_price
        return string, cost

if __name__ == "__main__":
    
    print("Item 1")
    name = input("Enter the item name:\n")
    price = int(input("Enter the item price:\n"))
    quant = int(input("Enter the item quantity:\n"))
    ob1 = ItemToPurchase(name,price,quant)
    
    print("\nItem 2")
    name = input("Enter the item name:\n")
    price = int(input("Enter the item price:\n"))
    quant = int(input("Enter the item quantity:\n"))
    ob2 = ItemToPurchase(name,price,quant) 
    
    print("\nTOTAL COST")
    str1, cost1 = ob1.print_item_cost()
    str2, cost2 = ob2.print_item_cost()
    print(str1)
    print(str2)
    print('\nTotal: ${}'.format(cost1 + cost2))