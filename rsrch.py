import os
import win32gui
import threading
from threading import Timer
from threading import Thread
import pynput
from pynput import mouse
<<<<<<< HEAD
from pynput.mouse import Button
from pynput.keyboard import Key
=======
from pynput.mouse import Listener
>>>>>>> 30754f0aef3d520f7686293b85dfa49d5439bf12
from pynput import keyboard
from pynput.keyboard import Key, Listener
import os
import time

#os.system("tasklist")   
#print(win32gui.GetDoubleClickTime())


mData=[]
    
lclick=0
rclick=0
iloop=1
<<<<<<< HEAD
def on_click(x, y, button, pressed):
    global lclick
    global rclick
    global iloop
    print(button)
    if pressed:
        if button==Button.left:
            lclick=1
        if button==Button.right:
            rclick=1
    if not pressed:
        if button==Button.left:
            lclick=0
        if button==Button.right:
            rclick=0
    mData.append([time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None])
    if iloop==0:
        return False
=======
>>>>>>> 30754f0aef3d520f7686293b85dfa49d5439bf12

def on_click(x, y, button, pressed):
    print("click")
    global lclick
    global rclick
    global iloop

    if pressed:
        if button==Button.left:
            lclick=1
        if button==Button.right:
            rclick=1
    if not pressed:
        if button==Button.left:
            lclick=0
        if button==Button.right:
            rclick=0
    #mData.append([time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None])
    print(button)
    if iloop==0:
        print("False click")
        return False


def on_scroll(x, y, dx, dy):
    global iloop
    print('Scrolled {0}'.format(
        (x, y)))
    print(dx,dy)
    if iloop==0:
        print("False click")
        return False


<<<<<<< HEAD
def recMousList():
    global mlistener
    # Collect events until released
    with mouse.Listener(
            on_click=on_click,
            on_scroll=on_scroll) as mlistener:
        mlistener.join()
=======


>>>>>>> 30754f0aef3d520f7686293b85dfa49d5439bf12


def recMousPos():
    global iloop
    while iloop:
        mData.append([time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None])
        #print(time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None)
<<<<<<< HEAD
    return False
=======
        #print (iloop)
    print("end pos")
    #threading.current_thread()._stop


>>>>>>> 30754f0aef3d520f7686293b85dfa49d5439bf12


def on_press(key):
    print(key)

def on_release(key):
    global iloop
    print(key)
    if key == Key.esc:
        global mlistener
        mlistener.stop()
        # Stop listener
        iloop=0
        return False



def recKeybPress():
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
<<<<<<< HEAD
            on_release=on_release) as klistener:
        klistener.join()    
=======
            on_release=on_release,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()
    print("end press")
    #threading.current_thread()._stop

t=[]

t.append(threading.Thread(target=recMousPos,args=()))

t.append(threading.Thread(target=recKeybPress,args=()))

t[0].start()
t[1].start()

#t[0].join()
#t[1].join()

#print(threading.enumerate())




>>>>>>> 30754f0aef3d520f7686293b85dfa49d5439bf12


print("The End")
