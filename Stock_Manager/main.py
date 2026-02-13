from database import(
    create_table,
    add_product
)

create_table()

name = input("Enter your full name : ")
quantity = int(input("Enter the quantity of stock : "))
price = int(input("Enter the total price of stock : "))
low_stock = int(input("Enter the threshold quantity of stock : "))
created_at = input("Enter the date of buy : ")

add_product(name, quantity, price, low_stock, created_at)