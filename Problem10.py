# 10. Write a function that takes camel-cased strings (i.e. ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument, separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

from functools import reduce


def convert_case(my_string, separator):
    return reduce(lambda x, y: x + (separator if y.isupper() else '') + y, my_string).lower()


str = 'PythonExerciseFromInsightWorkshop'
sep = '_'
print(convert_case(str, sep))


