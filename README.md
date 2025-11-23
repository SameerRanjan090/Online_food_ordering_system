# Online_food_ordering_system
The script implements a console-based Python food ordering system. It uses OOP (MenuItem, Order) to manage the menu, cart, and order status. Features include customer ordering, receipt generation, and an Admin Panel for menu and status updates.

# Online Food Ordering System (CLI)

## Overview of the project
This project is a console-based Python application designed to simulate an online food ordering platform. It serves as a comprehensive demonstration of Object-Oriented Programming (OOP) principles, managing the interaction between customers, orders, and administrative restaurant tasks.

The system allows users to browse a menu, manage a shopping cart, place orders with receipt generation, and track the real-time status of their food. Simultaneously, it includes a secured Admin Panel that allows restaurant staff to dynamically add new menu items and update the status of active orders (e.g., moving an order from "Pending" to "Delivered").

## Features

### Customer Module
* **Dynamic Menu Display:** View current food items categorized by type (Pizza, Burger, Drinks, etc.) with prices.
* **Cart Management:**
    * Add items by ID and specify quantity.
    * View cart sub-totals and grand totals.
    * Remove specific items from the cart before checkout.
* **Checkout System:**
    * Customer name input.
    * Instant receipt generation with a unique **Order ID**.
* **Order Tracking:** Check the live status of an order using the unique Order ID.

### Admin Module
* **Authentication:** Password-protected entry (Default Password: `admin`).
* **Menu Management:** Add new items to the menu (Name, Category, Price) during runtime.
* **Order Fulfillment:** View a list of all active orders and update their status (e.g., Pending → Preparing → Ready).

## Technologies/tools used
* **Language:** Python 3.x
* **Libraries:**
    * `random` (Used for generating unique Order IDs)
    * `time` (Imported for potential future timestamp extensions)
* **Interface:** Command Line Interface (CLI) / Terminal

## Steps to install & run the project

1.  **Prerequisites:** Ensure you have Python installed on your system. You can verify this by typing `python --version` in your terminal.
2.  **Download:** Download the source code file (e.g., `food_ordering.py`) to a local directory.
3.  **Run:** Open your terminal or command prompt, navigate to the directory, and run the following command:


*(Note: Replace `food_ordering.py` with whatever name you saved the python file as).*

## Instructions for testing

Follow this workflow to test all features of the application:

### Phase 1: The Customer Experience

1.  **View Menu:** Run the app and select **Option 1**. Observe the default menu items (Pizzas, Burgers, etc.).
2.  **Add to Cart:** Select **Option 2**. Enter the ID `1` (Margherita Pizza) and Quantity `2`.
3.  **View Cart:** Select **Option 3** to see your current total.
4.  **Checkout:**
      * Select **Option 4**.
      * Confirm with `y`.
      * Enter your name (e.g., "John").
      * **IMPORTANT:** Write down the **Order ID** shown on the receipt (e.g., `1234`).

### Phase 2: The Tracking Experience

1.  **Check Status:** Select **Option 5**.
2.  **Input ID:** Enter the Order ID you wrote down in Phase 1.
3.  **Verify:** The system should show the status as `[Pending]`.

### Phase 3: The Admin Experience

1.  **Login:** Select **Option 6**.
2.  **Auth:** Enter the password: `admin`
3.  **View Orders:** inside the Admin menu, select **Option 2**. You should see "John's" order listed there.
4.  **Update Status:**
      * Select **Option 3**.
      * Enter the Order ID from Phase 1.
      * Type the new status: `Delivered`.
5.  **Verify Update:** Exit the admin menu (Option 4), then use the Customer Tracking (Option 5) again to see that the status has changed to `[Delivered]`.
