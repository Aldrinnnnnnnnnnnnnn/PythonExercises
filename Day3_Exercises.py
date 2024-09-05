#1. Declare your age as integer variable
age = 22
#2. Declare your height as a float variable
float_num = 1.63
#3. Declare a variable that store a complex number
com_num = 4 - 4j
#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#    Enter base: 20
#    Enter height: 10
#    The area of the triangle is 100
user1 = int(input("Enter Base: "))
user2 = int(input("Enter a height: "))
area = 0.5
total = area * user1 * user2
print(total)#=100.0
#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
#Enter side a: 5
#Enter side b: 4
#Enter side c: 3
#The perimeter of the triangle is 12
user1 = int(input("Enter side a: "))
user2 = int(input("Enter side b: "))
user3 = int(input("Enter side c: "))
total = user1 + user2 + user3
print(f'The perimeter of the trinagle is: {total}')
#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
user1 = int(input("Enter a length: "))
user2 = int(input("Enter a width: "))
area = user1 * user2
perimeter = 2 * (user1 + user2)
print(f"The are is: {user1} and the perimeter is: {perimeter}")
#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter a number: ")) 
pi = 3.14
area = pi * radius * radius
circumference = 2 * pi * radius
print(f"The area is:{area} and circumference is: {circumference:.2f}")
#The area is:314.0 and circumference is: 62.80
#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Define the coefficients of the equation y = mx + b
m = 2  # Slope (coefficient of x)
b = -2  # Y-intercept (constant term)

# Calculate the y-intercept
y_intercept = b

# Calculate the x-intercept
# Set y = 0 and solve for x: 0 = mx + b
x_intercept = -b / m

# Print the results
print(f"The slope (m) is: {m}")
print(f"The y-intercept is: ({0}, {y_intercept})")
print(f"The x-intercept is: ({x_intercept}, {0})")
print()

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Coordinates of the points
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calculate the slope (m)
slope = (y2 - y1) / (x2 - x1)

# Calculate the Euclidean distance manually
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Print the results
print(f"The slope between the points is: {slope}")
print(f"The Euclidean distance between the points is: {distance:.2f}")
print()

#10. Compare the slopes in tasks 8 and 9.

print(f"Task 10:")
print(f"Slope from Task 8: {m}")
print(f"Slope from Task 9: {slope}")
print(f"Are the slopes equal? {'Yes' if m == slope else 'No'}")
#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Define different x values manually and calculate y for each one

# x = -10
x = -10
y = x**2 + 6*x + 9
print(f"For x = {x}, y = {y}")

# x = -5
x = -5
y = x**2 + 6*x + 9
print(f"For x = {x}, y = {y}")

# x = 0
x = 0
y = x**2 + 6*x + 9
print(f"For x = {x}, y = {y}")

# x = 1
x = 1
y = x**2 + 6*x + 9
print(f"For x = {x}, y = {y}")

# x = 2
x = 2
y = x**2 + 6*x + 9
print(f"For x = {x}, y = {y}")

# x = 3
x = 3
y = x**2 + 6*x + 9
print(f"For x = {x}, y = {y}")

# Find the x value where y = 0
x = -3
y = x**2 + 6*x + 9
print(f"\nThe value of x where y is 0 is: {x}")
print(f"At x = {x}, y = {y}")

#12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(not len('python') == len('dragon'))# This is True but we put not become False
#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
a = 'python'
b = 'dragon'
is_in_both = 'on' in a and 'on' in b
print(is_in_both) #=True
#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
string = "I hope this course is not full of jargon"
is_in_string = 'Jargon' in string
print(is_in_string)#True
#15. There is no 'on' in both dragon and python
dra = 'dragon'
py = 'python'
is_in_both = not 'on' in dra and 'on' in py
print(f"Is 'on' found in both '{dra}' and '{py}'? {is_in_both}")
#Is 'on' found in both 'dragon' and 'python'? False
#16. Find the length of the text python and convert the value to float and convert it to string
text = 'python'
length = len(text)#6
flo = float(length)
stri = str(flo)
print(f"The length oy the {text} is {length} and convert to float is {flo} to string is {str}")

#17. Even numbers are divisible by 2 and the remainder is zero. 
#How do you check if a number is even or not using python?
user = int(input("Enter any Positive number: "))
if user % 2 == 0:
  print(f"{user} This is a Even number")
else:
  print(f"{user} This is not Even number")
#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_division = 7 // 3
int_conversion = int(2.7)
is_equal = floor_division == int_conversion # 2 == 2
print(is_equal)#True
#19. Check if type of '10' is equal to type of 10
print(type('10')== type(10)) # class 'str'> == <class 'int'>
#20. Check if int('9.8') is equal to 10
float_value = float('9.8')#9.8
int_value1 = int(float_value)#9
num2 = 10
result = int_value1 == num2
print(result)#false

#21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#Enter hours: 40
#Enter rate per hour: 28
#Your weekly earning is 1120
user1 = int(input("Enter a hours: "))
user2 = int(input("Enter rate per hour: "))
total_earning = user1 * user2
print(f"Your weekly earning is: {total_earning}")
#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
#Enter number of years you have lived: 100
#You have lived for 3153600000 seconds.
# Constants
seconds_perminute = 60
minutes_perminute = 60
hours_perday = 24
day_per_year = 365
# Get user input
years_lived = int(input("Enter number of years you have lived: "))
# Calculate the number of seconds
seconds_lived = years_lived * day_per_year * hours_perday * minutes_perminute * seconds_perminute
# Print the result
print(f"You have lived for {seconds_lived} seconds.")
#23. Write a Python script that displays the following table
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125

print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
# Function to print the table
def print_table():
    # Define the maximum row and column numbers
    max_row = 5
    max_col = 5
    
    # Print the table header
    print(' ', end=' ')
    for i in range(1, max_col + 1):
        print(f'{i:>4}', end=' ')
    print()
    
    # Print the table rows
    for row in range(1, max_row + 1):
        print(f'{row:>2}', end=' ')
        for col in range(1, max_col + 1):
            # Calculate the value in the cell
            value = row ** (col - 1)
            print(f'{value:>4}', end=' ')
        print()

# Call the function to display the table
print_table()

#Jenny 