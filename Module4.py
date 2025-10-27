#Module 4 Portfolio Milestone
#ItemToPurchase class
class ItemToPurchase:
    ItemToPurchase_name = "none"
    ItemToPurchase_price = 0
    ItemToPurchase_quantity = 0
    #Method to print out ItemToPurchase cost
    def print_ItemToPurchase_cost(ItemToPurchase):
        total_cost = ItemToPurchase.ItemToPurchase_price * ItemToPurchase.ItemToPurchase_quantity
        print(f"{ItemToPurchase.ItemToPurchase_name} {ItemToPurchase.ItemToPurchase_quantity:.0f} @ ${ItemToPurchase.ItemToPurchase_price:.2f} = ${total_cost:.2f}")
    #Method to validate user input
    def valid_input(prompt, value_type, condition):
        value = value_type(input(prompt))
        while not condition(value):
            value = value_type(input("Please enter a valid value: "))
        return value

#Calculate and print total cost of both ItemToPurchases
def print_total_cost(ItemToPurchase1, ItemToPurchase2):
        total = ((ItemToPurchase1.ItemToPurchase_price * ItemToPurchase1.ItemToPurchase_quantity) + (ItemToPurchase2.ItemToPurchase_price * ItemToPurchase2.ItemToPurchase_quantity))
        print(f"\nTotal cost: ${total:.2f}")

#define objects
ItemToPurchase1 = ItemToPurchase()
ItemToPurchase2 = ItemToPurchase()

#get inputs from user
print("Item 1")
ItemToPurchase1.ItemToPurchase_name = ItemToPurchase.valid_input("Enter the item name: ", str, lambda x: x.strip() != "")
ItemToPurchase1.ItemToPurchase_price = ItemToPurchase.valid_input("Enter the item price: ", float, lambda x: x > 0)
ItemToPurchase1.ItemToPurchase_quantity = ItemToPurchase.valid_input("Enter the item quantity: ", int, lambda x: x > 0)

print("Item 2")
ItemToPurchase2.ItemToPurchase_name = ItemToPurchase.valid_input("Enter the item name: ", str, lambda x: x.strip() != "")
ItemToPurchase2.ItemToPurchase_price = ItemToPurchase.valid_input("Enter the item price: ", float, lambda x: x > 0)
ItemToPurchase2.ItemToPurchase_quantity = ItemToPurchase.valid_input("Enter the item quantity: ", int, lambda x: x > 0)

#Print costs
print("Total Cost:\n")
ItemToPurchase1.print_ItemToPurchase_cost()
ItemToPurchase2.print_ItemToPurchase_cost()
print_total_cost(ItemToPurchase1, ItemToPurchase2)
