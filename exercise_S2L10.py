# 1. Create a list of names and print the second item.
#
names = ["Brett", "Andrea", "Devon", "Ryan"]
print(names[1])

# 2. Create a list of sports and then replace the second item with another sport.
#
sports = ["tennis", "rugby", "cycling"]
sports[1] = "handball"
print(sports)

# 3. Create an list containing numbers and delete the fifth number from the array.
#
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.pop(4)
print(numbers)

# 4. Create two list of numbers and merge them.
#
one = [0, 1, 2, 3, 4, 5]
two = [6, 7, 8, 9]
merge = one + two
print(merge)

# 5. Create an list of numbers and find the length, minimum, and maximum.
#
print(len(numbers), min(numbers), max(numbers))

# 6. Create an dictionary of students and scores print out a student’s score.
#
students = {"Brett": 95, "Andrea": 99}
print(students["Brett"])

# 7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.
#
ages = {"Brett": 42, "Andrea": 43}
del ages["Andrea"]
print(ages)

# 8. Create a dictionary of names and ages and then print out all the keys and values
#
ages = {"Brett": 42, "Andrea": 43}
print(ages.items())

# 9. Create a tuple of your favorite movies
#
movies = ("Rambo", "The Usual Suspects", "Grease", "A Beautiful Mind", "Dante's Peak")
print(movies)

# 10. Create a tuple and print all the items from the first to third index.
print(movies[:4])
