# create a list
fruits = ['apple', 'banana', 'cherry']

# access elements by index
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Third fruit:", fruits[2])

# add an element to the end of the list
fruits.append('date')
print("Fruits after appending:", fruits)

# insert an element at a specific position
fruits.insert(1, 'orange')
print("Fruits after inserting:", fruits)

# remove an element by value
fruits.remove('banana')
print("Fruits after removing:", fruits)

# remove an element by index
del fruits[1]
print("Fruits after deleting:", fruits)

# find the index of an element
print("Index of cherry:", fruits.index('cherry'))

# check if an element is in the list
print("Is date in the fruits list:", 'date' in fruits)

# number of elements in the list
print("Number of fruits:", len(fruits))

# sort the list
fruits.sort()
print("Sorted fruits:", fruits)

# reverse the list
fruits.reverse()
print("Reversed fruits:", fruits)
