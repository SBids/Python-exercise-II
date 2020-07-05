# 18. Find a package in the Python standard library for dealing with JSON. Import the library module and inspect the
# attributes of the module. Use the help function to learn more about how to use the module. Serialize a dictionary
# mapping 'name' to you name and 'age' to your age, to a JSON string. Deserialize the JSON back into Python

import json

#help(json)

my_dict = {
    'name': 'Bidhya',
    'age': 22,
}

my_json = json.dumps(my_dict, sort_keys=True, indent=4)
print(my_json)


my_python = json.loads(my_json)
print(my_python)

# print(my_python["name"])
