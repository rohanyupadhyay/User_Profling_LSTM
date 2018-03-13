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

#l=ast.literal_eval(f.read())
#print(l[0])

a={}
b={}

a['a']=1
a['2']=2
a['3']=3

b['3']=3
b['2']=2

print(b==a)