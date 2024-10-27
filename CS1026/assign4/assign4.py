# Author: Ghala Basaad
# Student Number: 251384549
# Description: This file contains the implementation of classes related to product management, including Product, Inventory, ShoppingCart, and ProductCatalog.
# Each class has specific functionalities for managing products, inventory, shopping carts, and product catalogs.

class Product:
    def __init__(self, name, price, category):
        # Initialize product attributes
        self._name = name
        self._price = price
        self._category = category

    # Define how products are classified
    def __eq__(self, other):
         if isinstance(other, Product):
             if  ((self._name == other._name and self._price == other._price) and (self._category==other._category)):
                return True
             else:
                return False
         else:
            return False

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_category(self):
        return self._category

    # Implement string representation
    def __repr__(self):
        rep = 'Product(' + self._name + ',' + str(self._price) + ',' + self._category + ')'
        return rep

class Inventory:
    def __init__(self):
        # Initialize an empty inventory dictionary
        self._dict = {}


    def add_to_productInventory(self, productName, productPrice, productQuantity):
        # Add a product to the inventory with its price and quantity
        self._dict[productName] = [productPrice, productQuantity]


    def add_productQuantity(self, nameProduct, addQuantity):
        # Add quantity to an existing product in the inventory
        self._dict[nameProduct][1] += addQuantity


    def remove_productQuantity(self, nameProduct, removeQuantity):
        # Remove quantity from an existing product in the inventory
        self._dict[nameProduct][1] -= removeQuantity


    def get_productPrice(self, nameProduct):
        # Get the price of a specific product in the inventory
        return self._dict[nameProduct][0]


    def get_productQuantity(self, nameProduct):
        # Get the quantity of a specific product in the inventory
         return self._dict[nameProduct][1]


    def display_Inventory(self):
        # Display the current inventory
        inventory_display = []
        for item in self._dict:
           inventory_display.append(f"{item}, {int(self._dict[item][0])}, {self._dict[item][1]}")
        print('\n'.join(inventory_display))


class  ShoppingCart:
    def __init__(self, buyerName, inventory):
        # Initialize a shopping cart with a buyer's name and an inventory
        self._buyerName = buyerName
        self._inventory = inventory
        self._cart = {}


    def add_to_cart(self, nameProduct, requestedQuantity):
        # Add a product to the shopping cart with the requested quantity
        if self._inventory.get_productQuantity(nameProduct) < requestedQuantity:
            # If not enough quantity is available, return a message
            return "Can not fill the order"
        else:
            if nameProduct not in self._cart:
                # If the product is not in the cart, add it with the requested quantity
                self._cart[nameProduct] = requestedQuantity
            else:
                # If the product is already in the cart, increase the quantity
                self._cart[nameProduct] += requestedQuantity
            self._inventory.remove_productQuantity(nameProduct, requestedQuantity)
            return "Filled the order"


    def remove_from_cart(self, nameProduct, requestedQuantity):
        # Remove a product from the shopping cart with the requested quantity
        if nameProduct not in self._inventory._dict:
            # If the product is not in the cart, return a message
            return "Product not in the cart"
        elif requestedQuantity > self._inventory.get_productQuantity(nameProduct):
            # If the requested quantity exceeds what is in the cart, return a message
            return "The requested quantity to be removed from cart exceeds what is in the cart"
        else:
            self._cart[nameProduct] -= requestedQuantity
            self._inventory.add_productQuantity(nameProduct, requestedQuantity)
            return "Successful"


    def view_cart(self):
        # View the contents and total price of the shopping cart
        cart_items = []
        total = 0
        for item, details in self._cart.items():
            cart_items.append(f"{item} {details}")
            # Update the total price by multiplying the item's price with its quantity
            total += self._inventory.get_productPrice(item) * details

        result = '\n'.join(cart_items)
        result += f"\nTotal: {int(total)}\nBuyer Name: {self._buyerName}"
        print(result)

class ProductCatalog:
    def __init__(self):
        # Initialize an empty product catalog with sets for low, medium, and high-priced items
        self._catalog = {}
        self._low_prices = set()
        self._medium_prices = set()
        self._highPrices = set()


    def addProduct(self, product):
        # Add a product to the catalog
        self._catalog[product.get_name()] = [product.get_price(),product.get_category()]


    def price_category(self):
        # Categorize products in the catalog based on price ranges and display the count of each category
        for product in self._catalog:
            price = self._catalog[product][0]
            if 0 <= price <= 99:
                self._low_prices.add(product)
            elif 100 <= price <= 499:
                self._medium_prices.add(product)
            elif price >= 500:
                self._highPrices.add(product)
        print(f"Number of low price items: {len(self._low_prices)}\nNumber of medium price items: {len(self._medium_prices)}\nNumber of high price items: {len(self._highPrices)}")


    def display_catalog(self):
        # Display the products in the catalog with their prices and categories
        for product in self._catalog:
            print(f"Product: {product} Price: {int(self._catalog[product][0])} Category: {self._catalog[product][1]}")

def populate_inventory(filename):
    # Populate an inventory with product information from a file.
    try:
        with open(filename, 'r') as file:
            inventory = Inventory()
            for line in file:
                data = line.strip().split(',')
                name, price, quantity, category = data[0], float(data[1]), int(data[2]), data[3]
                inventory.add_to_productInventory(name, price, quantity)
            return inventory
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Could not read file: {filename}")


def populate_catalog(fileName):
    # Populate a product catalog with product information from a file.
    try:
        with open(fileName, 'r') as file:
            catalog = ProductCatalog()
            for line in file:
                data = line.strip().split(',')
                name, price, quantity, category = data[0], float(data[1]), int(data[2]), data[3]
                product = Product(name, price, category)
                catalog.addProduct(product)
            return catalog
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Could not read file: {fileName}")


