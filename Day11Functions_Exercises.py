# Exercises: Day 11
# Exercises: Level 1
user1 = int(input("Enter the 1st number: "))
user2 = int(input("Enter the 2nd number: "))


def add_two_number(user1, user2):
    return user1 + user2


# call the function
result = add_two_number(user1, user2)  # we can store it in the variable result.
print(result)


# 2.Area of a circle is calculated as follows: area = π x r x r.
# Write a function that calculates area_of_circle.
def area_of_circle(radius):
    return 3.14 * radius * radius


user_input = float(input("Enter the radius: "))
result = area_of_circle(user_input)
print(f"The area of the circle is: {result}")


# 3.Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.


# *args parameter allows the function to accept an arbitrary number of arguments
def add_all_nums(*args):
    total = 0  # This variable will be used to store the sum of all the numeric arguments passed to the function.
    for num in args:  # Each argument is assigned to the variable num in each iteration.
        # This line checks if the current argument (num) is not an instance of int or float using the isinstance() function.
        # isinstance() is used to verify the type of an object. In this case, it checks if num is either an int or float.
        if not isinstance(num, (int, float)):
            # If num is not a number (either int or float), the condition evaluates to True.
            return f"Error: '{num}' is not a number"
        total = total + num  # This line adds the current num to the total variable.
    return total  # After the loop completes (i.e., all arguments have been checked and added), this line returns the final sum stored in total.


print(add_all_nums(1, 2, 3, 4, 4))  # 14
print(add_all_nums(1, 2, 3, 4, "a"))  # Error: 'a' is not a number


# 4.Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


user = float(input("Enter the Celsius: "))
result = convert_celsius_to_fahrenheit(user)
print(result)


# 5.Write a function called check-season,
# it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month == "January" or month == "February" or month == "March":
        return "Autumn"
    elif month == "April" or month == "May" or month == "June":
        return "Winter"
    elif month == "July" or month == "August" or month == "September":
        return "spring"
    elif month == "October" or month == "November" or month == "December":
        return "Summer"
    else:
        print("Invalid month")


user = input("Enter a month: ").capitalize()
result = check_season(user)
print(f"The season of the month of {user} is {result}")


# 6.Write a function called calculate_slope which return the slope of a linear equation.
def calculate_slope(x1, x2, y1, y2):
    # Check if the x-coordinates are the same to avoid division by zero.
    if x1 == x2:
        return None  ## Indicates that the slope is undefined (vertical line)
    # Calculate the slope
    slope = (y2 - y1) / (x2 - x1)
    return slope


# example usage
x1, y1 = 0, 2
x2, y2 = 2, 6

slope = calculate_slope(x1, y1, x2, y2)

if slope is None:
    print("The slope is undefined (vertical line)")
else:
    print(
        f"The slope of the line through ({x1}), ({y1}) and ({x2}), ({y2}) is: {slope:.2f}"
    )
# 7.Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import cmath


def solve_quadratic_eqn(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c

    # Calculate two solutions using the quadratic formula
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return root1, root2


# Example usage
a = 1
b = -3
c = 2

solution1, solution2 = solve_quadratic_eqn(a, b, c)
print(f"The solutions are: {solution1} and {solution2}")


# 8.Declare a function named print_list.
# It takes a list as a parameter and it prints out each element of the list.
def print_list(list1):
    for i in list1:
        print(i)


examplelist = [1, 2, 3, 4, 5]
print(print_list(examplelist))


# 9.Declare a function named reverse_list.
# It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    reverse_list_Store = []
    for i in range(len(lst) - 1, -1, -1):
        reverse_list_Store.append(lst[i])
    return reverse_list_Store


example_list = [1, 2, 3, 4, 5]
print(reverse_list(examplelist))  # [5, 4, 3, 2, 1]


# [5, 4, 3, 2, 1]
def reversed_list1(lst2):
    store_reversed_string = []
    for i in range(len(lst2) - 1, -1, -1):
        store_reversed_string.append(lst2[i])
    return store_reversed_string


print(reversed_list1(["A", "B", "C"]))  # ['C', 'B', 'A']
# print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]


# 10.Declare a function named capitalize_list_items.
# It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    store_list = []
    for i in lst:
        store_list.append(i.upper())
    return store_list


print(
    capitalize_list_items(["aldrin", "jordan", "marc", "heidi"])
)  # ['ALDRIN', 'JORDAN', 'MARC', 'HEIDI']


# 11.Declare a function named add_item. It takes a list and an item parameters.
# It returns a list with the item added at the end.
def add_item(food_staff, item):
    food_staff.append(item)
    return food_staff


food_staff = ["Potato", "Tomato", "Mango", "Milk"]
result = add_item(food_staff, "Meat")
print(result)  # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];


def add_numbers(numbers, item):
    numbers.append(item)
    return numbers


numbers = [2, 3, 7, 9]
print(add_numbers(numbers, 5))  # [2, 3, 7, 9, 5]
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))[2, 3, 7, 9, 5]


# 12.Declare a function named remove_item.
# It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(food_staff, item):
    if item in food_staff:  # Check if the item exists in the list
        food_staff.remove(item)  # Remove the item by value
    return food_staff


food_staff = ["Potato", "Tomato", "Mango", "Milk"]
print(remove_item(food_staff, "Mango"))
# food_staff = ["Potato", "Tomato", "Mango", "Milk"]
# print(remove_item(food_staff, "Mango"))  # ['Potato', 'Tomato', 'Milk'];


def remove_number(numbers, item):
    if item in numbers:
        numbers.remove(item)
    return numbers


numbers = [2, 3, 7, 9]
print(remove_number(numbers, 7))  # [2, 3, 9]


# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 7))  # [2, 3, 9]


# 13.Declare a function named sum_of_numbers.
# It takes a number parameter and it adds all the numbers in that range.


def sum_of_number(number):
    total = 0
    for i in range(number + 1):
        total = total + i  # i = 1, i = 2 = 3
    return total


print(sum_of_number(5))

# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10))  # 55
# print(sum_all_numbers(100))  # 5050


# 14.Declare a function named sum_of_odds.
# It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(number):
    total = 0
    for i in range(number + 1):
        if i % 2 == 1:
            total = total + i
    return total


print(sum_of_odds(10))  # 1+3+5+7+9 = 25


# 15.Declare a function named sum_of_even.
# It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(number):
    total = 0
    for i in range(number + 1):
        if i % 2 == 0:
            total = total + i  # 2+4+6+8+10
    return total


print(sum_of_even(10))  # 30


# Exercises: Level 2
# 1.Declare a function named evens_and_odds .
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
# print(evens_and_odds(100))
# The number of odds are 50.
# The number of evens are 51.
def even_and_odds(positive_integer):
    # evens and odds, both set to 0. These will keep track of how many even and odd numbers we find.
    evens = 0
    odds = 0
    for i in range(positive_integer + 1):
        # The % operator finds the remainder when i is divided by 2. If the remainder is 0 (i % 2 == 0), then i is even.
        if i % 2 == 0:
            # If the number is even, add 1 to the evens counter. This increases the count of even numbers found so far.
            evens = evens + 1
        else:
            odds = odds + 1
    return evens, odds


# even_and_odds with 100 as the argument. It stores the results (counts of evens and odds) in the variables evens and odds.
evens, odds = even_and_odds(100)
print(f"The number of odds are : {odds}")
print(f"The number of evens are: {evens}")


# 1.Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number.
def factorial(n):
    # Check if the input is a non-negative integer
    if n < 0:
        return "Factorial is not defined for negative numbers!"
    result = 1
    for i in range(1, n + 1):  ## Loop from 1 to n (inclusive)
        result = result * i  # # Multiply result by the current number i
    return result


print(factorial(5))  # Output: 120 (5! = 5 * 4 * 3 * 2 * 1)


# 2.Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if param == "" or param == [] or param == {}:
        return True
    return False


print(is_empty(""))  # True
print(is_empty("Hello"))  # False


# 3.Write different functions which take lists.
# They should calculate_mean, calculate_median, calculate_mode,
# calculate_range, calculate_variance, calculate_std (standard deviation).
import statistics


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


# Function to calculate the median of a list
def calculate_median(numbers):
    return statistics.median(numbers)


# Function to calculate the mode of a list
def calculate_mode(numbers):
    return statistics.mode(numbers)


# Function to calculate the range of a list
def calculate_range(numbers):
    return max(numbers) - min(numbers)


# Function to calculate the variance of a list
def calculate_variance(numbers):
    return statistics.variance(numbers)


# Function to calculate the standard deviation of a list
def calculate_std(numbers):
    return statistics.stdev(numbers)


# Example usage:
data = [1, 2, 2, 3, 4, 5, 5, 6, 7]

print("Mean:", calculate_mean(data))
print("Median:", calculate_median(data))
print("Mode:", calculate_mode(data))
print("Range:", calculate_range(data))
print("Variance:", calculate_variance(data))
print("Standard Deviation:", calculate_std(data))


# Exercises: Level 3
# 1.Write a function called is_prime, which checks if a number is prime.
def prime_checker(number):  # 5%2==0, 5%3
    is_prime = True
    if user <= 1:
        is_prime = False
    for i in range(2, number):  # 5 = 2 ,3 4
        if number % i == 0:  # number % 2,3,4
            is_prime = False
    if is_prime == True:
        print(f"{user} Is a Prime number! ")
    else:  # is_prime = false
        print(f"{user} It is not a Prime number!")


user = int(input("Enter a number: "))
prime_checker(user)


# 2.Write a functions which checks if all items are unique in the list.
def all_unique(items):
    return len(items) == len(set(items))


my_list = [1, 2, 3, 4, 5]
print(all_unique(my_list))  # =True,Because all items in list are unique
my_list2 = [1, 2, 3, 4, 4, 5]
print(all_unique(my_list2))  # False,Because it duplicate the 4 twice.


# 3.Write a function which checks if all the items of the list are of the same data type.
def all_it_same_types(lst):
    # Get the type of the first item in the list.
    first_item_types = type(lst[0])

    # Loop through each item in the list.
    for i in lst:
        # If the type of the current item is different,return false.
        if type(i) != first_item_types:
            return False

    # If all items have the same type, return True
    return True


my_list3 = [1, 2, 3, 4, 5, "5"]
print(all_it_same_types(my_list3))  # False,because it has a data type string.


# 4.Write a function which check if provided variable is a valid python variable
import keyword


def is_valid_variable(var_name):
    # check if the variable name is empty
    if not var_name:
        return False

    # check if the first character is a letter or an underscore.
    if not (var_name[0].isalpha() or var_name[0] == "_"):
        return False

    # check if all characters in the name are letters,digits, or underscores
    for i in var_name:
        if not (i.isalnum() or i == "_"):
            return False

    # Check if the name is a reserved keyword
    if keyword.iskeyword(var_name):
        return False

    return True


print(is_valid_variable("my_variable"))  # True
print(is_valid_variable("2nd_variable"))  # False
print(is_valid_variable("for"))  # False

# 5.Go to the data folder and access the countries-data.py file.

# 1.Create a function called the most_spoken_languages in the world.
# It should return 10 or 20 most spoken languages in the world in descending order.

# Create a function called the most_populated_countries.
# It should return 10 or 20 most populated countries in descending order.


# Harry Problem set
# 1.Write a program using function to find greatest of three numbers.


def find_greatest(num1, num2, num3):
    # Compare num1 with num2 and num3
    if num1 >= num2 and num1 >= num3:
        return num1
    # Compare num2 with num3
    elif num2 >= 1 and num2 >= num3:
        return num2
    # If num3 is greater or equal to both num1 and num2
    else:
        return num3


# Input numbers from the user
num1 = float(input("Enter the first number: "))  # 10
num2 = float(input("Enter the second number: "))  # 100
num3 = float(input("Enter the third number: "))  # 47


greatest = find_greatest(num1, num2, num3)
print(f"The greatest number is: {greatest}")  # The greatest number is: 100


# 2.Write a python program using function to convert Celsius to fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (9 / 5 * celsius) + 32


user = int(input("Enter the Celsius: "))
result = celsius_to_fahrenheit(user)
print(result)

# 3.How do you prevent a python print() function to print a new line at the end.
print("Hello")
print("World")
# Hello
# World
# use the end parameter of the print() function.
# By setting end to an empty string (""), you can avoid the automatic newline.
print("Hello", end="")
print("World")  # =HelloWorld


# 4.Write a recursive function to calculate the sum of first n natural numbers.
"""
    Recursion is a way of solving a problem where a function calls itself to break down 
    the problem into smaller, more manageable parts. You can think of it as a process in 
    which a function repeats itself in a smaller scope until it reaches a condition that 
    stops the repetition (the "base case").
"""
"""
    Let's say you want to find the sum of the first 5 natural numbers: 1 + 2 + 3 + 4 + 5. If we break it down, you can think of it as:

    First, sum the first 4 numbers: 1 + 2 + 3 + 4 = 10.
    Then, just add 5 to that sum: 10 + 5 = 15.
    Similarly, to find the sum of the first n numbers, you can first sum the first n−1 numbers, and then add 
    n to that result. This is where recursion comes in handy.
"""


def sum_natural_numbers(n):
    # Base case: if n is 1, the sum is just 1
    if n == 1:
        return 1
    # Recursive case: sum of n is n + sum of numbers before it
    else:
        return n + sum_natural_numbers(n - 1)


n = int(input("Enter a natural number: "))
print(f"The sum of the first {n} natural numbers is: {sum_natural_numbers(n)}")  # =15


# 5.Write a python function to print first n lines of the following pattern:
# * * *
# * *
# *     -> for n=3

"""
    The idea is:

    In the first line, you print 3 asterisks.
    In the second line, you print 2 asterisks.
    In the third line, you print 1 asterisk.
    With recursion, we can say:

    Print the first line with n asterisks.
    Then, call the function again to print the next line with one less asterisk 
    until there's just one asterisk left.
"""


def print_pattern(n):
    # Base case: If n is 0, stop the recursion
    if n == 0:
        return  # if this is 0 it will stop the program. break
    print("* " * n)  # 3 = * * *
    # Recursive call to print the next line with one less asterisk
    print_pattern(n - 1)


"""
    How This Works
    Base Case: The function checks if n is 0. If it is, it stops (does nothing). 
    This is the ending of the story.

    Recursive Case: If n is not 0, it prints 
    n asterisks followed by a space ('* ' * n), then calls itself with n-1
    to print the next line with one less asterisk.

    Example Walkthrough for n = 3

    1.The first call prints: * * *.
    2.It then calls itself to print: * *.
    3.It calls itself again to print: *.
    4.Finally, it stops when n becomes 0.
"""

# input from the user
n = int(input("Enter the number of lines"))
print_pattern(n)


# 6.Write a python function which convert inches to cms.
# To convert inches to centimeters, you multiply the number of inches by 2.54,
# since 1 inch equals 2.54 centimeters.
def inches_to_cm(inches):
    # 1inch = 2.54 centimeter
    centimeters = inches * 2.54
    return centimeters


inches = float(input("Enter the length in inches: "))
print(f"{inches}  inches is equal to {inches_to_cm(inches)} centimeters.")
# =4.0 inches is equal to 10.16 centimeters.


# 7.Write a python function to remove a given word from a list and strip it at the same time.
def remove_and_strip(words_list, word_to_remove):
    # Strip each word in the list and filter out the word to remove.
    cleaned_list = [
        word.strip() for word in words_list if word.strip() != word_to_remove
    ]
    return cleaned_list


words = [" apple ", " banana", " orange ", " apple", " grape "]
word_to_remove = "grape"
result = remove_and_strip(words, word_to_remove)
print(result)


# 8.Write a python function to print multiplication table of a given number.
def multiplication(n):
    for i in range(11):
        print(f"{n} x {i} = {n * i}")


n = int(input("Enter a number: "))
print(multiplication(n))
