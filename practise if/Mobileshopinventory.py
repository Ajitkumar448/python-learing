mobiles = [
    {"name": "Samsung M35", "price": 18000, "stock": 5},
    {"name": "Redmi Note 14", "price": 15000, "stock": 8},
    {"name": "", "price": 12000, "stock": 4},
    {"name": "iPhone 15", "price": -50000, "stock": 2},
    {"name": "Realme P3", "price": 17000, "stock": 0}
]

def find_invalid_record(name,price,stock):
    constraints = {"name": isinstance(name,str) and len(name.strip())!=0,
                   "price":isinstance(price,int) and price> 0,
                   "stock":isinstance(stock,int) and stock >0 }
    return[key for key,value in constraints.items()if not value]

def show_valid_mobile(mobiles):
    for mobile in mobiles:
        is_invalid = find_invalid_record(**mobile)
        if is_invalid:
            print(f"invalid record:{mobile}")
            for key in is_invalid:
                print(f"{key}: {mobile[key]}")
        else:
            print(f"{mobile['name']} - {mobile['price']}")
def calculate_inventory(mobiles):
    total_value = 0
    for mobile in mobiles:
        is_invalid = find_invalid_record(**mobile)
        if not is_invalid:
            total_value += mobile["price"] * mobile["stock"]

    return total_value
show_valid_mobile(mobiles) 
total_inventory = calculate_inventory(mobiles)
print(f"Total value is {total_inventory}")    
