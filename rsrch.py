import os
import win32gui
import threading
from threading import Timer
from threading import Thread
import pynput
from pynput import mouse
from pynput.mouse import Button, Controller
from pynput.mouse import Listener
from pynput import keyboard
import math
import os
import time

#os.system("tasklist")   
#print(win32gui.GetDoubleClickTime())

mData=[]
    


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))


def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))
    print(dx,dy)


def recMousList():        
    # Collect events until released
    print("2")
    with Listener(
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()


def recMousPos():
        while 1:
            mData.append([time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],None,None])
            print(time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1])



t0=threading.Thread(target=recMousList,args=())
t1=threading.Thread(target=recMousPos,args=())
t0.start()
t1.start()
