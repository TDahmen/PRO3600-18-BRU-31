import numpy as np
import itertools

with open("convertedGames.txt") as f:
    content = f.read().splitlines()
    listeJeux = [list(x[1]) for x in itertools.groupby(content, lambda x: x=='NOUVEAU JEU') if not x[0]]
    listeJeuxBis = []
    k = 0
    for jeu in listeJeux:
        k = k+1
        l = []
        for coup in jeu:
            u = coup.split(' ')
            l.append(u)
        for plateau in l:
            plateauBis = []
            for value in plateau:
                if not('NOUVEAU' in value) and not('COUP' in value):
                    plateauBis.append(float(value))
            listeJeuxBis.append(plateauBis)
    tableauNumpy = np.asarray(listeJeuxBis, np.float32)
    np.save('gamesData.npy', tableauNumpy)
    print(listeJeuxBis, end=" ", file=open("gamesData.txt", "a"))
