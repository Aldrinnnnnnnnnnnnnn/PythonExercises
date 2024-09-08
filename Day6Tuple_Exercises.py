# Exercises: Level 1
# 1.Create an empty tuple
empty_tuple = ()
# 2.Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brother = ("Aldrin", "Jordan", "Marc", "Stella", "Heidi")
sister = ("Stella", "jul", "pia", "sofia")
# 3.Join brothers and sisters tuples and assign it to siblings
siblings = brother + sister
print(
    siblings
)  # ('Aldrin', 'Jordan', 'Marc', 'Stella', 'Heidi', 'Stella', 'jul', 'pia', 'sofia')
# 4.How many siblings do you have?
print(len(siblings))  # 9
# 5.Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
print(
    family_members
)  # ['Aldrin', 'Jordan', 'Marc', 'Stella', 'Heidi', 'Stella', 'jul', 'pia', 'sofia']
family_members.append("Jords")
family_members.append(
    "Romy"
)  # ['Aldrin', 'Jordan', 'Marc', 'Stella', 'Heidi', 'Stella', 'jul', 'pia', 'sofia', 'Jords', 'Romy']
family_members = tuple(family_members)
print(
    family_members
)  # ('Aldrin', 'Jordan', 'Marc', 'Stella', 'Heidi', 'Stella', 'jul', 'pia', 'sofia', 'Jords', 'Romy')
# Exercises: Level 2
# 1.Unpack siblings and parents from family_members
unpack = family_members[9:]  # ('Jords', 'Romy')
print(unpack)
# 2.Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("banana", "apple", "orange")
vegetables = ("Broccoli", "Carrots", "Capsicum")
animals = ("Cattle", "Pig", "Fish", "Goat", "Dog")

food_stuff_tp = fruits + vegetables + animals

print(food_stuff_tp)
# 3.Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(
    food_stuff_lt
)  # ['banana', 'apple', 'orange', 'Broccoli', 'Carrots', 'Capsicum', 'Cattle', 'Pig', 'Fish', 'Goat']
# 4.Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2  # 5
middle_item = food_stuff_lt[middle_index]
print(middle_item)  # Capsicum
# 5.Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[0:3]
last_three_items = food_stuff_lt[8:]
print(first_three_items)  # ['banana', 'apple', 'orange']
print(last_three_items)  # ['Fish', 'Goat', 'Dog']
# 6.Delete the food_staff_tp tuple completely
del food_stuff_tp
# print(food_stuff_tp)
# NameError: name 'food_stuff_tp' is not defined. Did you mean: 'food_stuff_lt'?

# 7.Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Estonia" in nordic_countries)  # False
# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)  # True

# Harry Practice set. List and Tuple
# 1.Write a program to store seven fruits in a list entered by the user.
user1 = input("Enter fruits 1: ")
user2 = input("Enter fruits 2: ")
user3 = input("Enter fruits 3: ")
user4 = input("Enter fruits 4: ")
user5 = input("Enter fruits 5: ")
user6 = input("Enter fruits 6: ")
user7 = input("Enter fruits 7: ")
fruits = [user1, user2, user3, user4, user5, user6, user7]
print(fruits)
# 2.Write a program to accept marks of 6 students and display them in a sorted manner.
# Accept marks for 6 students
mark1 = int(input("Enter the marks of student 1: "))
mark2 = int(input("Enter the marks of student 2: "))
mark3 = int(input("Enter the marks of student 3: "))
mark4 = int(input("Enter the marks of student 4: "))
mark5 = int(input("Enter the marks of student 5: "))
mark6 = int(input("Enter the marks of student 6: "))

# Store marks in a list
marks = [mark1, mark2, mark3, mark4, mark5, mark6]

# Sort the marks in ascending order
marks.sort()

# Display the sorted marks
print("The sorted marks are:", marks)

# 3.Check that a tuple  cannot be changed in python
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Trying to change the second element of the tuple
# my_tuple[1] = 10  # This will raise a TypeError

# 4.Write a program to sum a list with 4 numbers.
mark1 = int(input("Enter the marks of student 1: "))
mark2 = int(input("Enter the marks of student 2: "))
mark3 = int(input("Enter the marks of student 3: "))
mark4 = int(input("Enter the marks of student 4: "))

user = [mark1, mark2, mark3, mark4]
total = sum(user)
print(total)
# 5.Write a program to count  the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)

# Count the number of zeros in the tuple
zero_count = a.count(0)

# Display the result
print("The number of zeros in the tuple is:", zero_count)
