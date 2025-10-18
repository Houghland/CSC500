# item class
class item:
    item_name = "none"
    item_price = 0
    item_quantity = 0

#Check that input is valid
def valid_input(prompt, value_type, condition):
    value = value_type(input(prompt))
    while not condition(value):
        value = value_type(input("Please enter a valid value:"))
    return value

#objects
item1 = item()
item2 = item()

print("Item 1")
item1.item_name = valid_input("Enter the item name: ", str, lambda x: x.strip() != "")
item1.item_price = valid_input("Enter the item price: ", float, lambda x: x > 0)
item1.item_quantity = valid_input("Enter the item quantity: ", int, lambda x: x > 0)


print("Item 2")
item2.item_name = valid_input("Enter the item name: ", str, lambda x: x.strip() != "")
item2.item_price = valid_input("Enter the item price: ", float, lambda x: x > 0)
item2.item_quantity = valid_input("Enter the item quantity: ", int, lambda x: x > 0)

#calculations
print("Total Cost:\n")
print(item1.item_name, item1.item_price, "@ ${:.2f}".format(item1.item_quantity), "=", (item1.item_price * item1.item_quantity))
print(item2.item_name, item2.item_price, "@ ${:.2f}".format(item2.item_quantity), "=", (item2.item_price * item2.item_quantity))
