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



f=open("data.txt","r")

l=f.readline()
l=ast.literal_eval(l)
#print(l['sTime'])
print(len(l))
lis=list(l.values())
print(lis)
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

tempx=list(range(1,4))
x=[]
for i in range(1):
    x.extend(tempx[i:i+3])
x=np.reshape(x,(1,3,1))



