import csv
import math
import numpy as np

# max = 12352

def getOneHot():
    with open("data/chess.csv") as f:
        reader = csv.reader(f, delimiter=",")
        d = list(reader)
        liste1=[]
        n=0
        nNeg=0
        for k in range(51):
            liste2=[]
            liste2.append(k+1)
            l = d[k][1].split(' ')
            for x in l:
                if x != 'NA' and x != '':
                    liste2.append(float(x)/12352)
                    if float(x)>0:
                        n += 1
                    else:
                        nNeg += 1
            liste1.append(liste2)

        cls1=0
        cls2=0
        cls3=0
        cls4=0
        cls5=0

        oneHotTotal=[]

        for l in liste1:
            oneHot=[]
            oneHot.append(l[0])
            for k in range(1,len(l)):
                oneHotBis=[0 for k in range(8)]
                if l[k] > 0 and l[k] < 0.002 :
                    cls1 += 1
                    oneHotBis[4]=1
                if l[k] > 0.002 and l[k] < 0.004:
                    cls2 += 1
                    oneHotBis[5]=1
                if l[k] > 0.004 and l[k] < 0.01:
                    cls3 += 1
                    oneHotBis[6]=1
                if l[k] > 0.01 and l[k] <= 1:
                    cls4 += 1
                    oneHotBis[7]=1
                if l[k] <= 0 and l[k] > -0.0008 :
                    oneHotBis[0]=1
                if l[k] < -0.0008 and l[k] > -0.004:
                    oneHotBis[1]=1
                if l[k] < -0.004 and l[k] > -0.0135:
                    oneHotBis[2]=1
                if l[k] < -0.0135 and l[k] >= -1:
                    oneHotBis[3]=1
                oneHot.append(oneHotBis)
            oneHotTotal.append(oneHot)
    return oneHotTotal

oneHotEncoded = getOneHot()
print(oneHotEncoded, end=" ", file=open("oneHotEncoded.txt", "a"))
