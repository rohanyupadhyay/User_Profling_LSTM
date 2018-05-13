import csv
import os
import ast
import re
import numpy as np


if not os.path.exists(os.path.dirname(r"final/")):
    os.makedirs(os.path.dirname(r"final/"))
if not os.path.exists(os.path.dirname(r"final/in/")):
    os.makedirs(os.path.dirname(r"final/in/"))
if not os.path.exists(os.path.dirname(r"final/out/")):
    os.makedirs(os.path.dirname(r"final/out/"))
if not os.path.exists(os.path.dirname(r"final/out/")):
    os.makedirs(os.path.dirname(r"final/out/"))
if not os.path.exists(os.path.dirname(r"final/test/")):
    os.makedirs(os.path.dirname(r"final/test/"))
users=[]

for filename in os.listdir('data/'):
    users.append(''.join(re.split("(_)", filename)[0:-4]))
users=sorted(np.unique(users))
#print(users)
#print(users.index('admin'))
filei=1
#pfi=open("final/in/pp_in_"+str(filei)+".txt","a")
#pfo=open("final/out/pp_out_"+str(filei)+".txt","a")
pfu=open("final/users.txt","a")
pfu.write(str(users))

timesteps=250
finalIn=[]
finalOut=[]


count=0

for filename in os.listdir('data/'):
    #print(filename)
    cOut=''.join(re.split("(_)", filename)[0:-4])
    #print(cOut)
    f=open("data/"+filename)
    lines = f.readlines()
    tempFile=[]
    for line in lines:
        dLine=ast.literal_eval(line)
        tempLine=[]
        for key,value in sorted(dLine.items()):
            tempLine.append(value)
        tempLine.pop(13)
        tempLine.pop(-1)
        tempFile.append(tempLine)
    for i in range(len(tempFile)-timesteps+1):
        outS=list(np.zeros(len(users)))
        #print(cOut)
        outS[users.index(cOut)]=1
        #print(outS)
        finalIn.append(tempFile[i:i+250])
        finalOut.append(outS)
        count+=1
        if count==1024:
            np.save("final/in/pp_in_"+str(filei),finalIn)
            np.save("final/out/pp_out_"+str(filei),finalOut)
            #pfi.write(str(finalIn))
            #pfo.write(str(finalOut))
            count=0
            finalIn=[]
            finalOut=[]
            #pfi.close()
            #pfo.close()
            filei+=1
            #pfi=open("final/in/pp_in_"+str(filei)+".txt","a")
            #pfo=open("final/out/pp_out_"+str(filei)+".txt","a")


#print(finalIn)
#print(finalOut)
if count!=0:
    np.save("final/in/pp_in_"+str(filei),finalIn)
    np.save("final/out/pp_out_"+str(filei),finalOut)
    #pfi.write(str(finalIn))
    #pfo.write(str(finalOut))






