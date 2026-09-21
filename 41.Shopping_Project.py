# Shopping Cart Project

class ShoppingCart:
    class Product:
        def __init__(self,name,price,quantity):
            self.name=name
            self.price=price
            self.quantity=quantity
        def total(self):
            return self.price*self.quantity
        def __init__(self):
            self.cart=[]
        def add_product(self):
            name=input("enter product name:")
            price=int(input("enter product price:"))
            quantity=int(input("enter product quantity:"))

            p=self.Product(name,price,quantity)
            self.cart.append(p)
            print("Product added successfully")

        def show_cart(self):
            for c in self.cart:
                print(c.name,c.price,c.quantity,c.total())
shop = ShoppingCart()
shop.add_product()
shop.show_cart()