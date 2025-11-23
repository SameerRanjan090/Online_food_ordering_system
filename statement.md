# Project Statement: Online Food Ordering System

## 1. Problem Definition
In traditional restaurant settings, manual ordering systems often lead to operational inefficiencies. Reliance on pen-and-paper methods or verbal communication results in:
* **Calculation Errors:** Mistakes in billing totals or change.
* **Order mismanagement:** Orders being lost or recorded incorrectly in the kitchen.
* **Lack of Transparency:** Customers have no way to track the status of their meal (whether it is preparing or ready) without constantly asking staff.
* **Inefficient Menu Updates:** Changing the menu requires re-printing physical cards, which is costly and slow.

## 2. Proposed Solution
The **Online Food Ordering System** is a Python-based Command Line Interface (CLI) application designed to digitize and streamline the restaurant workflow. By centralizing the ordering process into a software system, we eliminate manual calculation errors and provide a structured flow for data from the customer to the kitchen.

## 3. Core Objectives
* **Automation:** To automate the calculation of bill totals, reducing human error to zero.
* **Customer Experience:** To provide users with a clear, readable menu and a shopping cart to manage their selection before purchasing.
* **Operational Control:** To give restaurant administrators a secure platform to manage menu items dynamically without physical reprints.
* **Transparency:** To implement an order tracking system where customers can view the real-time status of their specific order using a unique ID.

## 4. Project Scope

### In-Scope
* **Customer Module:** Menu browsing, Cart management (Add/Remove), Checkout, and Status Tracking.
* **Admin Module:** Password-protected entry, Menu creation, and Order status updates.
* **Data Handling:** Runtime storage using Python Lists and Dictionaries to simulate database operations.
* **Bill Generation:** Automated text-based receipt generation.

### Out-of-Scope
* **Payment Gateway:** The system simulates payment; it does not process actual credit cards or bank transactions.
* **Persistent Database:** Data is held in memory for the session; a permanent SQL/NoSQL database is not currently implemented.
* **Graphical User Interface (GUI):** The project operates strictly via the console/terminal.

## 5. Target Audience
* **Restaurant Owners:** Who wish to see a prototype of how digital ordering can assist business logic.
* **Students/Developers:** Seeking to understand Object-Oriented Programming (OOP) implementation in Python, specifically class interactions and state management.
