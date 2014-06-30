from sys import argv

script, user_name = argv
prompt = '> '

print "hi %s, I'm the %s script" % (user_name, script),
print "A few more questions!"
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "where do you live, %s" % user_name
lives = raw_input(prompt)

print "What kinda computer do you have, %s?" % user_name
computer = raw_input(prompt)

print """
Alright so you said the %r about liking me.
And you live in %r.
And you have an %r computer
""" % (likes, lives, computer)