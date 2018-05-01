import csv
import os
import ast



for filename in os.listdir('data/'):
    f=open("data/"+filename)
    lines = f.readlines()
    for line in lines:
        dLine=ast.literal_eval(line)
        for sorted(dLine.items())


