# -*- coding:utf-8 -*-
#print all .py file in that dir
import os

I = os.popen("dir /B *.py")
I = iter(I)
while True:
    try:
        print(next(I))
    except StopIteration:
        print("That's all.")
        break