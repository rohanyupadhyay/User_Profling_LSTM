import os
import win32gui
import threading
from threading import Timer
from threading import Thread
import pynput
from pynput import mouse
from pynput.mouse import Button
from pynput.keyboard import Key
from pynput import keyboard
import math
import os
import time

#os.system("tasklist")   
#print(win32gui.GetDoubleClickTime())

f=open("data.txt","a")

mData=[]
    
lclick=0
rclick=0
iloop=1
charc=0
def on_click(x, y, button, pressed):
    global lclick
    global rclick
    global iloop
    global mData
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
    if len(mData)==0:
        mData.append([time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None])
    else:
        if mData[-1]!=[time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None]:
            mData.append([time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None])
    if iloop==0:
        return False



def on_scroll(x, y, dx, dy):
    global iloop
    global mData
    print('Scrolled {0}'.format(
        (x, y)))
    print(dx,dy)
    if iloop==0:
        return False


def recMousList():
    global mlistener
    # Collect events until released
    with mouse.Listener(
            on_click=on_click,
            on_scroll=on_scroll) as mlistener:
        mlistener.join()


def recMousPos():
    global iloop
    global mData
    while iloop:
        if len (mData)==0:
            mData.append([time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None])
        else:
            if mData[-1] != [time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None]:  
                mData.append([time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None])
        #print(time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None)
    return False


def on_press(key):
    global charc
    print("press:" ,key)
    if isinstance(key,pynput.keyboard._win32.KeyCode):
        charc+=1
        print(charc)
    

def on_release(key):
    global iloop
    global charc
    if isinstance(key,pynput.keyboard._win32.KeyCode):
        charc-=1
        print(charc)
    print("release:",key)
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
            on_release=on_release) as klistener:
        klistener.join()    


t0=threading.Thread(target=recMousList,args=())
t1=threading.Thread(target=recMousPos,args=())
t2=threading.Thread(target=recKeybPress,args=())
t0.start()
t1.start()
t2.start()


Thread.join(t0)
Thread.join(t1)
Thread.join(t2)

f.write(str(mData))


