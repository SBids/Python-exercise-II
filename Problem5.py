# 5. Create a tuple with your first name, last name, and age. Create a list, people, and append your tuple to it.
# Make more tuples with the corresponding information from your friends and append them to the list. Sort the list.
# When you learn about sort method, you can use the key parameter to sort by any field in the tuple, first name, l
# ast name or age.

my_tuple = ('Taylor', 'Swift', 22)
people = [my_tuple, ]
justin_tuple = ('Justin', 'Timberlake', 36)
chris_tuple = ('Chris', 'Brown', 33)
people.append(justin_tuple)
people.append(chris_tuple)

sorted_people = sorted(people, key=lambda x: x[2])
print(sorted_people)


