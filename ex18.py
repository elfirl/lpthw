# this one is like oyur scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Mike", "Bilter")
print_two_again("Mike", "Bilter")
print_one("First!")
print_none()

# this is a test of my own
def my_own_test(num1, num2):
	total = int(num1) + int(num2)
	print "The sum is: %r" % total

my_own_test("3", "4")