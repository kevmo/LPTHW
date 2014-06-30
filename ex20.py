from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    #go back to very start of file
    #seek deals with bytes, not lines
    f.seek(0)

def print_a_line(line_count, f):
    #print sequential lines
    print line_count, f.readline()

current = open(input_file)

print "First, let's open the whole file \n"

print_all(current)

print "Now let's rewind"

rewind(current)

print "Let's print 3 lines:"

current_line = 1
print_a_line(current_line, current)

current_line = current_line + 1
print_a_line(current_line, current)

current_line = current_line + 1
print_a_line(current_line, current)
