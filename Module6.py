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
    customer_name = "none"
    current_date = "January 1, 2020"
    cart_items = []
# Add items to cart
    def add_item(ItemToPurchase):
        ShoppingCart.cart_items.append(ItemToPurchase)
# Remove items from cart
    def remove_item(item_name):
        exists = False
        for item in ShoppingCart.cart_items:
            if item.item_name == item_name:
                ShoppingCart.cart_items.remove(item)
                exists = True
                break
        if not exists:
            print("Item not found in cart. Nothing removed.")
# Modify items in cart
    def modify_item(ItemToPurchase):
        exists = False
        for item in ShoppingCart.cart_items:
            if item.item_name == ItemToPurchase.item_name:
                if ItemToPurchase.item_description != "none":
                    item.item_description = ItemToPurchase.item_description
                if ItemToPurchase.item_price != 0:
                    item.item_price = ItemToPurchase.item_price
                if ItemToPurchase.item_quantity != 0:
                    item.item_quantity = ItemToPurchase.item_quantity
                exists = True
                break
        if not exists:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart():
        total_quantity = sum(item.item_quantity for item in ShoppingCart.cart_items)
        return total_quantity

    def get_cost_of_cart():
        total_cost = sum(item.item_price * item.item_quantity for item in ShoppingCart.cart_items)
        return total_cost

    def print_total():
        print("{ShoppingCart.customer_name}'s Shopping Cart -", ShoppingCart.current_date)
        total_items = ShoppingCart.get_num_items_in_cart()
        print("Number of Items: ", total_items)
        if len(ShoppingCart.cart_items) == 0:
            print("\nSHOPPING CART IS EMPTY")
        else:
            for item in ShoppingCart.cart_items:
                item.print_item_cost()
        print(f"\nTotal: ${ShoppingCart.get_cost_of_cart():.2f}")

    def print_descriptions():
        print(ShoppingCart.customer_name, "'s Shopping Cart - ", ShoppingCart.current_date)
        print("\nItem Descriptions")
        for item in ShoppingCart.cart_items:
            item.print_item_description()

# Menu
def print_menu(ShoppingCart):
    option = ""
    while option != 'q':
        print("\n     ** MENU **")
        print("a - Add item to Cart")
        print("r - Remove item from Cart")
        print("c - Change item")
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
            ShoppingCart.add_item(new_item)

        elif option == 'r':
            print("Remove Item from Cart: ")
            name = input("Enter item to remove:\n")
            ShoppingCart.remove_item(name)
        #Options to update description/price/quantity
        elif option == 'c':
            print("Change Item")
            name = input("Enter the item:\n")
            #verify if item exists - if it does, update
            for item in ShoppingCart.cart_items:
                while item.item_name != name:
                    name = input("Item not found. Please enter valid item:")
                if item.item_name == name:
                    change = ""
                    while change != 's':
                        print("Which do you want to change:")
                        print("a - Description")
                        print("b - Price")
                        print("c - Quantity")
                        print("s - Save Changes")

                        change = input("\nChoose an option:\n").lower()
                        while change not in ['a', 'b', 'c', 's']:
                            change = input("Choose a valid option:\n").lower()
                        if change == 'a':
                            description = ItemToPurchase.valid_input("Enter the item description: ", str, lambda x: x.strip() != "")
                            modified_item = ItemToPurchase(item_name=name, item_description=description)
                            ShoppingCart.modify_item(modified_item)
                        elif change == 'b':
                            price = ItemToPurchase.valid_input("Enter the item price: ", float, lambda x: x > 0) 
                            modified_item = ItemToPurchase(item_name=name, item_price=price)
                            ShoppingCart.modify_item(modified_item)               
                        elif change == 'c':
                            quantity = ItemToPurchase.valid_input("Enter the item quantity: ", int, lambda x: x > 0)
                            modified_item = ItemToPurchase(item_name=name, item_quantity=quantity)
                            ShoppingCart.modify_item(modified_item)                                    
                        elif option == 's':
                            print("Changes Saved")
                            break 

        elif option == 'i':
            print("* OUTPUT ITEMS' DESCRIPTIONS *")
            ShoppingCart.print_descriptions()

        elif option == 'o':
            print("* OUTPUT SHOPPING CART *")
            ShoppingCart.print_total()

        elif option == 'q':
            break

#Main 
def main():
    ShoppingCart.customer_name = input("Enter customer name: ")
    ShoppingCart.current_date = input("Enter the date: ")
    print("\nCustomer name: ", ShoppingCart.customer_name)
    print("Today's date: ", ShoppingCart.current_date)

    print_menu(ShoppingCart)

if __name__ == "__main__":
   main()