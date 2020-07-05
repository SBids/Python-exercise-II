# 4. Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?

colleagues_list = []
print("The id of empty list : {}".format(id(colleagues_list)))
colleagues_list.append('Eliza')
colleagues_list.append('Lav')
colleagues_list.append('Deena')
colleagues_list.append('Lasata')
print("\n The id of friend list : {}".format(id(colleagues_list)))
colleagues_list = sorted(colleagues_list)
print("\n The id of sorted list : {}".format(id(colleagues_list)))

print("The first item on sorted list is : {}".format(colleagues_list[0]))
print("The second item on sorted list is : {}".format(colleagues_list[1]))


print("The id of friends in the  list is not changed even though they are sorted. \n"
      "The id of empty list and list with "
      "friends is also not changed. However the id of list is changed after sorting")
