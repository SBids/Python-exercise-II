# 13. Write a function to write a comma-separated value file. It should accept a filename and a list of tuples as
# parameters. The tuples should have a name, address, and age. The file should create a header row followed by a row for
# each tuple. If the following list of tuples was passed in :
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21

import csv


def write_csv(filename, tuple_lists):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        row_header = ['name', 'address', 'age']
        writer.writerow(row_header)
        writer.writerows(tuple_lists)


tuple_list = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
file_name = 'csv_write.csv'
write_csv(file_name, tuple_list)
