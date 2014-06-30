# namespace = format string
x = "there are %d types of people" % 10
binary = 'binary'
do_not = "don't"

# use parenthesis to pass mult vals to a format string
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y


print "I said: %r" % x
print "I also said: '%s' ." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"

print joke_evaluation % hilarious

w = "This is the left side of a "
e = "string with a right side."

# You can concat strings in python
print w + e