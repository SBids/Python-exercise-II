# 6. Create a list with the names of friends and colleagues. Search for the name ‘John’ using a for a loop.
# Print ‘not found’ if you didn't find it.

colleague_list = ['Ram', 'Shyam', 'Hari', 'Sita', 'Rita', 'Gita']
for colleague in colleague_list:
    if colleague == 'John':
        print("John found")
else:
    print("not found")
