# -*- coding:utf-8 -*-

x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary,do_not)
print (x)
print (y)

print ("I said: %r." % x)
print ("I also said: '%s'" % y)
hilarious = False
joke_evaluation = "Isn't that joke so funny?! % r"

print (joke_evaluation % hilarious)

w = "this is the left side of..."
e = "a string with a right side."

print (w+e)
#变量里面可以用格式化字符串 字符串变量也可以做格式化字符串
