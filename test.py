import win32gui
import pynput
from pynput import *
import time
from pynput import keyboard
from pynput.keyboard import Key, Listener
import ast
import os
import numpy as np

print(pynput.mouse.Controller().position[0])
print(time.time())

def on_release(key):
    global iloop
    print(key.value)
    if key == Key.esc:
        # Stop listener
        iloop=0
        return False


f2=open('final/pp_out.txt','r')
y=f2.readline()
y=ast.literal_eval(y)
print(len(y[:]))

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




