import csv
import os
import ast
import re
import numpy as np


if not os.path.exists(os.path.dirname(r"final/")):
    os.makedirs(os.path.dirname(r"final/"))
users=[]

for filename in os.listdir('data/'):
    users.append(''.join(re.split("(_)", filename)[0:-4]))
users=sorted(np.unique(users))
#print(users)
#print(users.index('admin'))

pfi=open("final/pp_in.txt","a")
pfo=open("final/pp_out.txt","a")
pfu=open("final/users.txt","a")
pfu.write(str(users))

timesteps=250
finalData=[]
finalOut=[]

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
        finalData.append(tempFile[i:i+250])
        finalOut.append(outS)

#print(finalData)
#print(finalOut)
pfi.write(str(finalData))
pfo.write(str(finalOut))






