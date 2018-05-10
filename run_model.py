import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np
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
import time

cData=[]
cData.append([])



stime=time.time()
ltime=0
mData={}
tempData={}
#mData['user']=os.environ['USERNAME']

mData['charc']=0
mData['lClick']=0
mData['rClick']=0
mData['mClick']=0
#mData['sTime']=time.time()-stime
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
mData['mouseX']=pynput.mouse.Controller().position[0]
mData['mouseY']=pynput.mouse.Controller().position[1]
mData['scrollX']=0
mData['scrollY']=0
mData['timeDiff']=0

mData=dict(sorted(mData.items()))
#print(mData)
#print(list(mData.values()))


iloop=1

keyPrsd=[]
def on_click(x, y, button, pressed):
    global ltime
    global stime
    global iloop
    #print (button)
    if pressed:
        if button==Button.left:
            mData['lClick']=1
        if button==Button.right:
            mData['rClick']=1
        if button==Button.middle:
            mData['mClick']=1
    if not pressed:
        if button==Button.left:
            mData['lClick']=0
        if button==Button.right:
            mData['rClick']=0
        if button==Button.middle:
            mData['mClick']=0
    #print(mData['lClick'],mData['mClick'],mData['rClick'])
    mData['mouseX']=pynput.mouse.Controller().position[0]
    mData['mouseY']=pynput.mouse.Controller().position[1]
    #mData['sTime']=time.time()-stime
    if ltime==0:
        mData['timeDiff']=0
    else:
        mData['timeDiff']=time.time()-ltime
    ltime=time.time()
    cData[0].append(list(mData.values()))



    if iloop==0:
        return False



def on_scroll(x, y, dx, dy):
    global stime
    global iloop
    global ltime
    #print('Scrolled {0}'.format((x, y)))
    #print(dx,dy)
    #mData['sTime']=time.time()-stime
    if ltime==0:
        mData['timeDiff']=0
    else:
        mData['timeDiff']=time.time()-ltime
    ltime=time.time()
    mData['scrollX']=dx
    mData['scrollY']=dy
    mData['mouseX']=x
    mData['mouseY']=y
    cData[0].append(list(mData.values()))
    mData['scrollX']=0
    mData['scrollY']=0

    if iloop==0:
        return False

def on_move(x,y):
    global iloop
    global ltime
    mData['mouseX']=x
    mData['mouseY']=y
    #mData['sTime']=time.time()-stime
    if ltime==0:
        mData['timeDiff']=0
    else:
        mData['timeDiff']=time.time()-ltime
    ltime=time.time()
    #print(x,y)
    cData[0].append(list(mData.values()))
    if iloop==0:
        return False




def recMousList():
    global mlistener
    # Collect events until released
    with mouse.Listener(
            on_click=on_click,
            on_scroll=on_scroll,
            on_move=on_move) as mlistener:
        mlistener.join()


def recMousPos():
    global iloop
    global stime
    global ltime
    while iloop:
        tempData=mData.copy()
        mData['mouseX']=pynput.mouse.Controller().position[0]
        mData['mouseY']=pynput.mouse.Controller().position[1]
        if tempData!=mData:
            #mData['sTime']=time.time()-stime
            if ltime==0:
                mData['timeDiff']=0
            else:
                mData['timeDiff']=time.time()-ltime
            ltime=time.time()            
            cData[0].append(list(mData.values()))
        
    return False


def on_press(key):
    global stime
    global ltime

    if isinstance(key,pynput.keyboard._win32.KeyCode) and key not in keyPrsd:
        #print("press:" ,key)
        mData['mouseX']=pynput.mouse.Controller().position[0]
        mData['mouseY']=pynput.mouse.Controller().position[1]
        #mData['sTime']=time.time()-stime
        if ltime==0:
            mData['timeDiff']=0
        else:
            mData['timeDiff']=time.time()-ltime
        ltime=time.time()
        keyPrsd.append(key)
        mData['charc']+=1
        cData[0].append(list(mData.values()))
        #print(mData['charc'])
    else:
        if key not in keyPrsd:
            #print("press:" ,key)
            mData['mouseX']=pynput.mouse.Controller().position[0]
            mData['mouseY']=pynput.mouse.Controller().position[1]
            #mData['sTime']=time.time()-stime
            if ltime==0:
                mData['timeDiff']=0
            else:
                mData['timeDiff']=time.time()-ltime
            ltime=time.time()
            keyPrsd.append(key)
            if key==Key.space:
                mData['space']=1
                #print(mData['space'])
                cData[0].append(list(mData.values()))
            if key==Key.backspace:
                mData['backSpace']=1
                #print(mData['backSpace'])
                cData[0].append(list(mData.values()))
            if key==Key.delete:
                mData['delete']=1
                #print(mData['delete'])
                cData[0].append(list(mData.values()))
            if key==Key.ctrl or key==Key.ctrl_l or key==Key.ctrl_r:
                mData['ctrl']=1
                #print(mData['ctrl'])
                cData[0].append(list(mData.values()))
            if key==Key.alt or key==Key.alt_l or key==Key.alt_r:
                mData['alt']=1
                #print(mData['alt'])
                cData[0].append(list(mData.values()))
            if key==Key.caps_lock:
                mData['capsLock']=1
                #print(mData['capsLock'])
                cData[0].append(list(mData.values()))
            if key==Key.shift or key==Key.shift_l or key==Key.shift_r:
                mData['shift']=1
                #print(mData['shift'])
                cData[0].append(list(mData.values()))
            if key==Key.tab:
                mData['tab']=1
                #print(mData['tab'])
                cData[0].append(list(mData.values()))
            if key==Key.num_lock:
                mData['numLock']=1
                #print(mData['numLock'])
                cData[0].append(list(mData.values()))
            if key==Key.enter:
                mData['enter']=1
                #print(mData['enter'])
                cData[0].append(list(mData.values()))
    
        

def on_release(key):
    global iloop
    global stime
    global ltime
    mData['mouseX']=pynput.mouse.Controller().position[0]
    mData['mouseY']=pynput.mouse.Controller().position[1]
    #mData['sTime']=time.time()-stime
    if ltime==0:
        mData['timeDiff']=0
    else:
        mData['timeDiff']=time.time()-ltime
    ltime=time.time()
    #print("release:",key)
    if isinstance(key,pynput.keyboard._win32.KeyCode):
        keyPrsd.remove(key)     
        mData['charc']-=1
        cData[0].append(list(mData.values()))
        #print(mData['charc'])
    else:
        keyPrsd.remove(key)
        if key==Key.space:
            mData['space']=0
            #print(mData['space'])
            cData[0].append(list(mData.values()))
        if key==Key.backspace:
            mData['backSpace']=0
            #print(mData['backSpace'])
            cData[0].append(list(mData.values()))
        if key==Key.delete:
            mData['delete']=0
            #print(mData['delete'])
            cData[0].append(list(mData.values()))
        if key==Key.ctrl or key==Key.ctrl_l or key==Key.ctrl_r:
            mData['ctrl']=0
            #print(mData['ctrl'])
            cData[0].append(list(mData.values()))
        if key==Key.alt or key==Key.alt_l or key==Key.alt_r:
            mData['alt']=0
            #print(mData['alt'])
            cData[0].append(list(mData.values()))
        if key==Key.caps_lock:
            mData['capsLock']=0
            #print(mData['capsLock'])
            cData[0].append(list(mData.values()))
        if key==Key.shift or key==Key.shift_l or key==Key.shift_r:
            mData['shift']=0
            #print(mData['shift'])
            cData[0].append(list(mData.values()))
        if key==Key.tab:
            mData['tab']=0
            #print(mData['tab'])
            cData[0].append(list(mData.values()))
        if key==Key.num_lock:
            mData['numLock']=0
            #print(mData['numLock'])
            cData.append(list(mData.values()))
        if key==Key.enter:
            mData['enter']=0
            #print(mData['enter'])
            cData[0].append(list(mData.values()))

    

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




def predictModel():
    global iloop
    #print("running")
    with tf.Session(graph=tf.Graph()) as sess:
        tf.saved_model.loader.load(sess,[tf.saved_model.tag_constants.SERVING],"model/")
        t_X=tf.get_default_graph().get_tensor_by_name('input:0')
        t_prediction=tf.get_default_graph().get_tensor_by_name('prediction:0')
        t_users=tf.get_default_graph().get_tensor_by_name('users:0')
        f_prediction=tf.nn.softmax(t_prediction)
        users_list=sess.run(t_users)
        for i in range(len(users_list)):
            users_list[i]=users_list[i].decode('utf-8')
        #print(tf.get_collection(tf.GraphKeys.key))
        #print(sess.graph.get_collection('variables'))       

        while iloop:
            if len(cData[0])>=250:
                tempcData=[]
                tempcData.append([])
                for i in range(len(range(250))):
                    tempcData[0].append(cData[0][i])
                print(users_list)
                print(sess.run(f_prediction,feed_dict={t_X:tempcData}))
                print()
                cData[0].pop(0)


t0=threading.Thread(target=recMousList,args=())
t1=threading.Thread(target=recKeybPress,args=())
t2=threading.Thread(target=predictModel,args=())
t0.start()
t1.start()
t2.start()


Thread.join(t0)
Thread.join(t1)
Thread.join(t2)




















    
    






    
    

    