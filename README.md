# Virtual Smart-Cart & Billing Engine 🛒

A modular, command-line interface (CLI) retail application built entirely in **pure Python**. This project demonstrates how to manage data state, input validation, dynamic pricing, and system modules using core Python data structures and syntax without relying on external databases or third-party libraries (like Pandas).

## 🚀 Key Features

* **Dynamic Inventory System:** Managed via nested in-memory dictionaries for $O(1)$ item lookup.
* **Smart Cart Management:** Allows users to interactively view, add, and automatically update item quantities in their session cart.
* **Flexible Billing Engine:** Features custom calculation logic using list comprehensions and applies dynamic discounts using Python's `**kwargs` (keyword arguments).
* **Robust Input Validation:** Uses Python's native `match-case` control flow to process user actions safely without application crashes.
* **Modular Architecture:** Explicit separation of data logic (`products.py`) and application runtime (`main.py`) using clean scope resolution checks (`if __name__ == "__main__"`).

---

## 🛠️ Concepts Demonstrated

This repository showcases a strong foundational grasp of intermediate Python syntax:
* **Advanced Data Structures:** Nested dictionaries, lists of dictionaries, and sets.
* **Control Flow:** `match-case` statements, complex conditional loops (`while/break/continue`).
* **Functional Programming:** Argument unpacking, default arguments, and variable-length keyword arguments (`**kwargs`).
* **Data Manipulation:** Inline collection transformations using **List Comprehensions**.
* **Clean Output Formatting:** Advanced F-string padding techniques (`{variable:<10}`) to generate aligned, programmatic tables in the terminal.

---

## 📂 Project Structure

```text
virtual-smart-cart/
│
├── main.py          # Application entry point & interactive UI loop
├── products.py      # Core data storage, lookup logic, and billing algorithms
└── README.md        # Project documentation
