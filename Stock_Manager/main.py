from database import(
    create_table,
    add_product,
    get_product_by_id,
    get_all_products,
    update_product_quantity,
    delete_product
)

create_table()

name = input("Enter your full name : ")
quantity = int(input("Enter the quantity of stock : "))
price = int(input("Enter the total price of stock : "))
low_stock = int(input("Enter the threshold quantity of stock : "))

add_product(name, quantity, price, low_stock)

id = int(input("Enter the id of the stock: "))

value = get_product_by_id(id)
print(value)

get_list = get_all_products()
print(get_list)

id_1 = int(input("Enter the id of the stock: "))
new_quantity = int(input("Enter the quantity of stock : "))
update_product_quantity(id_1, new_quantity)

get_list_1 = get_all_products()
print(get_list_1)

id_2 = int(input("Enter the id of the stock: "))
delete_product(id_2)




