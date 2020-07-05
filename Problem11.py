# 11.  Create a variable, filename. Assuming that it has a three-letter extension, and using slice operations, find the
# extension. For README.txt, the extension should be txt. Write code using  slice operations that will give the name
# without the extension. Does your code work on filenames of arbitrary length?


filename = 'python-exercise.txt'
extension = filename[slice(-1, -4, -1)]
print(extension)
extensionless_filename = filename[slice(0, -4, 1)]
print(extensionless_filename)

