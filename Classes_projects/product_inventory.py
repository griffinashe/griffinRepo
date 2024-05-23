"""
Create an application which manages an inventory of products. 
Create a product class which has a price, id, and quantity on hand.  
Then create an inventory class which keeps track of various products and 
can sum up the inventory.
"""
class Product:
    def __init__(self, id, price, quantity):
        self.id = id
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.id] = product

    def sum_inventory(self):
        return sum(product.price * product.quantity for product in self.products.values())

# Placeholders for testing
