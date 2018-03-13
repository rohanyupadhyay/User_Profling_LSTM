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

mData={}
tempData={}

mData['charc']=0
mData['lClick']=0
mData['rClick']=0
mData['mClick']=0
mData['absTime']=time.time()
mData['space']=0
mData['backSpace']=0
mData['delete']=0
mData['ctrl']=0
mData['alt']=0
mData['capsLock']=0
mData['shift']=0
mData['tab']=0
mData['numLock']=0
mData['enter']=0

iloop=1

charPrsd=[]
def on_click(x, y, button, pressed):
    global iloop
    print (button)
    if pressed:
        if button==Button.left:
            mData['lClick']+=1
        if button==Button.right:
            mData['rClick']+=1
        if button==Button.middle:
            mData['mClick']+=1
    if not pressed:
        if button==Button.left:
            mData['lClick']-=1
        if button==Button.right:
            mData['rClick']-=1
        if button==Button.middle:
            mData['mClick']-=1
    print(mData['lClick'],mData['mClick'],mData['rClick'])
    mData['absTime']=time.time()



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
        pass
        #print(time.time(),pynput.mouse.Controller().position[0],pynput.mouse.Controller().position[1],lclick,rclick,None,None)
    return False


def on_press(key):
    print("press:" ,key)
    if isinstance(key,pynput.keyboard._win32.KeyCode) and key not in charPrsd:
        charPrsd.append(key)
        mData['charc']+=1
        print(mData['charc'])
    

def on_release(key):
    global iloop
    global charc
    if isinstance(key,pynput.keyboard._win32.KeyCode):
        charPrsd.remove(key)
        mData['charc']-=1
        print(mData['charc'])
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


