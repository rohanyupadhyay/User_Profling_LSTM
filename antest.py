import threading
from threading import Timer
import pynput
from pynput import mouse
from pynput.mouse import Button, Controller
from pynput import keyboard
import math
import os


data=[]



class ntest:
 

    scrll=0
    clcksr=0
    clcksl=0
    keyps=0
    mous=0
    mouse=Controller()
    px=mouse.position[0]
    py=mouse.position[1]
    def afsec():
        for i in range (1000):
            print("afsec",i)      

    def strt():
        def on_move(x, y):
            #print('Pointer moved to {0}'.format((x, y)),ntest.px,ntest.py)
            ntest.mous+=math.sqrt(((x-ntest.px)*(x-ntest.px))+((y-ntest.py)*(y-ntest.py)))
            #print(ntest.mous)
            ntest.px=x
            ntest.py=y

        def on_click(x, y, button, pressed):
            #print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
            #print(button)
            if button == Button.left:
                ntest.clcksl+=0.5

            if button == Button.right: 
                ntest.clcksr+=0.5

            

        def on_scroll(x, y, dx, dy):
            #print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))
            ntest.scrll+=1


        def mousl():     
            with mouse.Listener(
                on_move=on_move,
                on_click=on_click,
                on_scroll=on_scroll) as listener:
                listener.join()



        def on_press(key):
            ntest.keyps+=1


        
        def keybl():
            with keyboard.Listener(
                on_press=on_press) as listener:
                listener.join()

        threading._start_new_thread(mousl,())
        threading._start_new_thread(keybl,())

        #print(os.getlogin())


def printit():
        threading.Timer(5.0, printit).start()
        data.append([ntest.mous,ntest.clcksl,ntest.clcksr,ntest.scrll,ntest.keyps])  
        #print(data)
        dfl=open("data.txt","a")
        if data != [[0,0,0,0,0]]:
            dfl.write(str(ntest.mous)+" "+str(ntest.clcksl)+" "+str(ntest.clcksr)+" "+str(ntest.scrll)+" "+str(ntest.keyps)+"\n")
            print(str(ntest.mous)+" "+str(ntest.clcksl)+" "+str(ntest.clcksr)+" "+str(ntest.scrll)+" "+str(ntest.keyps)+"\n")
        ntest.mous=0
        ntest.clcksl=0
        ntest.clcksr=0
        ntest.scrll=0
        ntest.keyps=0

printit()

ntest.strt()



