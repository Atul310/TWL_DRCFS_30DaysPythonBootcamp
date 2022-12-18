'''
Write a Python function called read_file() that takes a single parameter
filename, and opens the specified file in read-only mode. 
The function should read the entire contents of the file and return the contents as a string.
'''

def read_file(filename):
    with open ("Week 2\Assignments\my_file.txt","r") as filename:
      return filename.read()
    # TODO: Open the file in read-only mode and read its contents. Return the contents of the file.
   

contents = read_file(filename="my_file.txt")
print(contents)  # Output: "Hello, world!\nI just did my first Assignment of week 2."
