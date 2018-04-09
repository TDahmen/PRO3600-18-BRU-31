import numpy as np
import gamesConverter

valeursInterdites = [19, 22, 26, 27]

def createBoard():
    plateau = np.zeros([8,8])

    # On ajoute les pions (valeur : 1)

    for j in range (0,8):
        plateau[1][j] = -1
        plateau[6][j] = 1

    # On ajoute les tours (valeur : 4)

    plateau[7][0] = 5
    plateau[0][0] = -5
    plateau[0][7] = -5
    plateau[7][7] = 5

    # On ajoute les cavaliers (valeur : 2)

    plateau[7][1] = 3
    plateau[0][6] = -3
    plateau[0][1] = -3
    plateau[7][6] = 3

    # On ajoute les fous (valeur : 3)

    plateau[7][2] = 3.5
    plateau[0][2] = -3.5
    plateau[7][5] = 3.5
    plateau[0][5] = -3.5

    # On ajoute les reines (valeur : 5)

    plateau[7][3] = 9
    plateau[0][3] = -9

    # On ajoute les rois (valeur : 6)

    plateau[7][4] = 0
    plateau[0][4] = -0

    return plateau

def string_converter(a):
    if (a=='a'):
        res=0
    if (a=='b'):
        res=1
    if (a=='c'):
        res=2
    if (a=='d'):
        res=3
    if (a=='e'):
        res=4
    if (a=='f'):
        res=5
    if (a=='g'):
        res=6
    if (a=='h'):
        res=7
    return res

def converter(str):
    a=string_converter(str[0])
    b=8-int(str[1])
    c=string_converter(str[2])
    d=8-int(str[3])
    return (b,a,d,c)

def move(str,plateau):
    if (str=='e1g1'):
        plateau[7][6]=plateau[7][4]
        plateau[7][4]=0
        plateau[7][5]=plateau[7][7]
        plateau[7][7]=0
    if (str=='e1c1'):
        plateau[7][2]=plateau[7][4]
        plateau[7][4]=0
        plateau[7][3]=plateau[7][0]
        plateau[7][0]=0
    if (str=='e8g8'):
        plateau[0][6]=plateau[0][4]
        plateau[0][4]=0
        plateau[0][5]=plateau[0][7]
        plateau[0][7]=0
    if (str=='e8c8'):
        plateau[0][2]=plateau[0][4]
        plateau[0][4]=0
        plateau[0][3]=plateau[0][0]
        plateau[0][0]=0
    a,b,c,d=converter(str)
    plateau[c][d]=plateau[a][b]
    plateau[a][b] = 0

games = gamesConverter.getConvertedGames()
k=0
for game in games:
    if not(k in valeursInterdites):
        plateau = createBoard()
        for pos in game[1]:
            move(pos, plateau)
            for x in plateau:
                for y in x:
                    print(y, end=" ", file=open("convertedGames.txt", "a"))
            print("NOUVEAU COUP", file=open("convertedGames.txt", "a"))
        k += 1
        if k <= 50:
            # print("partie ", k)
            print("NOUVEAU JEU", file=open("convertedGames.txt", "a"))
        else:
            print("arret")
            break;
    else:
        k += 1
