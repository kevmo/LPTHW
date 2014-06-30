from sys import argv
from os.path import exists

file_from = raw_input("Which file to copy? ")
file_to = raw_input("Into which file? ")

old = open(file_from, 'r')
new = open(file_to, 'w')

data = old.read()

print "The %s file is %r bytes long." % (file_from, len(data))

print "Does the %s file really exist? %r" % (file_from, exists(file_from))

print "Ready? Hit return to continue, Control-C to quit"

raw_input()

new.write(data)

old.close()
new.close()