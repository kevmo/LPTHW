# sys is a module in standard python library.
# argv is a Python list of args passed on the command
# line.  argv[0] == script name == lp13.py
from sys import argv

uno, dos, tres = argv

print "The script is called: ", uno
print "The first var is called: ", dos
print "The second var is called", tres

print "Well? ", argv[0] == 'lp13.py'

raw_input("Sup? ") =
print argv