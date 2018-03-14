import win32gui
import pynput
from pynput import *
import time
from pynput import keyboard
from pynput.keyboard import Key, Listener
import ast

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
print(l['sTime'])
print(len(l))
#print(l[0])



