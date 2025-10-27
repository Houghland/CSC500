#Module 5 Critical Thinking Assigment
#Part 1: Rainfall
    #Method to validate user input
def valid_input(prompt, value_type, condition):
    value = value_type(input(prompt))
    while not condition(value):
        value = value_type(input("Please enter a valid value: "))
    return value

print("Part 1: Rainfall over a period of years")
#Initialize Variables
total_rainfall = 0
total_months = 0
rain_years = valid_input("Enter the Number of Years: ", int, lambda x: x > 0)

# Each year
for year in range(1, rain_years + 1):
    print(f"\nYear {year}")
    
    # Each month
    for month in range(1, 13):
        rainfall = valid_input(f"Enter inches of rainfall for month {month} : ", float, lambda x: x >= 0)
        total_rainfall += rainfall
        total_months += 1

# Average
average_rainfall = total_rainfall / total_months
print("\n** Rainfall Summary **")
print(f"Total Months: {total_months}")
print(f"Total inches of Rainfall: {total_rainfall:.2f} inches")
print(f"Average Rainfall per month: {average_rainfall:.2f} inches")

# Part 2
# CSU Global books_purchasedtore
# 0 books_purchased, they earn 0 points.
# 2 books_purchased, they earn 5 points.
# 4 books_purchased, they earn 15 points.
# 6 books_purchased, they earn 30 points.
# 8 or more books_purchased, they earn 60 points.
print("\nCSU Gloabl books_purchasedtore Rewards")
books_purchased = valid_input("Enter the Number of books_purchased Purchased: ", int, lambda x: x >= 0)

if books_purchased == 0:
    points = 0
elif books_purchased == 2 or books_purchased == 3:
    points = 5
elif books_purchased == 4 or books_purchased == 5:
    points = 15
elif books_purchased == 6 or books_purchased == 7:
    points = 30
elif books_purchased >= 8:
    points = 60
else:
    points = 0

print("You've received", points, "points this Month!")

