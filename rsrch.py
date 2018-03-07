import os
import win32gui
import threading
from threading import Timer
from threading import Thread
import pynput
from pynput import mouse
from pynput.mouse import Listener
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






def recMousPos():
    global iloop
    while iloop:
        mData.append([time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None])
        #print(time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None)
        #print (iloop)
    print("end pos")
    #threading.current_thread()._stop




def on_press(key):
    print(key)

def on_release(key):
    global iloop
    print(key)
    if key == Key.esc:
        # Stop listener
        iloop=0
        return False



def recKeybPress():
    # Collect events until released
    with Listener(
            on_press=on_press,
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






print("The End")
