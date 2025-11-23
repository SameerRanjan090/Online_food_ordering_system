import time
import random


class MenuItem:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.category}) - Rs.{self.price:.2f}"


class Order:
    def __init__(self, order_id, customer_name, items, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items  # Dictionary: {'Item Name': {'price': float, 'qty': int}}
        self.total_amount = total_amount
        self.status = "Pending"  # Pending -> Preparing -> Ready -> Delivered


class FoodSystem:
    def __init__(self):
        self.menu = []
        self.cart = {}  # {item_name: {'item_obj': MenuItem, 'qty': int}}
        self.orders = []
        self.admin_password = "admin"  # Simple password for menu management

        # Seed some initial data
        self._seed_menu()

    def _seed_menu(self):
        self.menu.append(MenuItem("Margherita Pizza", "Pizza", 12.50))
        self.menu.append(MenuItem("Pepperoni Pizza", "Pizza", 15.00))
        self.menu.append(MenuItem("Cheeseburger", "Burger", 8.50))
        self.menu.append(MenuItem("Veggie Burger", "Burger", 9.00))
        self.menu.append(MenuItem("Coke", "Drinks", 2.00))
        self.menu.append(MenuItem("Fries", "Sides", 3.50))

    # --- Display Methods ---
    def display_menu(self):
        print("\n---Current Menu---")
        print(f"{'ID':<5} {'Name':<20} {'Category':<15} {'Price':<10}")
        print("-" * 50)
        for idx, item in enumerate(self.menu):
            print(f"{idx + 1:<5} {item.name:<20} {item.category:<15} ${item.price:.2f}")
        print("-" * 50)

    def display_cart(self):
        if not self.cart:
            print("\n[!] Your cart is empty.")
            return False

        print("\n---Your Cart ---")
        print(f"{'Name':<20} {'Qty':<10} {'Subtotal':<10}")
        print("-" * 40)
        total = 0
        for name, details in self.cart.items():
            item = details['item_obj']
            qty = details['qty']
            subtotal = item.price * qty
            total += subtotal
            print(f"{name:<20} {qty:<10} ${subtotal:.2f}")
        print("-" * 40)
        print(f"Total: ${total:.2f}")
        return True

    # --- Customer Actions ---
    def add_to_cart(self):
        self.display_menu()
        try:
            choice = int(input("\nEnter Menu ID to add: ")) - 1
            if 0 <= choice < len(self.menu):
                qty = int(input(f"How many {self.menu[choice].name}? "))
                if qty > 0:
                    item = self.menu[choice]
                    if item.name in self.cart:
                        self.cart[item.name]['qty'] += qty
                    else:
                        self.cart[item.name] = {'item_obj': item, 'qty': qty}
                    print(f"Added {qty} x {item.name} to cart.")
                else:
                    print("[!] Quantity must be greater than 0.")
            else:
                print("[!] Invalid Menu ID.")
        except ValueError:
            print("[!] Please enter valid numbers.")

    def remove_from_cart(self):
        if not self.display_cart(): return

        name = input("\nEnter the exact name of the item to remove: ")
        if name in self.cart:
            del self.cart[name]
            print(f"Removed {name} from cart.")
        else:
            print("[!] Item not found in cart.")

    def checkout(self):
        if not self.cart:
            print("[!] Cart is empty. Cannot checkout.")
            return

        print("\n---Checkout Process ---")
        self.display_cart()
        confirm = input("Confirm order? (y/n): ").lower()

        if confirm == 'y':
            customer_name = input("Enter your name: ")
            total = sum(i['item_obj'].price * i['qty'] for i in self.cart.values())

            # Create simplified cart snapshot for the order history
            order_items = {k: {'price': v['item_obj'].price, 'qty': v['qty']} for k, v in self.cart.items()}

            new_order = Order(random.randint(1000, 9999), customer_name, order_items, total)
            self.orders.append(new_order)

            # Generate Receipt
            print("\n" + "=" * 30)
            print(f"   RECEIPT - Order #{new_order.order_id}")
            print("=" * 30)
            print(f"Customer: {customer_name}")
            for name, details in self.cart.items():
                print(f"{name} x{details['qty']} ... ${details['item_obj'].price * details['qty']:.2f}")
            print("-" * 30)
            print(f"TOTAL PAID: ${total:.2f}")
            print("=" * 30)
            print("Order Placed Successfully!")

            self.cart = {}  # Clear cart
        else:
            print("Checkout cancelled.")

    def view_order_status(self):
        order_id = input("Enter your Order ID: ")
        try:
            order_id = int(order_id)
            found = False
            for order in self.orders:
                if order.order_id == order_id:
                    print(f"\nOrder #{order_id} Status: [{order.status}]")
                    print(f"Items: {list(order.items.keys())}")
                    found = True
                    break
            if not found:
                print("[!] Order ID not found.")
        except ValueError:
            print("[!] Invalid ID format.")

    # --- Admin Actions (Menu Management) ---
    def admin_menu(self):
        pwd = input("Enter Admin Password: ")
        if pwd != self.admin_password:
            print("Access Denied.")
            return

        while True:
            print("\n---Admin Panel ---")
            print("1. Add Menu Item")
            print("2. View All Orders")
            print("3. Update Order Status")
            print("4. Back to Main Menu")

            choice = input("Select: ")

            if choice == '1':
                name = input("Item Name: ")
                cat = input("Category: ")
                try:
                    price = float(input("Price: "))
                    self.menu.append(MenuItem(name, cat, price))
                    print("Item added to menu.")
                except ValueError:
                    print("[!] Invalid price.")

            elif choice == '2':
                print("\n--- Active Orders ---")
                for order in self.orders:
                    print(
                        f"ID: {order.order_id} | Name: {order.customer_name} | Total: ${order.total_amount:.2f} | Status: {order.status}")

            elif choice == '3':
                try:
                    oid = int(input("Enter Order ID to update: "))
                    found = False
                    for order in self.orders:
                        if order.order_id == oid:
                            new_status = input("Enter new status (e.g., Preparing, Delivered): ")
                            order.status = new_status
                            print("Status updated.")
                            found = True
                            break
                    if not found: print("Order not found.")
                except ValueError:
                    print("Invalid input.")

            elif choice == '4':
                break

    # --- Main Loop ---
    def run(self):
        while True:
            print("\n===ONLINE FOOD ORDERING SYSTEM ===")
            print("1. View Menu")
            print("2. Add Item to Cart")
            print("3. View Cart / Remove Item")
            print("4. Checkout")
            print("5. Track Order Status")
            print("6. Admin Login (Manage Menu/Orders)")
            print("7. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.display_menu()
            elif choice == '2':
                self.add_to_cart()
            elif choice == '3':
                self.display_cart()
                if self.cart:
                    if input("Remove an item? (y/n): ").lower() == 'y':
                        self.remove_from_cart()
            elif choice == '4':
                self.checkout()
            elif choice == '5':
                self.view_order_status()
            elif choice == '6':
                self.admin_menu()
            elif choice == '7':
                print("Thank you for ordering! Goodbye.")
                break
            else:
                print("[!] Invalid choice.")


if __name__ == "__main__":
    app = FoodSystem()
    app.run()
