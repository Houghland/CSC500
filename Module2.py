import math
print("Module 2 from book")
print("\nUsing value, string, type and id")

birthday_year = 1986
birthday_month = 'April'
birthday_day = 22
age = 19

print('\nbirthday_year = 1986')
print(' value:', str(birthday_year))
print(' type:', type(birthday_year))
print(' id:', id(birthday_year))

print("\nbirthday_month = 'April'")
print(' value:', str(birthday_month))
print(' type:', type(birthday_month))
print(' id:', id(birthday_month))

print('\nbirthday_day = 22')
print(' value:', str(birthday_day))
print(' type:', type(birthday_day))
print(' id:', id(birthday_day))

print('\nage = 19')
print(' value:', str(age))
print(' type:', type(age))
print(' id:', id(age))

#reads in a mass in kilograms and prints the amount of energy stored in the mass

c_meters_per_sec = 299792458  # Speed of light (m/s)
joules_per_AA_battery = 4320.5  # Nickel-Cadmium AA batteries
joules_per_TNT_ton = 4.184e9
print()

#Read in a floating-point number from the user
print()
mass_kg = float(10)

#getting prefix
print("Using Modulo and // for prefix")
print("Given a 10-digit phone number stored as an integer, % and // can be used to get any part, such as the prefix. For phone_num = 9365551212 (whose prefix is 555)")
phone_num = 9365551212
tmp_val = phone_num // 10000  # '// 10000' removes rightmost 4 digits , so '9365551212 // 10000' is 936555. 
print("tmp_val = phone_num // 10000:", tmp_val)
prefix_num = tmp_val % 1000 # '% 1000' gets rightmost 3 digits, so '936555 % 1000' is 555.
print("prefix_num = tmp_val % 1000:", prefix_num)
print ("Dividing by a power of 10 removes rightmost digits. Ex: 321 // 10 is 32. Ex: 321 // 100 is 3.")
print("%\ by a power of 10 gets rightmost digits. Ex: 321 % 10 is 1. Ex: 321 % 100 is 21.")

#Math Functions
print("\nMath Functions")
x = 2.3
z = math.ceil(x)
print("math.ceil")
print("x = 2.3")
print("z = math.ceil(x)")
print("z = ",z)

x = 2.3
z = math.floor(x)
print("\nmath.floor")
print("x = 2.3")
print("z = math.floor(x)")
print("z = ",z)

z = 4.5
z = math.pow(math.floor(z), 2.0)
print("\nz = math.pow(math.floor())")
print("z = 4.5")
print("z = math.pow(math.floor(z), 2.0)")
print("z = ",z)

z = 15.75
ceil = math.ceil(z)
z = math.sqrt(math.ceil(z))
print("\nmath.sqrt(math.ceil()")
print("z = 15.75")
print("math.ceil(z) = ", ceil)
print("z = math.sqrt(math.ceil(z))")
print("z = ",z)

z = 4
z = math.factorial(z)
print("\nmath.factorial()")
print("z = 15.75")
print("z = math.factorial(z)")
print("z = ",z)

print("\nAssign point_dist with the distance between point (x1, y1) and point (x2, y2). " \
"\nThe calculation is: Distance = SquareRootOf( (x2 - x1)2 + (y2 - y1)2 ) ")

point_dist = 0.0

x1 = float(1.0)
y1 = float(2.0)
x2 = float(1.0)
y2 = float(5.0)
print("\npoint_dist = math.sqrt((math.pow((x2 - x1), 2.0)) + (math.pow((y2 - y1), 2.0)))")
point_dist = math.sqrt((math.pow((x2 - x1), 2.0)) + (math.pow((y2 - y1), 2.0)))
print('Points distance:', point_dist)