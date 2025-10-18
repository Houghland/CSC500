# item class
class item:
    item_name = "none"
    item_price = 0
    item_quantity = 0

    def print_item_cost(item):
        total_cost = item.item_price * item.item_quantity
        print(f"{item.item_name} {item.item_quantity:.0f} @ ${item.item_price:.2f} = ${total_cost:.2f}")
    
    def valid_input(prompt, value_type, condition):
        value = value_type(input(prompt))
        while not condition(value):
            value = value_type(input("Please enter a valid value:"))
        return value


def print_total_cost(item1, item2):
        total = ((item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity))
        print(f"\nTotal cost: ${total:.2f}")

#define objects
item1 = item()
item2 = item()


#get inputs
print("Item 1")
item1.item_name = item.valid_input("Enter the item name: ", str, lambda x: x.strip() != "")
item1.item_price = item.valid_input("Enter the item price: ", float, lambda x: x > 0)
item1.item_quantity = item.valid_input("Enter the item quantity: ", int, lambda x: x > 0)


print("Item 2")
item2.item_name = item.valid_input("Enter the item name: ", str, lambda x: x.strip() != "")
item2.item_price = item.valid_input("Enter the item price: ", float, lambda x: x > 0)
item2.item_quantity = item.valid_input("Enter the item quantity: ", int, lambda x: x > 0)


#calculations
print("Total Cost:\n")
item1.print_item_cost()
item2.print_item_cost()
print_total_cost(item1, item2)
