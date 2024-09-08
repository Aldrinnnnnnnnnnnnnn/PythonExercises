# 3. Declare a first name variable and assign a value to it
first_name = "Aldrin"
# 4. Declare a last name variable and assign a value to it
last_name = "Tamonte"
# 5. Declare a full name variable and assign a value to it
full_name = "Aldrin Tamonte"
# 6. Declare a country variable and assign a value to it
country = "Philippines"
# 7. Declare a city variable and assign a value to it
city = "San fabian"
# 8. Declare an age variable and assign a value to it
age = 22
# 9. Declare a year variable and assign a value to it
year = 2024
# 10. Declare a variable is_married and assign a value to it
is_married = False
# 11. Declare a variable is_true and assign a value to it
is_married = True
# 12. Declare a variable is_light_on and assign a value to it
is_light_on = True
# 13. Declare multiple variable on one line
a, b, c, d, e = 1, 2, 3, 4, 5
# 14. Write a program to add two numbers
num1, num2 = 1, 2
total = num1 + num2
print(total)
# 15. Write a program  to find the remainder when a number is divided  by 2
num3, num4 = 2, 6
total1 = num3 % num4
print(total1)
# 16. Check the type of the variable assigned using input() function

user = input("Enter a value: ")

print(type(user))
# 17. Use a comparison operator to find out whether a given variable'a' is greater than ‘b’ or not. Take a=34 and b=8
ax = 34
bx = 8

print(ax > bx)  # =True
# 18. Write a program to find the average of two numbers entered by the user.
user1 = float(input("Enter the First Number: "))
user2 = float(input("Enter the Second Number: "))

total = (user1 + user2) / 2

print(f"The average of {num1} and {num2} is: {total}")
"""
Enter the First Number: 100
Enter the Second Number: 12
The average of 1 and 2 is: 56.0
"""

# 19. Write a python program to calculate  the square  of a number entered by the user.
users = float(input("Enter any number: "))
total = users**2
print(total)  # 2 = 4.0

# Exercises: Level 2
# 1. Check the data type of all your variables using type() built-in function
print(type("Hai"))  # <class 'str'>
# 2. Using the len() built-in function, find the length of your first name
print(len("Aldrin"))  # =6
# 3. Compare the length of your first name and your last name
first_name = "Aldrin"
last_name = "Tamonte"
total = first_name, last_name
print(len(total))

"""4. Declare 5 as num_one and 4 as num_two
    * Add num_one and num_two and assign the value to a variable total
    * Subtract num_two from num_one and assign the value to a variable diff
    * Multiply num_two and num_one and assign the value to a variable product
    * Divide num_one by num_two and assign the value to a variable division
    * Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    * Calculate num_one to the power of num_two and assign the value to a variable exp
    * Find floor division of num_one by num_two and assign the value to a variable floor_division
"""
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one**num_two
floor_division = num_one // num_two
# 5. The radius of a circle is 30 meters.
#    * Calculate the area of a circle and assign the value to a variable name of area_of_circle
#    * Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#    * Take radius as user input and calculate the area.
# Approximate value of π
pi = 3.141592653589793
# Given radius
radius_of_circle = 30
# Calculate the area of the circle
area_of_circle = pi * radius_of_circle**2
# Calculate the circumference of a circle
circum_of_circle = 2 * pi * radius_of_circle

print(f"Area of the circle: {area_of_circle:.2f} square meters")
print(f"Circumference of the circle: {circum_of_circle:.2f} meters")
# .2f ensures that the number is displayed with exactly two digits after the decimal point.
# Take radius as user input and calculate the area
user_radius = float(input("Enter the radius of the circle in meters: "))
user_area_of_circle = pi * user_radius**2

# Print the area calculated with user input
print(
    f"Area of the circle with radius {user_radius} meters: {user_area_of_circle:.2f} square meters"
)
# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names.
# Get user input for first name
first_name = input("Enter your first name: ")

# Get user input for last name
last_name = input("Enter your last name: ")

# Get user input for country
country = input("Enter your country: ")

# Get user input for age and convert it to an integer
age = int(input("Enter your age: "))

# Print the collected information
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Country: {country}")
print(f"Age: {age}")
# 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
# open terminal and go to python shell >>>help('keywords')
# 8.Write a program to output this — First Program -Python Print Function
print("First Program -Python Print Function ")
# 9.Write a program to output this — It is Declared like this:
print("It is Declared like this: ")
# 10.Write a program to output this — print(“What to print”)
print('print("What to print")')
