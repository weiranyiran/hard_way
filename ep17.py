# -*- coding:utf-8 -*-

from sys import argv
from os.path import exists

sript, from_file, to_file = argv

print ("Copy from %s to %s"%(from_file,to_file))

in_file = open(from_file)
indata = in_file.read()

print("The input file is %d bytes long"% len(indata))

print("Does the ouput file exist? %r"% exists(to_file))
print("Ready,hit ruturn to continue,CTRL-C to abort.")
input()#接受回车
out_file = open(to_file,'w')
out_file.write(indata)

print ("Alright,all done.")

out_file.close()
in_file.close()