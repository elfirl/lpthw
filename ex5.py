name = 'Mike S. Bilter'
age = 36 # Not a lie
height = 73 # Inches
weight = 200 # This IS a lie
eyes = 'Blue'
teeth = 'White'
hair = 'Blonde'

print "Let's talk about %s." % name
print "He's %d inches tall" % height
print "He's %d heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d" % (
	age, height, weight, age + height + weight)