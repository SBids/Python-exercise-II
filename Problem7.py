# 7. Create a list of tuples of first name, last name, and age for your friends and colleagues.
# If you don't know the age, put in None. Calculate the average age, skipping over any None values.
# Print out each name, followed by old or young if they are above or below the average age.

from statistics import mean

colleague_list = [('Taylor', 'Swift', 22), ('Justin', 'Timberlake', 36), ('Chris', 'Brown', None), ('James', 'Bay', 3)]
average = mean(x[2] for x in colleague_list if x[2] is not None)

for colleague in colleague_list:
    if colleague[2] is not None:
        if colleague[2] > average:
            print(colleague[0] + ' ' + colleague[1] + ' old')
        elif colleague[2] < average:
            print(colleague[0] + ' ' + colleague[1] + ' young')



