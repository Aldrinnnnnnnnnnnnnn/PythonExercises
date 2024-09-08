# Exercises: Day 7
# sets
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# 1.Find the length of the set it_companies
print(len(it_companies))  # 7
# 2.Add 'Twitter' to it_companies
# Add one item using add()
# The update() allows to add multiple items to a set. The update() takes a list argument.
it_companies.add("Twitter")
print(it_companies)
# {'Apple', 'Amazon', 'Microsoft', 'Google', 'Oracle', 'Facebook', 'Twitter', 'IBM'}
# 3.Insert multiple IT companies at once to the set it_companies
it_companies.update(["Accenture", "Mozilla"])
print(it_companies)
# {'Apple', 'Amazon', 'Accenture', 'Facebook', 'Mozilla', 'Oracle', 'Twitter', 'Google', 'IBM', 'Microsoft'}
# 4.Remove one of the companies from the set it_companies
# The pop() methods remove a random item from a list and it returns the removed item.
it_companies.pop()
# {'Mozilla', 'Google', 'Facebook', 'Oracle', 'Twitter', 'IBM', 'Accenture', 'Microsoft', 'Amazon'}
print(it_companies)
# 5.What is the difference between remove and discard
# If the item is not found remove() method will raise errors.
# discard() method doesn't raise any errors.
# Exercises: Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
# 1.Join A and B
# We can join two sets using the union() or update() method.
# Union This method returns a new set.
c = A.union(B)
print(c)
# 2.Find A intersection B
# Intersection returns a set of items which are in both the sets.
result = A.intersection(B)
print(result)  # return ang magkaparehas using intersection.{19, 20, 22, 24, 25, 26}
# 3.Is A subset of B
# Subset: A smaller box that fits inside a bigger box (all its items are in the big box).
# Superset: The bigger box that holds everything from the smaller box and maybe more.
result = A.issubset(B)
print(result)  # True
# 4.Are A and B disjoint sets
# If two sets do not have a common item or items we call them disjoint sets.
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
result = B.isdisjoint(A)
print(result)  ## False, there are common items.{19,22,20,25,26,24}
# 5.Join A with B and B with A
# We can join two sets using the union() or update() method.
join_AwithB = A.union(B)
join_BwithA = B.union(A)
print(join_AwithB)  # {19, 20, 22, 24, 25, 26, 27, 28}
print(join_BwithA)  # {19, 20, 22, 24, 25, 26, 27, 28}
# 6.What is the symmetric difference between A and B
# It returns the the symmetric difference between two sets. It means that it returns a set that contains all items from both sets,
# except items that are present in both sets.
c = B.symmetric_difference(A)
print(c)  # {27, 28}
# 7.Delete the sets completely
del A
del B

# Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]
# 1.Convert the ages to a set and compare the length of the list and the set, which one is bigger?
is_set = set(age)
print(is_set)  # {19, 22, 24, 25, 26}
print(len(age))  # 8,Because it is a list
print(len(is_set))  # 5,converted to set. set dont allow 2 same items.
# 2.Explain the difference between the following data types: string, list, tuple and set
"""
1.String: Immutable text.Fixed line of text.
2.List: Mutable, ordered collection.[]Flexible, ordered list where you can change items.
3.Tuple: Immutable, ordered collection.()Fixed, ordered list where items can’t be changed.
4.Set: Mutable, unordered collection with unique items.{}Collection of unique items without order.
"""
# 3.I am a teacher and I love to inspire and teach people.
# 1.How many unique words have been used in the sentence?
# 2.Use the split methods and set to get the unique words.
# Define the sentence
sentence = "I am a teacher and I love to inspire and teach people."
# Split the sentence into words
# The split() method in Python is used to break a string into a list of substrings based on a specified delimiter.
words = sentence.split()
# ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people.']
# Convert the list of words into a set to get unique words
unique_words = set(words)
# Print the unique words
print("Unique words:", unique_words)

# Print the number of unique words
print("Number of unique words:", len(unique_words))
