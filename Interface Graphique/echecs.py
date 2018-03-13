#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:44:38 2018

@author: thomas
"""

import numpy as np
import math
from anytree import Node,RenderTree

def multiply(a,b):
    return a*b

#Variable pour savoir à qui est le tour

tour_blanc = True

# Création du plateau de jeu

plateau = np.zeros([12,12])

# Création des listes des pièces prises
# Ces pièces sont en valeur absolue

wonW = []
wonB = []

# On initialise les "bords" à -15

for k in range (0, 12):
    plateau[0][k] = -15
    plateau[1][k] = -15

for k in range (0, 12):
    plateau[10][k] = -15
    plateau[11][k] = -15

for k in range (0,12):
    plateau[k][0] = -15
    plateau[k][1] = -15

for k in range (0,12):
    plateau[k][10] = -15
    plateau[k][11] = -15

# On ajoute les pions (valeur : 1)

for j in range (2,10):
    plateau[3][j] = -1
    plateau[8][j] = 1

#Config spéciale pour le test de minimax

plateau[8][6]=1
plateau[3][5]=-1

# On ajoute les tours (valeur : 4)

plateau[9][2] = 4
plateau[2][2] = -4
plateau[2][9] = -4
plateau[9][9] = 4

# On ajoute les cavaliers (valeur : 2)

plateau[9][3] = 2
plateau[2][8] = -2
plateau[2][3] = -2
plateau[9][8] = 2

# On ajoute les fous (valeur : 3)

plateau[9][4] = 3
plateau[2][4] = -3
plateau[9][7] = 3
plateau[2][7] = -3

# On ajoute les reines (valeur : 5)

plateau[9][5] = 5
plateau[2][5] = -5

# On ajoute les rois (valeur : 6)

plateau[9][6] = 6
plateau[2][6] = -6

# Position de toutes les pièces blanches

position_W=[0 for k in range(16)]

for k in range(8):
    position_W[k]=(9,2+k)
    position_W[k+7]=(8,1+k)
position_W[15]=(8,9)

position_B=[0 for k in range(16)]

for k in range(8):
    position_B[k]=(2,2+k)
    position_B[k+7]=(3,1+k)
position_B[15]=(3,9)

#fonction copie pour les tableaux

def copy(tab):
    res=[]
    for k in range(len(tab)):
        res.append(tab[k])
    return res

#Création d'un dictionnaire pour les blancs : key = position sur le plateau, value = position dans la liste des positions

dico_position_W= dict()
dico_position_W[(9,2)]=0
dico_position_W[(9,3)]=1
dico_position_W[(9,4)]=2
dico_position_W[(9,5)]=3
dico_position_W[(9,6)]=4
dico_position_W[(9,7)]=5
dico_position_W[(9,8)]=6
dico_position_W[(9,9)]=7
dico_position_W[(8,2)]=8
dico_position_W[(8,3)]=9
dico_position_W[(8,4)]=10
dico_position_W[(8,5)]=11
dico_position_W[(8,6)]=12
dico_position_W[(8,7)]=13
dico_position_W[(8,8)]=14
dico_position_W[(8,9)]=15

#Même chose pour les noirs

dico_position_B=dict()
dico_position_B[(2,2)]=0
dico_position_B[(2,3)]=1
dico_position_B[(2,4)]=2
dico_position_B[(2,5)]=3
dico_position_B[(2,6)]=4
dico_position_B[(2,7)]=5
dico_position_B[(2,8)]=6
dico_position_B[(2,9)]=7
dico_position_B[(3,2)]=8
dico_position_B[(3,3)]=9
dico_position_B[(3,4)]=10
dico_position_B[(3,5)]=11
dico_position_B[(3,6)]=12
dico_position_B[(3,7)]=13
dico_position_B[(3,8)]=14
dico_position_B[(3,9)]=15

#bouger une pièce
#move_test -> mouvements ne respectant pas les règles mais utiles pour les test
#move_chess -> mouvements hypothétiques lors du calcul de chess_mate n'incrémentant pas les pièces prises
#move -> mouvements réel du joueur respectant les règles

def movetest(a,b,c,d):
    """
        Adds two numbers and returns the result.
 
        This add two real numbers and return a real result. You will want to
        use this function in any place you would usually use the ``+`` operator
        but requires a functional equivalent.
 
        :param a: The first number to add
        :param b: The second number to add
        :type a: int
        :type b: int
        :return: The result of the addition
        :rtype: int
    """
    if plateau[a][b] == 0:
        print("On ne peut pas jouer avec une case vide !")
    if plateau[c][d] != 0 :
        if plateau[a][b] < 0:
            wonB.append(abs(plateau[c][d]))
            del dico_position_W[(c,d)]
            pos=dico_position_B[(a,b)]
            position_B[pos]=(c,d)
            dico_position_B[(c,d)]=pos
            del dico_position_B[(a,b)]
        else :
            wonW.append(abs(plateau[c][d]))
            del dico_position_B[(c,d)]
            pos=dico_position_W[(a,b)]
            position_W[pos]=(c,d)
            dico_position_W[(c,d)]=pos
            del dico_position_W[(a,b)]
        plateau[c][d] = plateau[a][b]
        plateau[a][b] = 0

    if plateau[c][d] == 0 :
        plateau[c][d] = plateau[a][b]
        plateau[a][b] = 0
        if plateau[a][b] < 0:
            pos=dico_position_B[(a,b)]
            position_B[pos]=(c,d)
            dico_position_B[(c,d)]=pos
            del dico_position_B[(a,b)]
        else :
            pos=dico_position_W[(a,b)]
            position_W[pos]=(c,d)
            dico_position_W[(c,d)]=pos
            del dico_position_W[(a,b)]

def move(a,b,c,d):
    global tour_blanc
    l = valeurs_accessibles(a,b)
    if plateau[a][b] == 0:
        print("On ne peut pas jouer avec une case vide !")
    if plateau[c][d] != 0 and (c,d) in l :
        if plateau[a][b] < 0:
            wonB.append(abs(plateau[c][d]))
            del dico_position_W[(c,d)]
            pos=dico_position_B[(a,b)]
            position_B[pos]=(c,d)
            dico_position_B[(c,d)]=pos
            del dico_position_B[(a,b)]
        else :
            wonW.append(abs(plateau[c][d]))
            del dico_position_B[(c,d)]
            pos=dico_position_W[(a,b)]
            position_W[pos]=(c,d)
            dico_position_W[(c,d)]=pos
            del dico_position_W[(a,b)]
        plateau[c][d] = plateau[a][b]
        plateau[a][b] = 0

    if plateau[c][d] == 0 and (c,d) in l :
        plateau[c][d] = plateau[a][b]
        if plateau[a][b] < 0:
            pos=dico_position_B[(a,b)]
            position_B[pos]=(c,d)
            dico_position_B[(c,d)]=pos
            del dico_position_B[(a,b)]
        if plateau[a][b]>0:
            pos=dico_position_W[(a,b)]
            position_W[pos]=(c,d)
            dico_position_W[(c,d)]=pos
            del dico_position_W[(a,b)]
        plateau[a][b] = 0
    tour_blanc=not(tour_blanc)

def move_chess(a,b,c,d):
    l = valeurs_accessibles_test(a,b)
    #if plateau[a][b] == 0:
        #print("On ne peut pas jouer avec une case vide !")
    if plateau[c][d] != 0 and (c,d) in l :
        if plateau[a][b] < 0:
            del dico_position_W[(c,d)]
            pos=dico_position_B[(a,b)]
            position_B[pos]=(c,d)
            dico_position_B[(c,d)]=pos
            del dico_position_B[(a,b)]
        if plateau[a][b]>0 :
            del dico_position_B[(c,d)]
            pos=dico_position_W[(a,b)]
            position_W[pos]=(c,d)
            dico_position_W[(c,d)]=pos
            del dico_position_W[(a,b)]
        plateau[c][d] = plateau[a][b]
        plateau[a][b] = 0

    if plateau[c][d] == 0 and (c,d) in l :
        plateau[c][d] = plateau[a][b]
        if plateau[a][b] < 0:
            pos=dico_position_B[(a,b)]
            position_B[pos]=(c,d)
            dico_position_B[(c,d)]=pos
            del dico_position_B[(a,b)]
        if plateau[a][b]>0:
            pos=dico_position_W[(a,b)]
            position_W[pos]=(c,d)
            dico_position_W[(c,d)]=pos
            del dico_position_W[(a,b)]
        plateau[a][b] = 0
    #else:
    #return ("Cette case n'est pas accessible")

#Configuration jeu

#movetest(9,4,5,4)
#movetest(9,2,3,6)

def ensemble_valeurs_accessibles_W():
    res=[]
    for (k,l) in dico_position_W.keys():
        res+=valeurs_accessibles_test(k,l)
    return res

def ensemble_valeurs_accessibles_B():
    res=[]
    for (k,l) in dico_position_B.keys():
        res+=valeurs_accessibles_test(k,l)
    return res

def ensemble_move_possible_W():
    res=[]
    for (k,l) in dico_position_W.keys():
        for x,y in valeurs_accessibles_test(k,l):
            res+=[(k,l,x,y)]
    return res

def ensemble_move_possible_B():
    res=[]
    for (k,l) in dico_position_B.keys():
        for x,y in valeurs_accessibles_test(k,l):
            res+=[(k,l,x,y)]
    return res
#position du roi en 4ème position dans la liste des positions des pièces blanches
#retour de la fonction : mise en échec ou pas

def chess_W():
    return (position_W[4] in (ensemble_valeurs_accessibles_B()))

def chess_B():
    return (position_B[4] in (ensemble_valeurs_accessibles_W()))

def chess_Mate_B():
    chess_mate=True
    global plateau
    global position_B
    global dico_position_B
    global position_W
    global dico_position_W
    temp1 = np.copy(plateau)
    temp2=copy(position_B)
    temp3=dico_position_B.copy()
    temp4=copy(position_W)
    temp5=dico_position_W.copy()
    for i in dico_position_B.values():
        x,y=position_B[i]
        #print(position_B[i])
        poss=valeurs_accessibles_test(x,y)
        #print(poss)
        for (k,l) in poss:
            move_chess(x,y,k,l)
            #print(plateau)
            chess_mate=chess_B()
            plateau=np.copy(temp1)
            position_B=copy(temp2)
            dico_position_B=temp3.copy()
            position_W=copy(temp4)
            dico_position_W=temp5.copy()
            if not chess_mate:
                return False
    return chess_mate

def mouv_possible_chess_B():
    res=[]
    global plateau
    global position_B
    global dico_position_B
    global position_W
    global dico_position_W
    temp1 = np.copy(plateau)
    temp2=copy(position_B)
    temp3=dico_position_B.copy()
    temp4=copy(position_W)
    temp5=dico_position_W.copy()
    for i in dico_position_B.values():
        x,y=position_B[i]
        poss=valeurs_accessibles_test(x,y)
        for (k,l) in poss:
            chess_mate=True
            move_chess(x,y,k,l)
            chess_mate=chess_B()
            plateau=np.copy(temp1)
            position_B=copy(temp2)
            dico_position_B=temp3.copy()
            position_W=copy(temp4)
            dico_position_W=temp5.copy()
            if not chess_mate:
                res+=[(x,y,k,l)]
    return res


def chess_Mate_W():
    chess_mate=True
    global plateau
    global position_W
    global dico_position_W
    global position_B
    global dico_position_B
    temp1 = np.copy(plateau)
    temp2=copy(position_W)
    temp3=dico_position_W.copy()
    temp4=copy(position_B)
    temp5=dico_position_B.copy()
    for i in dico_position_W.values():
        x,y=position_W[i]
        #print(position_W[i])
        poss=valeurs_accessibles_test(x,y)
        #print(poss)
        for (k,l) in poss:
            move_chess(x,y,k,l)
            #print(plateau)
            chess_mate=chess_W()
            plateau=np.copy(temp1)
            position_W=copy(temp2)
            dico_position_W=temp3.copy()
            position_B=copy(temp4)
            dico_position_B=temp5.copy()
            if not chess_mate:
                return False
    return chess_mate

def mouv_possible_chess_W():
    res=[]
    global plateau
    global position_B
    global dico_position_B
    global position_W
    global dico_position_W
    temp1 = np.copy(plateau)
    temp2=copy(position_B)
    temp3=dico_position_B.copy()
    temp4=copy(position_W)
    temp5=dico_position_W.copy()
    for i in dico_position_W.values():
        x,y=position_W[i]
        poss=valeurs_accessibles_test(x,y)
        for (k,l) in poss:
            chess_mate=True
            move_chess(x,y,k,l)
            chess_mate=chess_W()
            plateau=np.copy(temp1)
            position_B=copy(temp2)
            dico_position_B=temp3.copy()
            position_W=copy(temp4)
            dico_position_W=temp5.copy()
            if not chess_mate:
                res+=[(x,y,k,l)]
    return res

def opponent(a,b):
    return (a*b<0)

def valide(a):
    return a!=-15



def valeurs_accessibles(x,y):
    res=[]
    piece_depart=plateau[x][y]
    #print(chess_W())
    if tour_blanc and chess_W():
        l = mouv_possible_chess_W()
        for (a, b, c, d) in l:
            if x == a and y == b:
                res.append((c,d))
        return res

    if not(tour_blanc) and chess_B():
        l = mouv_possible_chess_B()
        for (a, b, c, d) in l:
            if x == a and y == b:
                res.append((c,d))
        return res

    if (plateau[x][y]==1): #piece_depart=pion positif
        if (plateau[x-1][y]==0) and valide(plateau[x-1][y]): #mouvement basique
            res.append((x-1,y))
        if (x==8) and  (plateau[x-2][y]==0) and valide(plateau[x-2][y]):
            res.append((x-2,y))
        if opponent(plateau[x-1][y+1],piece_depart) and valide (plateau[x-1][y+1]):#manger à droite
            res.append((x-1,y+1))
        if opponent(plateau[x-1][y-1],piece_depart) and valide (plateau[x-1][y-1]): #manger à gauche
            res.append((x-1,y-1))

    if (plateau[x][y]==-1): #piece_depart=pion_negatif
        if (plateau[x+1][y]==0) and valide(plateau[x+1][y]): #mouvement basique
            res.append((x+1,y))
        if (x==3) and  (plateau[x+2][y]==0) and valide(plateau[x+2][y]):
            res.append((x+2,y))
        if opponent(plateau[x+1][y+1],piece_depart) and valide (plateau[x+1][y+1]):#manger à droite
            res.append((x+1,y+1))
        if opponent(plateau[x+1][y-1],piece_depart) and valide (plateau[x+1][y-1]): #manger à gauche
            res.append((x+1,y-1))

    if (abs(plateau[x][y])==2): #piece_depart=cavalier

        if (plateau[x-1][y+2]==0 or opponent(piece_depart,plateau[x-1][y+2])) and valide(plateau[x-1][y+2]): #mouvement basique
            res+=[(x-1,y+2)]
        if (plateau[x+1][y+2]==0 or opponent(piece_depart,plateau[x+1][y+2])) and valide(plateau[x+1][y+2]): #mouvement basique
            res+=[(x+1,y+2)]
        if (plateau[x-2][y+1]==0 or opponent(piece_depart,plateau[x-2][y+1])) and valide(plateau[x-2][y+1]): #mouvement basique
            res+=[(x-2,y+1)]
        if (plateau[x+2][y+1]==0 or opponent(piece_depart,plateau[x+2][y+1])) and valide(plateau[x+2][y+1]): #mouvement basique
            res+=[(x+2,y+1)]
        if (plateau[x-2][y-1]==0 or opponent(piece_depart,plateau[x-2][y-1])) and valide(plateau[x-2][y-1]): #mouvement basique
            res+=[(x-2,y-1)]
        if (plateau[x+2][y-1]==0 or opponent(piece_depart,plateau[x+2][y-1]))and valide(plateau[x+2][y-1]): #mouvement basique
            res+=[(x+2,y-1)]
        if (plateau[x-1][y-2]==0 or opponent(piece_depart,plateau[x-1][y-2]))and valide(plateau[x-1][y-2]): #mouvement basique
            res+=[(x-1,y-2)]
        if (plateau[x+1][y-2]==0 or opponent(piece_depart,plateau[x+1][y-2]))and valide(plateau[x+1][y-2]): #mouvement basique
            res+=[(x+1,y-2)]

    if (abs(plateau[x][y])==3): #piece_depart=fou
        k=1
        while (plateau[x+k,y+k]==0 and valide(plateau[x+k,y+k])):
            res+=[(x+k,y+k)]
            k+=1
        if opponent(piece_depart,plateau[x+k,y+k]) and valide(plateau[x+k,y+k]):
            res+=[(x+k,y+k)]
        i=1
        while (plateau[x-i,y+i]==0 and valide(plateau[x-i,y+i])):
            res+=[(x-i,y+i)]
            i+=1
        if opponent(piece_depart,plateau[x-i,y+i]) and valide(plateau[x-i,y+i]):
            res+=[(x-i,y+i)]
        k=1
        while (plateau[x+k,y-k]==0) and valide(plateau[x+k,y-k]):
            res+=[(x+k,y-k)]
            k+=1
        if opponent(piece_depart,plateau[x+k,y-k]) and valide(plateau[x+k,y-k]):
            res+=[(x+k,y-k)]
        i=1
        while (plateau[x-i,y-i]==0 and valide(plateau[x-i,y-i])):
            res+=[(x-i,y-i)]
            i+=1
        if opponent(piece_depart,plateau[x-i,y-i]) and valide(plateau[x-i,y-i]):
            res+=[(x-i,y-i)]

    if (abs(plateau[x][y])==4): #piece_depart=tour
        k=1
        while (plateau[x+k,y]==0) and valide(plateau[x+k,y]):
            res+=[(x+k,y)]
            k+=1
        if opponent(piece_depart,plateau[x+k,y]) and valide(plateau[x+k,y]):
            res+=[(x+k,y)]
        i=1
        while (plateau[x-i,y]==0 and valide(plateau[x-i,y])):
            res+=[(x-i,y)]
            i+=1
        if opponent(piece_depart,plateau[x-i,y]) and valide(plateau[x-i,y]):
            res+=[(x-i,y)]
        k=1
        while (plateau[x,y+k]==0 and valide(plateau[x,y+k])):
            res+=[(x,y+k)]
            k+=1
        if opponent(piece_depart,plateau[x,y+k]) and valide(plateau[x,y+k]):
            res+=[(x,y+k)]
        i=1
        while (plateau[x,y-i]==0 and valide(plateau[x,y-i])):
            res+=[(x,y-i)]
            i+=1
        if opponent(piece_depart,plateau[x,y-i])and valide(plateau[x,y-i]):
            res+=[(x,y-i)]

    if (abs(plateau[x][y])==5): #piece_depart=dame
        k=1
        while (plateau[x+k,y]==0 and valide(plateau[x+k,y])):
            res+=[(x+k,y)]
            k+=1
        if (opponent(piece_depart,plateau[x+k,y]) and valide(plateau[x+k,y])):
            res+=[(x+k,y)]
        i=1
        while (plateau[x-i,y]==0 and valide(plateau[x-i,y])):
            res+=[(x-i,y)]
            i+=1
        if opponent(piece_depart,plateau[x-i,y]) and valide(plateau[x-i,y]):
            res+=[(x-i,y)]
        k=1
        while (plateau[x,y+k]==0 and valide(plateau[x,y+k])):
            res+=[(x,y+k)]
            k+=1
        if opponent(piece_depart,plateau[x,y+k]) and valide(plateau[x,y+k]):
            res+=[(x,y+k)]
        i=1
        while (plateau[x,y-i]==0 and valide(plateau[x,y-i])):
            res+=[(x,y-i)]
            i+=1
        if opponent(piece_depart,plateau[x,y-i])and valide(plateau[x,y-i]):
            res+=[(x,y-i)]
        k=1
        while (plateau[x+k,y+k]==0) and valide(plateau[x+k,y+k]):
            res+=[(x+k,y+k)]
            k+=1
        if opponent(piece_depart,plateau[x+k,y+k]) and valide(plateau[x+k,y+k]):
            res+=[(x+k,y+k)]
        i=1
        while (plateau[x-i,y+i]==0) and valide(plateau[x-i,y+i]):
            res+=[(x-i,y+i)]
            i+=1
        if opponent(piece_depart,plateau[x-i,y+i]) and valide(plateau[x-i,y+i]):
            res+=[(x-i,y+i)]
        k=1
        while (plateau[x+k,y-k]==0 and valide(plateau[x+k,y-k])):
            res+=[(x+k,y-k)]
            k+=1
        if opponent(piece_depart,plateau[x+k,y-k]) and valide(plateau[x+k,y-k]):
            res+=[(x+k,y-k)]
        i=1
        while (plateau[x-i,y-i]==0 and valide(plateau[x-i,y-i])):
            res+=[(x-i,y-i)]
            i+=1
        if opponent(piece_depart,plateau[x-i,y-i]) and valide(plateau[x-i,y-i]):
            res+=[(x-i,y-i)]

    if (abs(plateau[x][y])==6): #piece_depart=roi

        if ((plateau[x][y+1]==0) or opponent(plateau[x][y+1],piece_depart)) and valide(plateau[x][y+1]): #mouvement basique
            res+=[(x,y+1)]

        if ((plateau[x][y-1]==0) or opponent(plateau[x][y-1],piece_depart)) and valide(plateau[x][y-1]): #mouvement basique
            res+=[(x,y-1)]

        if ((plateau[x+1][y]==0)or opponent(plateau[x+1][y],piece_depart)) and valide(plateau[x+1][y]): #mouvement basique
            res+=[(x+1,y)]

        if ((plateau[x-1][y]==0)or opponent(plateau[x-1][y],piece_depart)) and valide(plateau[x-1][y]):#mouvement basique
            res+=[(x-1,y)]

        if ((plateau[x+1][y+1]==0) or opponent(plateau[x+1][y+1],piece_depart)) and valide(plateau[x+1][y+1]): #mouvement basique
            res+=[(x+1,y+1)]

        if ((plateau[x+1][y-1]==0) or opponent(plateau[x+1][y-1],piece_depart)) and valide(plateau[x+1][y-1]): #mouvement basique
            res+=[(x+1,y-1)]

        if ((plateau[x-1][y+1]==0)or opponent(plateau[x-1][y+1],piece_depart)) and valide(plateau[x-1][y+1]): #mouvement basique
            res+=[(x-1,y+1)]

        if ((plateau[x-1][y-1]==0)or opponent(plateau[x-1][y-1],piece_depart)) and valide(plateau[x-1][y-1]):#mouvement basique
            res+=[(x-1,y-1)]

   # if (plateau[x][y]==0):
       # return("Case vide")
    return res

def valeurs_accessibles_test(x,y):
    res=[]
    piece_depart=plateau[x][y]

    if (plateau[x][y]==1): #piece_depart=pion positif
        if (plateau[x-1][y]==0) and valide(plateau[x-1][y]): #mouvement basique
            res.append((x-1,y))
        if (x==8) and  (plateau[x-2][y]==0) and valide(plateau[x-2][y]):
            res.append((x-2,y))
        if opponent(plateau[x-1][y+1],piece_depart) and valide (plateau[x-1][y+1]):#manger à droite
            res.append((x-1,y+1))
        if opponent(plateau[x-1][y-1],piece_depart) and valide (plateau[x-1][y-1]): #manger à gauche
            res.append((x-1,y-1))

    if (plateau[x][y]==-1): #piece_depart=pion_negatif
        if (plateau[x+1][y]==0) and valide(plateau[x+1][y]): #mouvement basique
            res.append((x+1,y))
        if (x==3) and  (plateau[x+2][y]==0) and valide(plateau[x+2][y]):
            res.append((x+2,y))
        if opponent(plateau[x+1][y+1],piece_depart) and valide (plateau[x+1][y+1]):#manger à droite
            res.append((x+1,y+1))
        if opponent(plateau[x+1][y-1],piece_depart) and valide (plateau[x+1][y-1]): #manger à gauche
            res.append((x+1,y-1))

    if (abs(plateau[x][y])==2): #piece_depart=cavalier

        if (plateau[x-1][y+2]==0 or opponent(piece_depart,plateau[x-1][y+2])) and valide(plateau[x-1][y+2]): #mouvement basique
            res+=[(x-1,y+2)]
        if (plateau[x+1][y+2]==0 or opponent(piece_depart,plateau[x+1][y+2])) and valide(plateau[x+1][y+2]): #mouvement basique
            res+=[(x+1,y+2)]
        if (plateau[x-2][y+1]==0 or opponent(piece_depart,plateau[x-2][y+1])) and valide(plateau[x-2][y+1]): #mouvement basique
            res+=[(x-2,y+1)]
        if (plateau[x+2][y+1]==0 or opponent(piece_depart,plateau[x+2][y+1])) and valide(plateau[x+2][y+1]): #mouvement basique
            res+=[(x+2,y+1)]
        if (plateau[x-2][y-1]==0 or opponent(piece_depart,plateau[x-2][y-1])) and valide(plateau[x-2][y-1]): #mouvement basique
            res+=[(x-2,y-1)]
        if (plateau[x+2][y-1]==0 or opponent(piece_depart,plateau[x+2][y-1]))and valide(plateau[x+2][y-1]): #mouvement basique
            res+=[(x+2,y-1)]
        if (plateau[x-1][y-2]==0 or opponent(piece_depart,plateau[x-1][y-2]))and valide(plateau[x-1][y-2]): #mouvement basique
            res+=[(x-1,y-2)]
        if (plateau[x+1][y-2]==0 or opponent(piece_depart,plateau[x+1][y-2]))and valide(plateau[x+1][y-2]): #mouvement basique
            res+=[(x+1,y-2)]

    if (abs(plateau[x][y])==3): #piece_depart=fou
        k=1
        while (plateau[x+k,y+k]==0 and valide(plateau[x+k,y+k])):
            res+=[(x+k,y+k)]
            k+=1
        if opponent(piece_depart,plateau[x+k,y+k]) and valide(plateau[x+k,y+k]):
            res+=[(x+k,y+k)]
        i=1
        while (plateau[x-i,y+i]==0 and valide(plateau[x-i,y+i])):
            res+=[(x-i,y+i)]
            i+=1
        if opponent(piece_depart,plateau[x-i,y+i]) and valide(plateau[x-i,y+i]):
            res+=[(x-i,y+i)]
        k=1
        while (plateau[x+k,y-k]==0) and valide(plateau[x+k,y-k]):
            res+=[(x+k,y-k)]
            k+=1
        if opponent(piece_depart,plateau[x+k,y-k]) and valide(plateau[x+k,y-k]):
            res+=[(x+k,y-k)]
        i=1
        while (plateau[x-i,y-i]==0 and valide(plateau[x-i,y-i])):
            res+=[(x-i,y-i)]
            i+=1
        if opponent(piece_depart,plateau[x-i,y-i]) and valide(plateau[x-i,y-i]):
            res+=[(x-i,y-i)]

    if (abs(plateau[x][y])==4): #piece_depart=tour
        k=1
        while (plateau[x+k,y]==0) and valide(plateau[x+k,y]):
            res+=[(x+k,y)]
            k+=1
        if opponent(piece_depart,plateau[x+k,y]) and valide(plateau[x+k,y]):
            res+=[(x+k,y)]
        i=1
        while (plateau[x-i,y]==0 and valide(plateau[x-i,y])):
            res+=[(x-i,y)]
            i+=1
        if opponent(piece_depart,plateau[x-i,y]) and valide(plateau[x-i,y]):
            res+=[(x-i,y)]
        k=1
        while (plateau[x,y+k]==0 and valide(plateau[x,y+k])):
            res+=[(x,y+k)]
            k+=1
        if opponent(piece_depart,plateau[x,y+k]) and valide(plateau[x,y+k]):
            res+=[(x,y+k)]
        i=1
        while (plateau[x,y-i]==0 and valide(plateau[x,y-i])):
            res+=[(x,y-i)]
            i+=1
        if opponent(piece_depart,plateau[x,y-i])and valide(plateau[x,y-i]):
            res+=[(x,y-i)]

    if (abs(plateau[x][y])==5): #piece_depart=dame
        k=1
        while (plateau[x+k,y]==0 and valide(plateau[x+k,y])):
            res+=[(x+k,y)]
            k+=1
        if (opponent(piece_depart,plateau[x+k,y]) and valide(plateau[x+k,y])):
            res+=[(x+k,y)]
        i=1
        while (plateau[x-i,y]==0 and valide(plateau[x-i,y])):
            res+=[(x-i,y)]
            i+=1
        if opponent(piece_depart,plateau[x-i,y]) and valide(plateau[x-i,y]):
            res+=[(x-i,y)]
        k=1
        while (plateau[x,y+k]==0 and valide(plateau[x,y+k])):
            res+=[(x,y+k)]
            k+=1
        if opponent(piece_depart,plateau[x,y+k]) and valide(plateau[x,y+k]):
            res+=[(x,y+k)]
        i=1
        while (plateau[x,y-i]==0 and valide(plateau[x,y-i])):
            res+=[(x,y-i)]
            i+=1
        if opponent(piece_depart,plateau[x,y-i])and valide(plateau[x,y-i]):
            res+=[(x,y-i)]
        k=1
        while (plateau[x+k,y+k]==0) and valide(plateau[x+k,y+k]):
            res+=[(x+k,y+k)]
            k+=1
        if opponent(piece_depart,plateau[x+k,y+k]) and valide(plateau[x+k,y+k]):
            res+=[(x+k,y+k)]
        i=1
        while (plateau[x-i,y+i]==0) and valide(plateau[x-i,y+i]):
            res+=[(x-i,y+i)]
            i+=1
        if opponent(piece_depart,plateau[x-i,y+i]) and valide(plateau[x-i,y+i]):
            res+=[(x-i,y+i)]
        k=1
        while (plateau[x+k,y-k]==0 and valide(plateau[x+k,y-k])):
            res+=[(x+k,y-k)]
            k+=1
        if opponent(piece_depart,plateau[x+k,y-k]) and valide(plateau[x+k,y-k]):
            res+=[(x+k,y-k)]
        i=1
        while (plateau[x-i,y-i]==0 and valide(plateau[x-i,y-i])):
            res+=[(x-i,y-i)]
            i+=1
        if opponent(piece_depart,plateau[x-i,y-i]) and valide(plateau[x-i,y-i]):
            res+=[(x-i,y-i)]

    if (abs(plateau[x][y])==6): #piece_depart=roi

        if ((plateau[x][y+1]==0) or opponent(plateau[x][y+1],piece_depart)) and valide(plateau[x][y+1]): #mouvement basique
            res+=[(x,y+1)]

        if ((plateau[x][y-1]==0) or opponent(plateau[x][y-1],piece_depart)) and valide(plateau[x][y-1]): #mouvement basique
            res+=[(x,y-1)]

        if ((plateau[x+1][y]==0)or opponent(plateau[x+1][y],piece_depart)) and valide(plateau[x+1][y]): #mouvement basique
            res+=[(x+1,y)]

        if ((plateau[x-1][y]==0)or opponent(plateau[x-1][y],piece_depart)) and valide(plateau[x-1][y]):#mouvement basique
            res+=[(x-1,y)]

        if ((plateau[x+1][y+1]==0) or opponent(plateau[x+1][y+1],piece_depart)) and valide(plateau[x+1][y+1]): #mouvement basique
            res+=[(x+1,y+1)]

        if ((plateau[x+1][y-1]==0) or opponent(plateau[x+1][y-1],piece_depart)) and valide(plateau[x+1][y-1]): #mouvement basique
            res+=[(x+1,y-1)]

        if ((plateau[x-1][y+1]==0)or opponent(plateau[x-1][y+1],piece_depart)) and valide(plateau[x-1][y+1]): #mouvement basique
            res+=[(x-1,y+1)]

        if ((plateau[x-1][y-1]==0)or opponent(plateau[x-1][y-1],piece_depart)) and valide(plateau[x-1][y-1]):#mouvement basique
            res+=[(x-1,y-1)]

   # if (plateau[x][y]==0):
       # return("Case vide")
    return res

#description fonctions d'évaluation

def eval_denombrement():
    res=0
    for k in range(len(wonW)):
        if (wonW[k]==1):
            res+=1
        if (wonW[k]==2) or (wonW[k]==3):
            res+=3
        if (wonW[k]==4):
            res+=5
        if (wonW[k]==5):
            res+=9
        if (wonW[k]==6):
            res+=0 #à vérifier, les sources ne sont pas concordantes (0 ou +infini)

    for k in range(len(wonB)):
        if (wonB[k]==1):
            res+=-1
        if (wonB[k]==2) or (wonB[k]==3):
            res+=-3
        if (wonB[k]==4):
            res+=-5
        if (wonB[k]==5):
            res+=-9
        if (wonB[k]==6):
            res+=0 #à vérifier, les sources ne sont pas concordantes (0 ou +infini)
    return res



#Création de l'arbre de jeu

root_tree_W=Node((0,0,0,0,0))

def create_tree_W_viz():
   # t=0
    global plateau
    global position_B
    global dico_position_B
    global position_W
    global dico_position_W
    global wonW
    global wonB
    temp1=np.copy(plateau)
    temp2=copy(position_W)
    temp3=dico_position_W.copy()
    temp4=copy(position_B)
    temp5=dico_position_B.copy()
    temp6=copy(wonW)
    temp7=copy(wonB)
    for a,b,c,d in (ensemble_move_possible_W()):
        move(a,b,c,d)
        node_i=Node((a,b,c,d,0),parent=root_tree_W)
        temp1_2=np.copy(plateau)
        temp2_2=copy(position_W)
        temp3_2=dico_position_W.copy()
        temp4_2=copy(position_B)
        temp5_2=dico_position_B.copy()
        temp6_2=copy(wonW)
        temp7_2=copy(wonB)
        for i,j,k,l in (ensemble_move_possible_B()):
            move(i,j,k,l)
            node_i_k=Node((i,j,k,l,0),parent=node_i)
            temp1_3=np.copy(plateau)
            temp2_3=copy(position_W)
            temp3_3=dico_position_W.copy()
            temp4_3=copy(position_B)
            temp5_3=dico_position_B.copy()
            temp6_3=copy(wonW)
            temp7_3=copy(wonB)
            for m,n,o,p in (ensemble_move_possible_W()):
                move(m,n,o,p)
                val=eval_denombrement()
                node_i_k_l=Node((m,n,o,p,val),parent=node_i_k)
                plateau=np.copy(temp1_3)
                position_W=copy(temp2_3)
                dico_position_W=temp3_3.copy()
                position_B=copy(temp4_3)
                dico_position_B=temp5_3.copy()
                wonW=copy(temp6_3)
                wonB=copy(temp7_3)
                #t+=1
            plateau=np.copy(temp1_2)
            position_W=copy(temp2_2)
            dico_position_W=temp3_2.copy()
            position_B=copy(temp4_2)
            dico_position_B=temp5_2.copy()
            wonW=copy(temp6_2)
            wonB=copy(temp7_2)
        plateau=np.copy(temp1)
        position_W=copy(temp2)
        dico_position_W=temp3.copy()
        position_B=copy(temp4)
        dico_position_B=temp5.copy()
        wonW=copy(temp6)
        wonB=copy(temp7)
        #print(t)

def create_tree_W(): #arbre non-lisible mais seulement utile pour alpha_beta et min-max
   # t=0
    global plateau
    global position_B
    global dico_position_B
    global position_W
    global dico_position_W
    global wonW
    global wonB
    temp1=np.copy(plateau)
    temp2=copy(position_W)
    temp3=dico_position_W.copy()
    temp4=copy(position_B)
    temp5=dico_position_B.copy()
    temp6=copy(wonW)
    temp7=copy(wonB)
    for a,b,c,d in (ensemble_move_possible_W()):
        move(a,b,c,d)
        node_i=Node((a,b,c,d,0),parent=root_tree_W)
        temp1_2=np.copy(plateau)
        temp2_2=copy(position_W)
        temp3_2=dico_position_W.copy()
        temp4_2=copy(position_B)
        temp5_2=dico_position_B.copy()
        temp6_2=copy(wonW)
        temp7_2=copy(wonB)
        for i,j,k,l in (ensemble_move_possible_B()):
            move(i,j,k,l)
            node_i_k=Node((a,b,c,d,0),parent=node_i)
            temp1_3=np.copy(plateau)
            temp2_3=copy(position_W)
            temp3_3=dico_position_W.copy()
            temp4_3=copy(position_B)
            temp5_3=dico_position_B.copy()
            temp6_3=copy(wonW)
            temp7_3=copy(wonB)
            for m,n,o,p in (ensemble_move_possible_W()):
                move(m,n,o,p)
                val=eval_denombrement()
                node_i_k_l=Node((a,b,c,d,val),parent=node_i_k)
                plateau=np.copy(temp1_3)
                position_W=copy(temp2_3)
                dico_position_W=temp3_3.copy()
                position_B=copy(temp4_3)
                dico_position_B=temp5_3.copy()
                wonW=copy(temp6_3)
                wonB=copy(temp7_3)
                #t+=1
            plateau=np.copy(temp1_2)
            position_W=copy(temp2_2)
            dico_position_W=temp3_2.copy()
            position_B=copy(temp4_2)
            dico_position_B=temp5_2.copy()
            wonW=copy(temp6_2)
            wonB=copy(temp7_2)
        plateau=np.copy(temp1)
        position_W=copy(temp2)
        dico_position_W=temp3.copy()
        position_B=copy(temp4)
        dico_position_B=temp5.copy()
        wonW=copy(temp6)
        wonB=copy(temp7)
        #print(t)

root_tree_B=Node((0,0,0,0,0))

def create_tree_B(): #arbre non-lisible mais seulement utile pour alpha_beta et min-max
   # t=0
    global plateau
    global position_B
    global dico_position_B
    global position_W
    global dico_position_W
    global wonW
    global wonB
    temp1=np.copy(plateau)
    temp2=copy(position_W)
    temp3=dico_position_W.copy()
    temp4=copy(position_B)
    temp5=dico_position_B.copy()
    temp6=copy(wonW)
    temp7=copy(wonB)
    #print(ensemble_move_possible_B())
    for a,b,c,d in (ensemble_move_possible_B()):
        #print(a,b,c,d)
        move(a,b,c,d)
        node_i=Node((a,b,c,d,0),parent=root_tree_B)
        temp1_2=np.copy(plateau)
        temp2_2=copy(position_W)
        temp3_2=dico_position_W.copy()
        temp4_2=copy(position_B)
        temp5_2=dico_position_B.copy()
        temp6_2=copy(wonW)
        temp7_2=copy(wonB)
        #print(ensemble_move_possible_W())
        for i,j,k,l in (ensemble_move_possible_W()):
            move(i,j,k,l)
            node_i_k=Node((a,b,c,d,0),parent=node_i)
            temp1_3=np.copy(plateau)
            temp2_3=copy(position_W)
            temp3_3=dico_position_W.copy()
            temp4_3=copy(position_B)
            temp5_3=dico_position_B.copy()
            temp6_3=copy(wonW)
            temp7_3=copy(wonB)
           # print(i,j,k,l)
           # print(ensemble_move_possible_B())
            for m,n,o,p in (ensemble_move_possible_B()):
               # print(m,n,o,p)
                move(m,n,o,p)
                val=eval_denombrement()
                node_i_k_l=Node((a,b,c,d,val),parent=node_i_k)
                plateau=np.copy(temp1_3)
                position_W=copy(temp2_3)
                dico_position_W=temp3_3.copy()
                position_B=copy(temp4_3)
                dico_position_B=temp5_3.copy()
                wonW=copy(temp6_3)
                wonB=copy(temp7_3)
                #t+=1
            plateau=np.copy(temp1_2)
            position_W=copy(temp2_2)
            dico_position_W=temp3_2.copy()
            position_B=copy(temp4_2)
            dico_position_B=temp5_2.copy()
            wonW=copy(temp6_2)
            wonB=copy(temp7_2)
        plateau=np.copy(temp1)
        position_W=copy(temp2)
        dico_position_W=temp3.copy()
        position_B=copy(temp4)
        dico_position_B=temp5.copy()
        wonW=copy(temp6)
        wonB=copy(temp7)
        #print(t)

#Affichage de l'arbre



#Algorithme minimax

def is_max_W(arb):
    if arb.is_root:
        return True
    else:
        n=(arb.ancestors[0]).height
        return ((n-arb.height)%2==0)

def is_min_B(arb):
     if arb.is_root:
        return True
     else:
        n=(arb.ancestors[0]).height
        return ((n-arb.height)%2==0)


#Minimax Classique

#def minimax(arb,profondeur):
#    if arb.is_leaf:
#        valeur_de_la_position=arb.name #à changer par la valeur de la fonction d'évaluation
#        return valeur_de_la_position
#    for node in arb.children:
#        valeur_du_fils_courant=minimax(node,profondeur+1)
#        if is_max(arb): #c'est un noeud max
#            if (valeur_du_fils_courant> arb.name) or (node==arb.children[0]):
#                arb.name=valeur_du_fils_courant
#        else: #c'est un noeud min
#            if (valeur_du_fils_courant < arb.name) or (node==arb.children[0]):
#                arb.name=valeur_du_fils_courant
#    valeur_de_la_position=arb.name
#    return valeur_de_la_position

#Pour les blancs

def minimax_W(arb,profondeur): #Minimax pour les arbres à quintuplet-> 4 premières valeurs pour le move
                                                                 #-> 5ème : valeur de la fonction d'éval
    if arb.is_leaf:
        valeur_de_la_position=arb.name #à changer par la valeur de la fonction d'évaluation
        return valeur_de_la_position
    for node in arb.children:
        valeur_du_fils_courant=minimax_W(node,profondeur+1)
        if is_max_W(arb): #c'est un noeud max
            if (valeur_du_fils_courant[4]> arb.name[4]) or (node==arb.children[0]):
                arb.name=valeur_du_fils_courant
        else: #c'est un noeud min
            if (valeur_du_fils_courant[4] < arb.name[4]) or (node==arb.children[0]):
                arb.name=valeur_du_fils_courant
    valeur_de_la_position=arb.name
    return valeur_de_la_position

def get_minimax_W():
    return minimax_W(root_tree_W,0)[0:4]

#Pour les noirs

def minimax_B(arb,profondeur): #Minimax pour les arbres à quintuplet-> 4 premières valeurs pour le move
                                                                 #-> 5ème : valeur de la fonction d'éval
    if arb.is_leaf:
        valeur_de_la_position=arb.name #à changer par la valeur de la fonction d'évaluation
        return valeur_de_la_position
    for node in arb.children:
        valeur_du_fils_courant=minimax_B(node,profondeur+1)
        if not(is_min_B(arb)): #c'est un noeud max
            if (valeur_du_fils_courant[4]> arb.name[4]) or (node==arb.children[0]):
                arb.name=valeur_du_fils_courant
        else: #c'est un noeud min
            if (valeur_du_fils_courant[4] < arb.name[4]) or (node==arb.children[0]):
                arb.name=valeur_du_fils_courant
    valeur_de_la_position=arb.name
    return valeur_de_la_position

def get_minimax_B():
    return minimax_B(root_tree_B,0)[0:4]

#Élagage alpha_beta

#Pour les blancs
def alpha_beta_W(arb,profondeur,alpha,beta):
    global m2
    global n2
    global o2
    global p2
    global mp2
    global np2
    global op2
    global qp2
    if arb.is_leaf:
        valeur_de_la_position=arb.name
        return valeur_de_la_position
    else:
        if is_max_W(arb):
            for node in arb.children:
                if alpha<beta:
                    valeur_du_fils_courant=alpha_beta_W(node,profondeur+1,alpha,beta)
                    if alpha < valeur_du_fils_courant[4]:
                        alpha=valeur_du_fils_courant[4]
                        m2,n2,o2,p2 =valeur_du_fils_courant[0:4]
            valeur_de_la_position=(m2,n2,o2,p2,alpha)
        else:
            for node in arb.children:
                if alpha<beta:
                    valeur_du_fils_courant=alpha_beta_W(node,profondeur+1,alpha,beta)
                    if beta > valeur_du_fils_courant[4]:
                        beta=valeur_du_fils_courant[4]
                        mp2,np2,op2,qp2 =valeur_du_fils_courant[0:4]
            valeur_de_la_position=(mp2,np2,op2,qp2,beta)
    return valeur_de_la_position

def get_alpha_beta_W():
    return alpha_beta_W(root_tree_W,0,-math.inf,math.inf)[0:4]

#Pour les noirs

def alpha_beta_B(arb,profondeur,alpha,beta):
    global m1
    global n1
    global o1
    global p1
    global mp1
    global np1
    global op1
    global qp1
    if arb.is_leaf:
        valeur_de_la_position=arb.name
        return valeur_de_la_position
    else:
        if not(is_min_B(arb)):
            for node in arb.children:
                if alpha<beta:
                    valeur_du_fils_courant=alpha_beta_B(node,profondeur+1,alpha,beta)
                    if alpha < valeur_du_fils_courant[4]:
                        alpha=valeur_du_fils_courant[4]
                        m1,n1,o1,p1 =valeur_du_fils_courant[0:4]
            valeur_de_la_position=(m1,n1,o1,p1,alpha)
        else:
            for node in arb.children:
                if alpha<beta:
                    valeur_du_fils_courant=alpha_beta_B(node,profondeur+1,alpha,beta)
                    if beta > valeur_du_fils_courant[4]:
                        beta=valeur_du_fils_courant[4]
                        mp1,np1,op1,qp1 =valeur_du_fils_courant[0:4]
            valeur_de_la_position=(mp1,np1,op1,qp1,beta)
    return valeur_de_la_position

def get_alpha_beta_B():
    return alpha_beta_B(root_tree_B,0,-math.inf,math.inf)[0:4]

#Configuration jeu

def tour_Blanc(x):
    return x

root_tree_B=Node((0,0,0,0,0))

def move_IA_black():
    # del root_tree_B
    root_tree_B=Node((0,0,0,0,0))
    create_tree_B()
    return get_alpha_beta_B()

#print(valeurs_accessibles(2,5))
#print(valeurs_accessibles(3,3))
#k=0
#while not(chess_Mate_W() or chess_Mate_B()) and k<15:
#    del root_tree_W
#    root_tree_W=Node((0,0,0,0,0))
#    create_tree_W()
#    a,b,c,d=get_alpha_beta_W()
#    print((a,b,c,d))
#    move(a,b,c,d)
#    del root_tree_B
#    root_tree_B=Node((0,0,0,0,0))
#    create_tree_B()
#    a,b,c,d=get_alpha_beta_B()
#    print((a,b,c,d))
#    move(a,b,c,d)
#    k+=1


#for pre, fill, node in RenderTree(root_tree_B):
#    print("%s%s" % (pre, node.name))

