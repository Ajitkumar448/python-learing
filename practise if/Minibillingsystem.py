from scipy.__config__ import show


cart = [
    {"item": "Milk", "price": 50, "qty": 2},
    {"item": "Bread", "price": 30, "qty": 1},
    {"item": "Eggs", "price": 10, "qty": 12}
]

def calculate_bill_cart(cart):
    total_bill =0
    for item in cart:
        total_bill += item["price"] *item["qty"]
    return total_bill

def show_bill(cart):
    for item in cart:
        item_total = item["price"] * item["qty"]
    
        print(f"{item['item']} = ₹{item_total}")
show_bill(cart)
calculate_bill = calculate_bill_cart(cart)
print(f'total bill : {calculate_bill}')

def find_expensive_price(cart):
    for item in cart:
        item_total = item["price"] * item["qty"]
        if item_total > 100:
            print(f"{item['item']} ")
find_expensive_price(cart)

