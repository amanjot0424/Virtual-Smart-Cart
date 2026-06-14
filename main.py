from Product import INVENTORY, display_inventory, calculate_final_bill

def show_cart(cart):
    """Displays items currently in the cart."""
    if not cart:
        print("\nYour cart is empty!")
        return

    print("\n==== YOUR CART ====")
    for index, item in enumerate(cart, start=1):
        print(f"{index}. {item['name'].capitalize()} x {item['quantity']}")

def main():
    # In-memory cart: list of dictionaries
    user_cart = []
    
    while True:
        print("\n=== VIRTUAL SMART-CART CONTROLLER ===")
        print("1. View Store Inventory")
        print("2. Add Item to Cart")
        print("3. View Current Cart")
        print("4. Checkout & Generate Bill")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()
        
        # Match-Case Statement
        match choice:
            case "1":
                display_inventory()
                
            case "2":
                display_inventory()
                item_name = input("\nEnter the item name to add: ").lower().strip()
                
                # Membership testing operator ('in')
                if item_name not in INVENTORY:
                    print("❌ Sorry, we don't carry that item!")
                    continue
                    
                qty_input = input(f"How many {item_name}s would you like? ")
                if not qty_input.isdigit() or int(qty_input) <= 0:
                    print("❌ Invalid quantity. Please enter a positive number.")
                    continue
                    
                quantity = int(qty_input)
                
                # Check if item already exists in cart using a list comprehension
                existing_items = [item for item in user_cart if item["name"] == item_name]
                
                if existing_items:
                    existing_items[0]["quantity"] += quantity
                else:
                    user_cart.append({"name": item_name, "quantity": quantity})
                    
                print(f"✅ Added {quantity} {item_name}(s) to your cart.")
                
            case "3":
                show_cart(user_cart)
                
            case "4":
                if not user_cart:
                    print("❌ Your cart is empty. Add items before checking out!")
                    continue
                
                show_cart(user_cart)
                
                # Example of passing keyword arguments (defaulting to 10% off for testing)
                subtotal, final_total = calculate_final_bill(user_cart, discount_percentage=10, flat_coupon=15)
                
                print("\n==========================")
                print(f"Subtotal: ₹{subtotal}")
                print(f"Grand Total (After Discounts): ₹{final_total}")
                print("==========================")
                print("Thank you for shopping with us!")
                break # Exit program after successful checkout
                
            case "5":
                print("Exiting application. Goodbye!")
                break
                
            case _:
                print("❌ Invalid choice! Please select a valid menu option.")

# Scope Resolution check to ensure it only runs when directly executed
if __name__ == "__main__":
    main()