books = [
    {"title": "Python Basics", "price": 500, "stock": 10},
    {"title": "SQL Guide", "price": 350, "stock": 5},
    {"title": "", "price": 400, "stock": 8},
    {"title": "Excel Mastery", "price": -100, "stock": 7},
    {"title": "Power BI", "price": 600, "stock": 0}
]

def find_invalid_books(title, price, stock):
    constraints = {
        "title" : isinstance(title,str) and len(title.strip())!= 0,
        "price" : isinstance(price,int) and price >0,
        "stock" : isinstance (stock,int) and stock > 0
    }
    return[key for key, value in constraints.items()if not value]
def show_valid_books(books):
    for book in books:
        invalid_book = find_invalid_books(**book)
        if invalid_book:
            print(f"invalid book:{book}")
            for key in invalid_book:
                print(f"{key}: {book[key]}")
        else:
            print(f"{book['title']}:₹{book['price']}")
def calculate_inventory(books):
    total_value= 0
    for book in books:
        invalid_book = find_invalid_books(**book)
        if not invalid_book:
            total_value += book["price"]* book["stock"]
    return total_value
show_valid_books(books)
total_inventory = calculate_inventory(books)
print(f"total inventory: {total_inventory}")

