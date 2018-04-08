def getConvertedGames():
    listeTotale=[]
    with open("data/data_uci.pgn") as f:
        nGame=0
        for line in f:
            if not('[' in line):
                l = line.split(' ')
                if not('\n' in l):
                    nGame += 1
                    bonneListe=[]
                    bonneListe.append(nGame)
                    x = len(l)-1
                    new = ''.join( c for c in l[x] if  c not in '\n' )
                    l[x] = new
                    newL=[]
                    for k in range (0,len(l)-1):
                        newL.append(l[k])
                    bonneListe.append(newL)
                    listeTotale.append(bonneListe)
    return listeTotale
