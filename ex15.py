# Gets the argv feature from the sys package
from sys import argv

# Unpacks the script name, and the filename entered when running the file
script, filename = argv

# Creates a file object and assigs it to the var txt
txt = open(filename)

# Prints the string, and the filename
print "Here's your file %r:" % filename

# Prints the content of the file object assigned to txt
print txt.read()

# Closes the file object assigned to txt
txt.close()

# Assigns the input from the command prompt to the file_again var
print "Type the filename again:"
file_again = raw_input("> ")

# Creates a file object and assigns it to the txt_again var
txt_again = open(file_again)

# Prints the contet of the file object assigned to txt_again
print txt_again.read()

# Closes the file object
txt_again.close()