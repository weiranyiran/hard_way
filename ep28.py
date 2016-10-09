# -*- coding:utf-8 -*-
#to print the true or false or the input expression
x = input("Input your expression:\n")
while(x!="q"):
    if(eval(x)):
        print("The answer is True")
    else:
        print("The answer is Fasle")
    x = input("Input your expression:\n")