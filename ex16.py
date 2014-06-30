from sys import argv


script, filename = argv

print "We're going to erase %r" % filename
print "If you dont want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("Well?")

print "Opening the file..."
target = open(filename, 'r+')

print "Truncating the file!"
target.truncate()

print "Now Imm ask you for 3 - count em - lines"

line1 = raw_input ("1? ")
line2 = raw_input("2? ")
line3 = raw_input("3 ?")

print "Imma write them to a file"

result = line1.join(line2).join(line3)

print "result: " + result

# print result

target.write(line1)

print target.read()

