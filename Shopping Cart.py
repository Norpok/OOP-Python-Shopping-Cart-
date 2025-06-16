class Items:
    listOfItems = []

    def __init__(self, name, price, quantity, discount=1):
        self.name = name
        self.price = price
        self.discount = discount if discount else 1
        self.quantity = quantity

    def final_price(self):
        return self.price * self.discount

    def addToShelf(self):
        Items.listOfItems.append(self)


class Cart:
    def __init__(self, S_no):
        self.S_no = S_no
        self.Item_list = []
        self.total_price = 0

    def addToCart(self, item_name):
        for item in Items.listOfItems:
            if item.name.lower() == item_name.lower() and item.quantity > 0:
                if len(self.Item_list) < 10:
                    print(f"{item.name} is available and added to cart.")
                    self.Item_list.append(item)
                    item.quantity -= 1
                    return
                else:
                    print("Cart is full. Cannot add more items.")
                    return
        print("Product not available or out of stock.")

    def removeItems(self, item_name):
        for item in self.Item_list:
            if item.name.lower() == item_name.lower():
                self.Item_list.remove(item)
                item.quantity += 1
                print(f"{item.name} removed from cart and restocked.")
                return
        print("Item not found in cart.")

    def TotalPrice(self):
        self.total_price = 0
        for item in self.Item_list:
            self.total_price += item.final_price()
        print(f"Total Price of items in cart: ₹{self.total_price:.2f}")


class User:
    def __init__(self, name, cart):
        self.name = name
        self.cart = cart

    def showItems(self):
        if not self.cart.Item_list:
            print(f"{self.name}'s cart is empty.")
        else:
            print(f"\n{self.name}'s Cart:")
            for item in self.cart.Item_list:
                print(f"- {item.name} | ₹{item.final_price():.2f}")



pencil = Items("Pencil", 2, 5)
eraser = Items("Eraser", 5, 10, 0.5)
pen = Items("Pen", 10, 3)


pencil.addToShelf()
eraser.addToShelf()
pen.addToShelf()

cart1 = Cart(S_no=1)
user1 = User("Aadi", cart1)

while True:
    print("\n1. Show available items")
    print("2. Add item to cart")
    print("3. Remove item from cart")
    print("4. View cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Choose an option: ")

    match choice:
        case "1":
            print("\nAvailable Items on Shelf:")
            for item in Items.listOfItems:
                print(f"- {item.name} | ₹{item.final_price():.2f} | Stock: {item.quantity}")
        case "2":
            item_name = input("Enter the item name to add: ")
            cart1.addToCart(item_name)
        case "3":
            item_name = input("Enter the item name to remove: ")
            cart1.removeItems(item_name)
        case "4":
            user1.showItems()
        case "5":
            cart1.TotalPrice()
        case "6":
            print("Thanks for shopping. Goodbye!")
            break
        case _:
            print("Invalid option. Try again.")
