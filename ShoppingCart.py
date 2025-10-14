class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self,item_name,qty):
        item = (item_name,qty)
        self.items.append(item)

    def remove_item(self,item_name):

      for item in self.items:
          if item[0] == item_name:
              self.items.remove(item)
              break

    def calculate_total(self):
        total = 0
        for item in self.items:
          total += item[1]
        return total
#driver code
cart = ShoppingCart()
#Add items to the shopping cart
cart.add_item("Banana",50)
cart.add_item("Mango",60)
cart.add_item("Orange",40)
    
