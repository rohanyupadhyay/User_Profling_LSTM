import win32gui
import pynput
from pynput import *
import time
from pynput import keyboard
from pynput.keyboard import Key, Listener
import ast
import os
import numpy as np


f1=open('final/test/pp_in_1.txt','r')

'''
for i in range(500):
    w1.write(f1.readline())

for i in range(500):
    w2.write(f2.readline())

for i in range(500):
    w3.write(f3.readline())
'''
print(len(ast.literal_eval(f1.readline())))

#x1=open('final/in/pp_in_146.txt','r')

#y1=x1.readline()

#y1=ast.literal_eval(y1)
#print(len(y1))





#lis=list(l.values())
#print(lis)
#print(l[0])



#print(os.environ['USERNAME'])
'''
newx=list(range(1,11,1))
print(newx)

def square(lst):
    return list(map(lambda x: x ** 2, lst))

newy=square(newx)
print(newy)
'''




