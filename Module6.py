#ItemToPurchase Class
class ItemToPurchase:
    def __init__(item, item_name = "none", item_price = 0.0, item_quantity = 0, item_description = "none"):
        item.item_name = item_name
        item.item_price = item_price
        item.item_quantity = item_quantity
        item.item_description = item_description

    def print_item_cost(item):
        total_cost = item.item_price * item.item_quantity
        print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${total_cost}")

    def print_item_description(item):
        print(f"{item.item_name}: {item.item_description}")

    def valid_input(prompt, value_type, condition):
        value = value_type(input(prompt))
        while not condition(value):
            value = value_type(input("Please enter a valid value: "))
        return value

#ShoppingCart Class
class ShoppingCart:
    def __init__(cart, customer_name = "none", current_date = "January 1, 2020"):
        cart.customer_name = customer_name
        cart.current_date = current_date
        cart.cart_items = []
# Add items to cart
    def add_item(cart, item):
        cart.cart_items.append(item)
# Remove items from cart
    def remove_item(cart, item_name):
        exists = False
        for item in cart.cart_items:
            if item.item_name == item_name:
                cart.cart_items.remove(item)
                exists = True
                break
        if not exists:
            print("Item not found in cart. Nothing removed.")
# Modify items in cart
    def modify_item(cart, modified_item):
        exists = False
        for item in cart.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                exists = True
                break
        if not exists:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(cart):
        total_quantity = sum(item.item_quantity for item in cart.cart_items)
        return total_quantity

    def get_cost_of_cart(cart):
        total_cost = sum(item.item_price * item.item_quantity for item in cart.cart_items)
        return total_cost

    def print_total(cart):
        print(cart.customer_name, "'s Shopping Cart -", cart.current_date)
        total_items = cart.get_num_items_in_cart()
        print("Number of Items: ", total_items)
        if len(cart.cart_items) == 0:
            print("\nCart is Empty..")
        else:
            for item in cart.cart_items:
                item.print_item_cost()
        print(f"\nTotal: ${cart.get_cost_of_cart():.2f}")

    def print_descriptions(cart):
        print(cart.customer_name, "'s Shopping Cart - ", cart.current_date)
        print("Item Descriptions")
        for item in cart.cart_items:
            item.print_item_description()

# Menu
def print_menu(cart):
    option = ""
    while option != 'q':
        print("\n     ** MENU **")
        print("a - Add item to Cart")
        print("r - Remove item from Cart")
        print("c - Change item Quantity")
        print("i - Output item Descriptions")
        print("o - Output Shopping Cart")
        print("q - Quit")

        option = input("\nChoose an option:\n").lower()

        while option not in ['a', 'r', 'c', 'i', 'o', 'q']:
            option = input("Choose a valid option:\n").lower()

        if option == 'a':
            print("Add Item to Cart")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = ItemToPurchase.valid_input("Enter the item price: ", float, lambda x: x > 0)
            quantity = ItemToPurchase.valid_input("Enter the item quantity: ", int, lambda x: x > 0)
            new_item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(new_item)

        elif option == 'r':
            print("Remove Item from Cart: ")
            name = input("Enter item to remove:\n")
            cart.remove_item(name)

        elif option == 'c':
            print("Change Item Quantity: ")
            name = input("Enter the item:\n")
            quantity = ItemToPurchase.valid_input("Enter the item quantity: ", int, lambda x: x > 0)
            modified_item = ItemToPurchase(item_name=name, item_quantity=quantity)
            cart.modify_item(modified_item)

        elif option == 'i':
            print("* Item Descriptions *")
            cart.print_descriptions()

        elif option == 'o':
            print("* Shopping Cart *")
            cart.print_total()

        elif option == 'q':
            break

#Start 
customer_name = input("Enter customer name: ")
current_date = input("Enter the date: ")
print("\nCustomer name: ", customer_name)
print("Today's date: ", current_date)

cart = ShoppingCart(customer_name, current_date)
print_menu(cart)

