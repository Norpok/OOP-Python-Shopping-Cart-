# 🛒 OOP-Based Shopping Cart in Python

This is a basic **Object-Oriented Python project** simulating a shopping cart system using three main classes: `Items`, `Cart`, and `User`.

---

## 📌 Features

- Add/remove items from a virtual shelf
- Maintain cart with a limit of 10 items
- Real-time stock updates
- Dynamic total price calculation with discounts
- Clean CLI interface with menu options

---

## 🧱 Classes and Structure

### 1. `Items`
- Represents a product with attributes like `name`, `price`, `quantity`, and `discount`.
- Stored in a shared class-level list (`listOfItems`).
- Automatically updates shelf when added.

### 2. `Cart`
- Tracks a user's selected items.
- Handles addition/removal of items with inventory sync.
- Calculates total discounted price.

### 3. `User`
- Owns a cart and can view its contents.

---

## 🖥️ Sample Menu

```text
1. Show available items
2. Add item to cart
3. Remove item from cart
4. View cart
5. Checkout
6. Exit
