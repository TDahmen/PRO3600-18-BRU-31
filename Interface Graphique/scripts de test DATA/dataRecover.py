import numpy as np
import itertools
import oneHotEncoder as one


with open("convertedGames.txt") as f:
    content = f.read().splitlines()
    listeJeux = [list(x[1]) for x in itertools.groupby(content, lambda x: x=='NOUVEAU JEU') if not x[0]]
    listeJeuxBis = []
    for jeu in listeJeux:
        l = []
        for coup in jeu:
            u = coup.split(' ')
            l.append(u)
        lBis = []
        for plateau in l:
            plateauBis = []
            for value in plateau:
                if not('NOUVEAU' in value) and not('COUP' in value):
                    plateauBis.append(value)
            lBis.append(plateauBis)
        listeJeuxBis.append(lBis)
    # print(listeJeuxBis, file=open("recoveredData.txt", "a"))

    listeOneHot = one.getOneHot()
    k = 0
    res = True
    for partie in listeJeuxBis:
        res=(len(listeOneHot[k])-1==len(partie))
        if not res:
            print(k)
            print(res)
        k += 1
