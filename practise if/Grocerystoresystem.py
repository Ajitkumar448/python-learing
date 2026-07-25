products = [
    {"name": "Milk", "price": 50, "stock": 10},
    {"name": "Bread", "price": 30, "stock": 5},
    {"name": "", "price": 20, "stock": 8},
    {"name": "Eggs", "price": -10, "stock": 12},
    {"name": "Rice", "price": 60, "stock": 0}
]
def find_invalid_products(name, price, stock):
    constraints = { 
        "name" : isinstance (name,str) and len(name) >0,
                   "price" :isinstance (price,int) and price > 0,
                   "stock" : isinstance( stock,int) and stock > 0
    }

    return[key for key,value in constraints . items()if not value]
         
def show_valid_product(product):
     for product in products:
        invalid_records = find_invalid_products(**product)
        if invalid_records:
            print(f"Invalid product: {product}")
            for key in invalid_records:
                print(f" - {key}: {product[key]}")
        else:
            print(f"Valid product: {product}")
def calculate_inventory_value(product):
    total_value = 0
    for product in products:
        invalid_records = find_invalid_products(**product)
        if not invalid_records:
            total_value += product["price"] * product["stock"]
    return total_value
show_valid_product(products)
inventory_value = calculate_inventory_value(products)
print(f"Total inventory value: {inventory_value}")
