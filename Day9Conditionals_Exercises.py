# Jenny Problem
# Check whether given number is even or odd.

user = int(input("Enter a positive number: "))

if user % 2 == 0:
    print("Even number")
else:
    print("Odd number!")


# Exercises: Level 1
# 1.Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
user = int(input("Enter your age: "))
if user >= 18:
    print("You can drive!")
else:
    years_left = 18 - user  # if user input 17.  18-17=1
    print(f"You need {years_left} more years to learn drive.")
    # You need 1 more years to learn drive.

# 2.Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
my_age = 22
your_age = int(input("Enter your age: "))

if my_age > your_age:  # 22 > 19 = True
    difference = my_age - your_age  # 22 -19 =3 =I'm {3} older  years than you
    if difference == 1:
        print("I'm 1 year older than you")
    else:
        print(f"I'm {difference} older years than you")
elif my_age < your_age:  # 22 < 23 true
    difference = your_age - my_age  # 23-22=1#You are 1 year older than me
    if difference == 1:
        print("You are 1 year older than me")
    else:
        print(f"You are {difference} years older than me")
else:
    print("We are same age")
# 3.Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3

user_a = int(input("Enter First number: "))
user_b = int(input("Enter Second number: "))

if user_a > user_b:
    print(f"{user_a} is greather than {user_b}")
elif user_a < user_b:
    print(f"{user_a} is less than {user_b}")
else:
    print(f"{user_a} is equal to {user_b}")


### Exercises: Level 2
# 1.Write a code which gives grade to students according to theirs scores:

# 80 - 100, A
# 70 - 79, B
# 60 - 69, C
# 50 - 59, D
# 0 - 49, f
user = int(input("Enter the grade: "))

if user >= 80 and user <= 100:
    print("A")
elif user >= 70 and user <= 79:
    print("B")
elif user >= 60 and user <= 69:
    print("C")
elif user >= 50 and user <= 59:
    print("D")
else:
    print("F")
# 2.Check if the season is Autumn, Winter, Spring or Summer.
# If the user input is: September, October or November, the season is Autumn.
# December,January or February, the season is Winter.
# March, April or May, the season is Spring.
# June, July or August, the season is Summer

user = input("Enter a month: ").capitalize()
if user == "September" or user == "October" or user == "November":
    print("The season is Autumn")
elif user == "December" or user == "January" or user == "February":
    print("Winter")
elif user == "March" or user == "April" or user == "May":
    print("Spring")
else:
    print("Summer")
# 2nd method
# Get the month from the user
month = input("Enter the month: ").strip().capitalize()

# Determine the season based on the month
if month in ["September", "October", "November"]:
    season = "Autumn"
elif month in ["December", "January", "February"]:
    season = "Winter"
elif month in ["March", "April", "May"]:
    season = "Spring"
elif month in ["June", "July", "August"]:
    season = "Summer"
else:
    season = "Invalid month"

# Print the season
print(f"The season is: {season}")
# 3.The following list contains some fruits:

fruits = ["banana", "orange", "mango", "lemon"]
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')
new_fruit = input("Enter a fruit: ").lower()

if new_fruit in fruits:
    print("That fruit already exist in the list of fruits!")
else:
    fruits.append(new_fruit)
    print(fruits)

# Exercises: Level 3
# 4.Here we have a person dictionary. Feel free to modify it!
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
# 1. Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    print(person["skills"])
    # Retrieve the list of skills from the dictionary
    skills_list = person["skills"]
    # Calculate the middle index of the skills list
    middle_index = len(skills_list) // 2  # 2.5=3
    middle_item = skills_list[middle_index]
    print(middle_item)
# 2. Check if the person dictionary has skills key,
# if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
    list_of_skill = person["skills"]
    if "Python" in list_of_skill:
        print(list_of_skill)
    else:
        print("The person does not have 'Python' skill.")
else:
    print("The 'skills' key is not in the dictionary.")

# 3. If a person skills has only JavaScript and React, print('He is a front end developer'),
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'),
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
# else print('unknown title') - for more accurate results more conditions can be nested!
if "skills" in person:
    list_of_skills = person["skills"]
    if (
        "Javascript" in list_of_skills
        and "React" in list_of_skills
        and len(list_of_skills) == 2
    ):
        print("He is frontend Developer")
    elif (
        "Node" in list_of_skills
        and "Python" in list_of_skills
        and "MongoDB" in list_of_skills
        and len(list_of_skills) == 3
    ):
        print("He is backend Developer")
    elif (
        "React" in list_of_skills
        and "Node" in list_of_skills
        and "MongoDB" in list_of_skills
        and len(list_of_skills) == 3
    ):
        print("He is a fullstack developer")
    else:
        print("Unknow title")
else:
    print("The 'skills' key is not in the dictionary.")
# 4. If the person is married and if he lives in Finland, print the information in the following format:
#  Asabeneh Yetayeh lives in Finland. He is married.
if person.get("country") == "Finland" and person.get("is_marred"):
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name} lives in finland. He is married.")
else:
    print("The person does not meet the criteria for the specified format.")

# Harry problem set. conditional
# 1.Write a program to find greatest of four numbers entered by the user.

user1 = int(input("Enter 1st number"))
user2 = int(input("Enter 2nd number"))
user3 = int(input("Enter 3rd number"))
user4 = int(input("Enter 4th number"))

list_number = max([user1, user2, user3, user4])

print(list_number)
# 2.Write a program to find out whether a student is pass or fail.
# if it requires total 40% and at least 33% in each subject to pass.
# Assume 3 subjects and take marks as an input from the user.
# Get marks for 3 subjects from the user
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

# Calculate total and percentage
total_marks = subject1 + subject2 + subject3
percentage = (total_marks / 300) * 100

# Check if the student has at least 33% in each subject and total is 40% or more
if subject1 >= 33 and subject2 >= 33 and subject3 >= 33 and percentage >= 40:
    print("Congratulations! The student has passed.")
else:
    print("Sorry, the student has failed.")

# 3.A spam comment is definded as a tect containing following keywords:
# "Make a lot of money,"buy now","subscribe this,"click this"
# Write a program to detect these spams.
comment = input("Enter a comment: ")
# Convert the comment to lowercase for case-insensitive comparison
comment_lower = comment.lower()
# Check if the comment contains any spam keywords
if "make a lot of money" in comment_lower:
    print("This comment is spam (contains 'make a lot of money').")
elif "buy now" in comment_lower:
    print("This comment is spam (contains 'buy now').")
elif "subscribe this" in comment_lower:
    print("This comment is spam (contains 'subscribe this').")
elif "click this " in comment_lower:
    print("This comment is spam (contains 'click this').")
else:
    print("This comment is not spam!")
# 4.Write a program to find whether a given username contains less than 10 characters or not.
username = input("Enter a username: ")

if len(username) < 10:
    print("The username is less than 10 characters")
else:
    print("The username contains 10 or more characters")

# 5.Write a program which finds out whether a given name is present in a list or not.
names_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
given_name = input("Enter a given name: ").capitalize()
if given_name in names_list:
    print("The name is in the list")
else:
    print("The given name is not in the List!")
# 6.Write a program to calculate the grade of a student from this marks from the following scheme:

# 90-100 -Excellent
# 80-90 -A
# 70-80 -B
# 60-70 -C
# 50-60 -D
# <50   -F
# Get the student's marks as input
marks = float(input("Enter the student's marks: "))

# Determine the grade using the 'and' operator
if marks >= 90 and marks <= 100:
    print("Grade: Excellent")
elif marks >= 80 and marks < 90:
    print("Grade: A")
elif marks >= 70 and marks < 80:
    print("Grade: B")
elif marks >= 60 and marks < 70:
    print("Grade: C")
elif marks >= 50 and marks < 60:
    print("Grade: D")
elif marks >= 0 and marks < 50:
    print("Grade: F")
else:
    print("Invalid marks entered. Please enter marks between 0 and 100.")

# 7.Write a program to find out whether a given post is talking about "Marry" or not.
# Get the post content from the user
post = input("Enter the post content: ")

# Convert the post to lowercase for case-insensitive comparison
post_lower = post.capitalize()

# Check if "marry" is mentioned in the post
if "Marry" in post_lower:
    print("The post is talking about Marry.")
else:
    print("The post is not talking about Marry.")
