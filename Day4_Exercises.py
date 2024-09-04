#1.Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
letters = ['Thirty','Days','Of', 'Python']
result = ' '.join(letters)
print(result)

letter = 'Thirty' + ' ' +'Days'+ ' '+ 'of'+ ' ' +'Python'
print(letter)
#2.Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
code = 'Coding ,'+ ' ' +'For ,'+ ' ' +'All'
print(code)

code1 = ['Coding','For','All']
result = ' '.join(code1)
print(result)
#3.Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For ALL"
#4.Print the variable company using print().
print(company)#Coding For ALL
#5.Print the length of the company string using len() method and print().
print(len(company))#Coding For ALL=14
#6.Change all the characters to uppercase letters using upper() method.
print(company.upper())#=CODING FOR ALL
#7.Change all the characters to lowercase letters using lower() method.
print(company.lower())#=coding for all
#8.Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())#Coding for all. it capitalize first character.
print(company.title())#Coding For All. Returns a title cased string
print(company.swapcase())#cODING fOR all.Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
#9.Cut(slice) out the first word of 'Coding For All' string.
print(company[:6])#=Coding
#10.Check if Coding For All string contains a word Coding using the method index, find or other methods.
coding_in_company = 'Coding' in company
print(coding_in_company)#=True
print(company.index('Coding'))#=0The index() method works similarly to find(), but it raises a ValueError if the substring is not found.
print(company.find('Coding'))#=0. If the substring is not found, it returns -1. Since "Coding" is at the beginning of the string, it returns 0.
#11.Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding','Python'))#Python For ALL
#12.Change Python for Everyone to Python for All using the replace method or other methods.
let = "Python for Everyone"
print(let.replace('Everyone','All'))#Python for All
#13.Split the string 'Coding For All' using space as the separator (split()) .
spl = 'Coding for All'
print(spl.split(', '))#['Coding for All']
#14."Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
words = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(words.split(','))#['Facebook', ' Google', ' Microsoft', ' Apple', ' IBM', ' Oracle', ' Amazon']
#15.What is the character at index 0 in the string Coding For All.
wordss = 'Coding for All'
print(wordss[0])#C
#16.What is the last index of the string Coding For All.
print(wordss[13])#l
#17.What character is at index 10 in "Coding For All" string.
print(wordss[10])#space
#18.Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = 'Python For Everyone'
words = phrase.split()#['Python', 'For', 'Everyone']
# Create acronym by manually concatenating the first letters
acronym = words[0][0].upper() + words[1][0].upper() + words[2][0].upper()
print(words)#PFE
#19.Create an acronym or an abbreviation for the name 'Coding For All'.
name = 'Coding For all'
name_split = name.split()#['Coding', 'For', 'all']
name_acronym = name_split[0][0].upper() + name_split[1][0].upper() + name_split[2][0].upper()
print(name_acronym)#CFA
#20.Use index to determine the position of the first occurrence of C in Coding For All.
occurence_of_C = 'Coding For All'
print(occurence_of_C.index('C'))#=0
#21.Use index to determine the position of the first occurrence of F in Coding For All.
print(occurence_of_C.index('F'))#=7
#22.Use rfind to determine the position of the last occurrence of l in Coding For All People.
find_position = 'Coding For All People'
print(find_position.rfind('l'))
#23.Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
find_the_position = 'You cannot end a sentence with because because because is a conjunction'
print(find_the_position.index('because'))#31
print(find_the_position.find('because'))#31
#24.Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
last_occurence = 'You cannot end a sentence with because because because is a conjunction'
print(last_occurence.rindex('because'))#47
#25.Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
slice_out_because = 'You cannot end a sentence with because because because is a conjunction'
convert = slice_out_because.split()
out_because = convert[6] +' ' + convert[7] + ' ' +convert[8]
print(out_because)#because because because
#other method
start_index = slice_out_because.index('because')
end_index = start_index + len('because because because')

# Slicing the phrase
sliced_phrase = slice_out_because[start_index:end_index]
print(sliced_phrase)#because because because
#26.Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))#31
#27.Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start_ind = sentence.index('because')
last_ind = start_ind + len('because because because')
#slicing the phrase
sliced = sentence[start_ind:last_ind]
print(sliced)#because because because
#28.Does ''Coding For All' start with a substring Coding?
sen = 'Coding For All' 
sub_string = 'Coding'
# Check if the sentence starts with the substring
start_sub =sen.startswith(sub_string)
print(start_sub)#=True
#29.Does 'Coding For All' end with a substring coding?
sen = 'Coding For All' 
sub_string = 'coding'
# Check if the sentence if ends with coding
last_sub = sen.endswith(sub_string)
print(last_sub)#False


#30.'   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence = "  Coding For all  "

# Strip leading and trailing spaces, then slice out the first and last characters
result = sentence.strip()[0:14]

print(f"'{result}'")#'Coding For all'

#31.Which one of the following variables return True when we use the method isidentifier():
#Checks for a valid identifier - it checks if a string is a valid variable name
  #30DaysOfPython
  #thirty_days_of_python
sentence1 = '30DaysOfPython'
sentence2 = 'thirty_days_of_python'
print(sentence1.isidentifier())#False, because it starts with a number
print(sentence2.isidentifier())#True
#32.The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list1))#Django# Flask# Bottle# Pyramid# Falcon
#33.Use the new line escape sequence to separate the following sentences.
  #I am enjoying this challenge.
  #I just wonder what is next.
print('I am enjoying this challenge.\nI just wonder what is next.')

#34.Use a tab escape sequence to write the following lines.
  #Name      Age     Country   City
  #Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity\nAsabaneh\t250\tFinland\tHelsinki')
#35.Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square
print(f"The area of a circle with radius {radius} is {area} meters square")
#36.Make the following using string formatting methods:
a = 8
b = 6

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
floor_division = a // b
exponentiation = a ** b

formatted_strings = (
    f"{a} + {b} = {addition}\n"
    f"{a} - {b} = {subtraction}\n"
    f"{a} * {b} = {multiplication}\n"
    f"{a} / {b} = {division:.2f}\n"
    f"{a} % {b} = {modulus}\n"
    f"{a} // {b} = {floor_division}\n"
    f"{a} ** {b} = {exponentiation}"
)

print(formatted_strings)

#Harry Practice set
#1.Write a python program to display a user entered name followed  by Good Afternoon using input() function
user = input("Enter a name: ")
print(f"Good afternoon {user}")
#2.Write a program to fill in a letter template  given below  with name and date:
  #letter = ''' Dear <name>,You are selected!<Date>'''
name = "Aldrin"
date = 'september 4 2024'
print(f"Dear {name}, You are selected! {date} ")
#3.Write a program to detect double spaces in a string.
text = 'python  program  to display a user'
print(text.find('  '))
#4.Replace the double spaces from problem 3with single spaces.
print(text.replace('  ',' '))
#5.Write a program to format  the following letter using escape sequence character.
letter = "Dear Harry,\nThis Python course is nice.\nThanks!"
print(letter)