#Exercises: Level 1
#1.Declare an empty list
empty_list = []
#2.Declare a list with more than 5 items
empty_list = ['Aldrin',1,3-3j,False,True,]
#3.Find the length of your list
print(len(empty_list))
#4.Get the first item, the middle item and the last item of the list
my_list = [10, 20, 30, 40, 50, 60, 70,80,90]
first_item = my_list[0]
middle_index = len(my_list) // 2 #= 3 index
middle_item =my_list[middle_index]
last_item = my_list[-1]
print(first_item,middle_item,last_item)#10 40 70
#5.Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Aldirn',22,163,'single','Philippines']

#6.Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
#7.Print the list using print()
print(it_companies)
#8.Print the number of companies in the list
print(len(it_companies))
#9.Print the first, middle and last company
first_item = it_companies[0]
middle_index = len(it_companies) // 2 #3 ='Apple' --7 ÷ 2 equals 3.5, but with floor division, the decimal part (.5) is discarded, and the result is 3.
middle_item = it_companies[middle_index]
last_item = it_companies[-1]
print(first_item,middle_item,last_item)
#10.Print the list after modifying one of the companies
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
it_companies[1] = 'Accenture'

#7.Print the list using print()
print(it_companies)
#['Facebook', 'Accenture', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#11.Add an IT company to it_companies
add_item = it_companies.append('IT Company')
print(it_companies)
#['Facebook', 'Accenture', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'IT Company']
#12.Insert an IT company in the middle of the companies list
# Calculate the middle index
middle_index = len(it_companies) // 2
# Insert a new IT company in the middle (for example, 'IT Company')
it_companies.insert(middle_index,'It company')
print(it_companies)


#13.Change one of the it_companies names to uppercase (IBM excluded!)
#The assignment operator (=) takes the result of it_companies[2].upper() (which is "MICROSOFT")
# and replaces the value at index 2 of the it_companies list.
it_companies[2] = it_companies[2].upper()
print(it_companies)
#14.Join the it_companies with a string '#;  '
modified = '#; '.join(it_companies)
print(modified)#Facebook#; Accenture#; MICROSOFT#; Apple#; It company#; IBM#; Oracle#; Amazon#; IT Company
#15.Check if a certain company exists in the it_companies list.
does_exist = 'Facebook' in it_companies
print(does_exist)#True
#16.Sort the list using sort() method
it_companies.sort()#Ascending order
print(it_companies)#['Accenture', 'Amazon', 'Apple', 'Facebook', 'IBM', 'IT Company', 'It company', 'MICROSOFT', 'Oracle']

#17.Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)#Descending order
print(it_companies)
#18.Slice out the first 3 companies from the list
#['Oracle', 'MICROSOFT', 'It company', 'IT Company', 'IBM', 'Facebook', 'Apple', 'Amazon', 'Accenture']
#19.Slice out the last 3 companies from the list
sort_out = it_companies[6:]
print(sort_out)#['Apple', 'Amazon', 'Accenture']
#20.Slice out the middle IT company or companies from the list
sort_out = it_companies[4]
print(sort_out)

#21.Remove the first IT company from the list
#['Oracle', 'MICROSOFT', 'It company', 'IT Company', 'IBM', 'Facebook', 'Apple', 'Amazon', 'Accenture']
it_companies.pop(0)
#['MICROSOFT', 'It company', 'IT Company', 'IBM', 'Facebook', 'Apple', 'Amazon', 'Accenture']
print(it_companies)
#22.Remove the middle IT company or companies from the list
#['MICROSOFT', 'It company', 'IT Company', 'IBM', 'Facebook', 'Apple', 'Amazon', 'Accenture']
middle_index = len(it_companies) // 2
it_companies.pop(middle_index)
print(it_companies)
#['MICROSOFT', 'It company', 'IT Company', 'IBM', 'Apple', 'Amazon', 'Accenture']
#23.Remove the last IT company from the list
it_companies.pop()
print(it_companies)
#['MICROSOFT', 'It company', 'IT Company', 'IBM', 'Apple', 'Amazon']
#24.Remove all IT companies from the list
#del it_companies
#print(it_companies)#NameError: name 'it_companies' is not defined
#25.Destroy the IT companies list
it_companies.clear()
print(it_companies) #[]
#26.Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)
#['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
#or
front_end.extend(back_end)
print(front_end)
#['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
#27.After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy()
print(full_stack)
#['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
#Exercises: Level 2
#1.The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#1Sort the list and find the min and max age
ages.sort()#[19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
ages.sort(reverse='True')#[26, 25, 25, 24, 24, 24, 22, 20, 19, 19]
min_age = min(ages)
max_age = max(ages)
print(f"The minimum is:{min_age} and The maximun is {max_age}" )
#2Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)
#3Find the median age (one middle item or two middle items divided by two)
#[26, 25, 25, 24, 24, 24, 22, 20, 19, 19, 19, 26]
middle_index = len(ages) // 2
middle_item = ages[middle_index]
print(middle_item)#22
#4Find the average age (sum of all items divided by their number )
total_sum = sum(ages)#273
number_of_items = len(ages)#12
average_age = total_sum / number_of_items
print(average_age)#22.75
#5Find the range of the ages (max minus min)
# Find the minimum and maximum age
min_age = min(ages)
max_age = max(ages)
# Calculate the range
age_range = max_age - min_age

# Print the range
print("Range of ages:", age_range)
#6Compare the value of (min - average) and (max - average), use abs() method
# List of student ages
ages = [26, 25, 25, 24, 24, 24, 22, 20, 19, 19, 19, 26]

# Calculate the minimum, maximum, and average age
min_age = min(ages)
max_age = max(ages)
average_age = sum(ages) / len(ages)

# Calculate the differences
min_diff = min_age - average_age
max_diff = max_age - average_age

# Compute the absolute values
abs_min_diff = abs(min_diff)
abs_max_diff = abs(max_diff)

# Print the results
print("Absolute difference (min - average):", abs_min_diff)
print("Absolute difference (max - average):", abs_max_diff)

#1.Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
middle_index = len(countries) // 2#96
print(middle_index)
middle_item = countries[middle_index]
print(middle_item)#Lesotho
#2.Divide the countries list into two equal lists if it is even if not one more country for the first half.
# Calculate the split index
''split_index = (len(countries) + 1) // 2

# Divide the list into two parts
first_half = countries[:split_index]
second_half = countries[split_index:]

# Print the two halves
print("First half:", first_half)
print("Second half:", second_half)''
#3.['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
# Unpack the first three countries
countries = [
    'China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'
]

# Unpacking the first three countries
first_three = countries[:3]

# The rest of the countries (Scandinavian countries)
scandinavian_countries = countries[3:]

print("First Three Countries:", first_three)
print("Scandinavian Countries:", scandinavian_countries)
