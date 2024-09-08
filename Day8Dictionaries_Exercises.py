#Exercises: Day 8
#1.Create an empty dictionary called dog
dog = {}
print(type(dog))#<class 'dict'>
#2.Add name, color, breed, legs, age to the dog dictionary
dog = {
  'name':'Heidi',
  'color':'Mahogani',
  'breed':'Belgian',
  'legs':4,
  'age':2
}
#3.Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
  'first_name':'Aldrin',
  'lat_name':'Tamonte',
  'gender':'Male',
  'age':22,
  'marital status':'single',
  'skills':['Pyhton','C++','Javascript'],
  'country':'philippines',
  'city':'San fabian',
  'address':{
  'street':'Bolasi',
  'zip_code':2433
  }
}
#4.Get the length of the student dictionary
print(len(student))#9
#5.Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))#<class 'list'>
#6.Modify the skills values by adding one or two skills
student['skills'] += ['Java','Ruby']
print(student)
#7.Get the dictionary keys as a list
keys_as_list = student.keys()
print(keys_as_list)
#dict_keys(['first_name', 'lat_name', 'gender', 'age', 'marital status', 'skills', 'country', 'city', 'address'])
#<class 'dict'>
#8.Get the dictionary values as a list
values_as_list = student.values()
print(values_as_list)
#dict_values(['Aldrin', 'Tamonte', 'Male', 22, 'single', ['Pyhton', 'C++', 'Javascript', 'Java', 'Ruby'], 'philippines', 'San fabian', {'street': 'Bolasi', 'zip_code': 2433}])
#9.Change the dictionary to a list of tuples using items() method.
dict_to_list = student.items()
print(dict_to_list)
#dict_items([('first_name', 'Aldrin'), ('lat_name', 'Tamonte'), ('gender', 'Male'), ('age', 22), ('marital status', 'single'), ('skills', ['Pyhton', 'C++', 'Javascript', 'Java', 'Ruby']), ('country', 'philippines'), ('city', 'San fabian'), ('address', {'street': 'Bolasi', 'zip_code': 2433})])
#10.Delete one of the items in the dictionary
student.popitem()
print(student)
#11.Delete one of the dictionaries
del student['first_name']
print(student)

#Set and dictionaries harry problem sets
#1.Write a program to create a dictionary of Hindi words with value as  their english translation.
  #Provide user with an option to look it up!
# Define the dictionary with Hindi words and their English translations
hindi_to_english = {
    'नमस्ते': 'Hello',
    'धन्यवाद': 'Thank you',
    'पानी': 'Water',
    'खाना': 'Food',
    'सपना': 'Dream',
    'मित्र': 'Friend',
    'सपोर्ट': 'Support'
}
def loop_for_word ():
# Ask the user to enter a Hindi word
  hindi_word = input("Enter a Hindi word: ")
#Use the get method to fetch the translation from the dictionary.
#The get method returns None, which is a NoneType object data type, if the key does not exist.
#ex .get()print(person.get('first_name')) # Asabeneh
#get(): It’s a special tool that looks up a word in our dictionary. 
#If the word isn’t found, it gives a message saying "Translation is not found".
  translation = hindi_to_english.get(hindi_word,"Translation is not found")
# Print the result.
  print(f"The english Translation is: {hindi_word} is {translation}")
#This actually makes the function start working and perform its task, which is to ask for a Hindi word and then show its English translation.
loop_for_word()


#2.Write a program to input eight numbers from the user and display all the unique number(once.)
user1 = int(input('Enter a number: '))
user2 = int(input('Enter a number: '))
user3 = int(input('Enter a number: '))
user4 = int(input('Enter a number: '))
user5 = int(input('Enter a number: '))
user6 = int(input('Enter a number: '))
user7 = int(input('Enter a number: '))
user8 = int(input('Enter a number: '))
list_of_set = {user1,user2,user3,user4,user5,user6,user7,user8}
print(list_of_set)
'''
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 4
Enter a number: 5
Enter a number: 5
Enter a number: 5
Enter a number: 6
{1, 2, 3, 4, 5, 6}
'''
#3.Can we have a set with 18(int) and "18"(str) as a number as a value in it?
'''
yes. Since 18 and "18" are of different types (integer and string), 
they are considered different elements and thus both can exist in the same set.
'''
# Create a set with both integer 18 and string "18"
my_set = {18, "18"}

# Print the set to see its contents
print(my_set)

#4.What will be the length of following set S.
S = set()
print(len(S))#0
S.add(20)
print(len(S))#1
S.add(20.0)
print(len(S))#1
S.add("20") #=> length of S after these operations?
print(len(S))#2
#5.
S ={} #What is the type of S?
print(type(S))#<class 'dict'>
#6.Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names.
  #Assume that the name are unique.
user1 = input('Enter a language: ')
user2 = input('Enter a language: ')
user3 = input('Enter a language: ')
user4 = input('Enter a language: ')
empty_dict = {
  'John': user1,
  'Tom': user2,
  'Jordan': user3,
  'Jerome': user4
}
print(empty_dict)#{'John': 'English', 'Thom': 'Tgalog', 'Jordan': 'Hindi', 'Jerome': 'Ilocano'}
#7.If names of 2 friends are same; What will to the program in Problem6?
#It will not print the second same name.it only prints the first name.
#a dictionary is a data structure that stores key-value pairs. Each key in the dictionary is unique and is used to access its corresponding value. 
# Think of a dictionary as a map where you use keys to find specific pieces of information.
#{'John': 'Tagalog', 'Jordan': 'Hindi', 'Jerome': 'Arabic'}

#8.If languages  of two friends are same; what will happen to the program in Problem 6?
#it will print the same value pairs. it allowed it value but in key is not allowed to duplicate.
#{'John': 'English', 'Tom': 'English', 'Jordan': 'Tagalog', 'Jerome': 'Arabic'}
#9.Can you change the values inside a list which is contained in set S.
S = {8,7,12,'Harry',[1,2]}#TypeError: unhashable type: 'list'
#set is a collection of unique and immutable (unchangeable) elements. Because of this immutability requirement, 
# a set cannot contain mutable elements, such as lists.
print(S)