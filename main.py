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
        print("3.5 Remove items from Cart")
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

            case "3.5":
                
                show_cart(user_cart)
                
                if not user_cart:
                    print("❌ Your cart is empty!")
                    continue
                    
                Removing_item = input("Select the Item to Remove: ").strip().lower()
                cart_names = [item["name"] for item in user_cart]
                
                # This will tell us exactly what Python sees
                print(f"-> Look closely! Your cart actually contains: {cart_names}")
                print(f"-> You tried to match it with: '{Removing_item}'")
                
                if Removing_item not in cart_names:
                    print("❌ Sorry, You don't have that item!")
                    continue
                else:
                    target_item = [item for item in user_cart if item["name"] == Removing_item][0]
                    print("1. Reduce the Quantity of the Item")
                    print("2. Completely Remove the Item")
                    
                    select_input = input("Select the Option (1-2): ").strip()
                    match select_input:
                        case "1":
                            qty_input = input("How much quantity you want to reduce: ").strip()
                            if qty_input.isdigit():
                                quantity_to_reduce = int(qty_input)
                                target_item["quantity"] -= quantity_to_reduce
                                print(f"✅ Reduced quantity of {Removing_item.capitalize()} by {quantity_to_reduce}.")
                                
                                if target_item["quantity"] <= 0:
                                    user_cart.remove(target_item)
                                    print(f"✅ {Removing_item.capitalize()} is now completely removed.")
                            else:
                                print("❌ Invalid quantity.")
                        case "2":
                            user_cart.remove(target_item)
                            print(f"✅ Completely removed {Removing_item.capitalize()} from your cart.")
                        case _:
                            print("❌ Invalid option choice.")
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