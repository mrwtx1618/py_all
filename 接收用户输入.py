# -*- coding:UTF-8 -*-
#现在利用argv和raw_input来向用户提一些特别的问题
from sys import argv
script,user_name = argv
promp = ':'
print "Hi, %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do U like me %s?" %user_name
likes = raw_input(promp)
print "Where do you live %s?" %user_name
lives = raw_input(promp)
print "what kind of computer do you have?"
computer = raw_input(promp)
print """
All right, so you have said %r about linking me.
You live in %r.Not sure where that is.
And you have a %r computer.Nice
""" % (likes,lives,computer)