#Part 1: total amount of a meal purchased at a restaurant
print("Part 1: Total for Meal")
print("Enter the charge for your food:")
food_charge = float(input())

#Check if number is <=0
while food_charge<=0 and food_charge=='':
    print("Your food charge cannot be less than or equal to 0\nPlease enter the amount:")
    food_charge = float(input())
tip = food_charge * 0.18
print("An 18% tip for ${:.2f}".format(food_charge),"would be: ${:.2f}".format(tip))
tax = food_charge * 0.07
print("A 7% sales tax on ${:.2f}".format(food_charge), "would be: ${:.2f}".format(tax))
total = food_charge + tip + tax
print("Your Total including Tax and Tip is: ${:.2f}".format(total))

#Part 2: 24-hour alarm clock
print("\nPart 2: 24-hour Alarm Clock")
print("What is the current time in hours (0-23)?")
current_time = int(input())

#Check if number is outside range
while current_time<0 or current_time>23:
    print("Please enter a valid time:")
    current_time = int(input())

print("In how many hours do you want the alarm to go off?")
alarm_hours = int(input())

#Check if number is <= 0
while alarm_hours<=0:
    print("Please enter a valid number:")
    alarm_hours = int(input())

#set alarm time
alarm_time = (current_time + alarm_hours) % 24

#Print formatted time alarm will go off
print("Your alarm will go off at: {:02d}:00".format(alarm_time))