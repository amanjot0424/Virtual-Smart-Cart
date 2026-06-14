# Global constant inventory (Dictionary of Dictionaries)
INVENTORY = {
    "apple": {"price": 20, "category": "fruits"},
    "banana": {"price": 10, "category": "fruits"},
    "milk": {"price": 50, "category": "dairy"},
    "bread": {"price": 40, "category": "bakery"},
    "maggi": {"price": 14, "category": "snacks"}
}

def display_inventory():
    """Prints the available items in a clean format."""
    print("\n==== AVAILABLE ITEMS ====")
    print(f"{'Item':<10} | {'Price (₹)':<10} | {'Category':<10}")
    print("-" * 38)
    for item, details in INVENTORY.items():
        print(f"{item.capitalize():<10} | {details['price']:<10} | {details['category']:<10}")

def calculate_final_bill(cart, **discounts):
    """
    Calculates total price using a list comprehension.
    Applies flexible discounts using **kwargs (keyword arguments).
    """
    # List comprehension to get the cost of each item based on its quantity
    item_totals = [INVENTORY[item['name']]['price'] * item['quantity'] for item in cart]
    subtotal = sum(item_totals)
    
    total = subtotal
    
    # Handling keyword arguments dynamically
    if "discount_percentage" in discounts:
        pct = discounts["discount_percentage"]
        total -= (subtotal * (pct / 100))
        print(f"Applied {pct}% discount!")
        
    if "flat_coupon" in discounts:
        coupon = discounts["flat_coupon"]
        total -= coupon
        print(f"Applied flat ₹{coupon} coupon!")
        
    # Prevent negative total just in case
    total = max(0, total)
    
    return subtotal, total