from sklearn import svm
from sklearn.cluster import KMeans
from sklearn.svm import OneClassSVM
import numpy as np
import array
import threading
from threading import Timer
import pynput
from pynput import mouse
from pynput.mouse import Button, Controller
from pynput import keyboard
import math
import os

fl= open("data.txt","r")
rwdt=fl.readlines()

#print(rwdt)
smpl_sz=len(rwdt)
dt=[]
clss=[]
for i in range(1,smpl_sz,1):
    dt.append(rwdt[i].split())
#print(dt)
clss=[]
for i in range(1,smpl_sz,1):
    clss.append(0)
#print(clss)


X=np.array(dt)
#print(X)
#kmeans=KMeans(n_clusters=1, random_state=0).fit(X)
#print(kmeans.labels_)
#for i in range(0,len(kmeans.cluster_centers_),1):
        #for j in kmeans.cluster_centers_[i]:
            #print(float(j))
#print(kmeans.cluster_centers_)
#print(kmeans.predict([[2000,7,4,10,5],[2000,7,4,10,5]]))
okso=OneClassSVM()
#okso.fit(X)
oks=okso.fit(X)
#oks.predict(X)
#print(okso.decision_function(X))
#print(okso.predict(X))
#print(oks)
#print(oks.predict(X))
#arr=np.array([2000,7,4,10,5])
#arr=arr.reshape(1,-1)




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
        arr=np.array([ntest.mous,ntest.clcksl,ntest.clcksr,ntest.scrll,ntest.keyps])
        arr=arr.reshape(1,-1)
        #print(arr)
        print()
        print(oks.decision_function(arr))
        print(oks.predict(arr))
        #print(data)
        #dfl=open("data.txt","a")
        #dfl.write(str(ntest.mous)+" "+str(ntest.clcksl)+" "+str(ntest.clcksr)+" "+str(ntest.scrll)+" "+str(ntest.keyps)+"\n")
        ntest.mous=0
        ntest.clcksl=0
        ntest.clcksr=0
        ntest.scrll=0
        ntest.keyps=0

printit()

ntest.strt()




