#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:44:38 2018

"""

import numpy as np
import random
from anytree import Node,RenderTree
import time

#Variable pour savoir à qui est le tour

tour_blanc = True

# Création du plateau de jeu

plateau = np.zeros([12,12])

position_W=[0 for k in range(16)]
position_B=[0 for k in range(16)]
dico_position_W= dict()
dico_position_B= dict()


# Création des listes des pièces prises
# Ces pièces sont en valeur absolue

wonW = []
wonB = []


def initialize():
    """
        Initializes board configuration and all the different parameters (dictionnary,position lists)

        :rtype: None
    """
    global plateau
    # On initialise les "bords" à -15
    plateau = np.zeros([12,12])
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

    for k in range(8):
        position_W[k]=(9,2+k)
        position_W[k+7]=(8,1+k)
    position_W[15]=(8,9)


    for k in range(8):
        position_B[k]=(2,2+k)
        position_B[k+7]=(3,1+k)
    position_B[15]=(3,9)

    #Création d'un dictionnaire pour les blancs : key = position sur le plateau, value = position dans la liste des positions


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


#fonction copie pour les tableaux

def copy(tab):
    res=[]
    for k in range(len(tab)):
        res.append(tab[k])
    return res



#réinitialise tous les bons paramètres en prenant en compte un nouveau plateau

def scan(new_plateau):
    """
        Reinitializes the different board parameters (dictionnaries and position lists) given a board configuration

        :param new_plateau: new board configuration
        :type new_plateau: numpy array
        :rtype: None
    """
    global plateau
    global position_B
    global position_W
    global dico_position_W
    global dico_position_B
    new_dict_W=dict()
    new_dict_B=dict()
    nbCav_W=0
    nbTours_W=0
    nbFous_W=0
    nbPion_W=0
    nbTours_B=0
    nbCav_B=0
    nbFous_B=0
    nbPion_B=0
    for k in range(2,10):
        for l in range(2,10):
            if new_plateau[k][l] == 5:
                new_dict_W[(k,l)] = 3
            if new_plateau[k][l] == 6:
                new_dict_W[(k,l)] = 4

            if new_plateau[k][l] == 4:
                if nbTours_W == 0 :
                    new_dict_W[(k,l)] = 0
                    nbTours_W+=1
                else:
                    new_dict_W[(k,l)] = 7

            if new_plateau[k][l] == 2:
                if nbCav_W == 0 :
                    new_dict_W[(k,l)] = 1
                    nbCav_W+=1
                else:
                    new_dict_W[(k,l)] = 6

            if new_plateau[k][l] == 3:
                if nbFous_W == 0 :
                    new_dict_W[(k,l)] = 2
                    nbFous_W+=1
                else:
                    new_dict_W[(k,l)] = 5

            if new_plateau[k][l] == 1:
                new_dict_W[(k,l)]=8 + nbPion_W
                nbPion_W+=1

            if new_plateau[k][l] == -5:
                new_dict_B[(k,l)] = 3

            if new_plateau[k][l] == -6:
                new_dict_B[(k,l)] = 4


            if new_plateau[k][l] == -4:
                if nbTours_B == 0 :
                    new_dict_B[(k,l)] = 0
                    nbTours_B+=1
                else:
                    new_dict_B[(k,l)] = 7

            if new_plateau[k][l] == -2:
                if nbCav_B == 0 :
                    new_dict_B[(k,l)] = 1
                    nbCav_B+=1
                else:
                    new_dict_B[(k,l)] = 6

            if new_plateau[k][l] == -3:
                if nbFous_B == 0 :
                    new_dict_B[(k,l)] = 2
                    nbFous_B+=1
                else:
                    new_dict_B[(k,l)] = 5

            if new_plateau[k][l] == -1:
                new_dict_B[(k,l)]=8+nbPion_B
                nbPion_B+=1

    dico_position_W=new_dict_W
    dico_position_B=new_dict_B
    for cle,val in dico_position_W.items():
        position_W[val]=cle
    for cle,val in dico_position_B.items():
        position_B[val]=cle
    plateau=np.copy(new_plateau)

def promotion(x,y):
    if (x==2) and (plateau[x][y]==1):
        plateau[x][y]=5
    if (x==9) and (plateau[x][y]==-1):
        plateau[x][y]=-5

#bouger une pièce
#move_test -> mouvements ne respectant pas les règles mais utiles pour les test
#move_chess -> mouvements hypothétiques lors du calcul de chess_mate n'incrémentant pas les pièces prises
#move -> mouvements réel du joueur respectant les règles

def move(a,b,c,d):
    """
        * Moves a piece located on (a,b) to (c,d) if the movement is allowed by changing the values of plateau.
        * Updates dico_position_W, dico_position_B, position_W, position_B,wonW,wonB
        * Reverses the boolean value of tour_blanc to allow next player to play

        :param a: X axis of the piece we want to move
        :param b: Y axis of the piece we want to move
        :param c: X axis of the position we want to move the piece on
        :param d: Y axis of the position we want to move the piece on
        :type a: int
        :type b: int
        :type c: int
        :type d: int
        :return: None
        :rtype: None
    """
    global tour_blanc

    l = valeurs_accessibles(a,b)

    if (a,b)==(9,6) and (c,d)==(9,4) and plateau[a][b]==6 and (c,d) in l:
        plateau[9][4] = 6
        plateau[9][5] = 4
        plateau[9][6] = 0
        plateau[9][2] = 0
        position_W[0]=(9,5)
        position_W[4]=(9,4)
        del dico_position_W[(9,6)]
        del dico_position_W[(9,2)]
        dico_position_W[(9,5)]=0
        dico_position_W[(9,4)]=4

    elif (a,b)==(9,6) and (c,d)==(9,8) and plateau[a][b]==6 and (c,d) in l:
        plateau[9][8] = 6
        plateau[9][7] = 4
        plateau[9][6] = 0
        plateau[9][9] = 0
        position_W[0]=(9,7)
        position_W[4]=(9,8)
        del dico_position_W[(9,6)]
        del dico_position_W[(9,9)]
        dico_position_W[(9,7)]=0
        dico_position_W[(9,8)]=4

    elif (a,b)==(2,6) and (2,d)==(2,4) and plateau[a][b]==-6 and (c,d) in l:
        plateau[2][4] = -6
        plateau[2][5] = -4
        plateau[2][6] = 0
        plateau[2][2] = 0
        position_B[0]=(2,5)
        position_B[4]=(2,4)
        del dico_position_B[(2,6)]
        del dico_position_B[(2,2)]
        dico_position_B[(2,5)]=0
        dico_position_B[(2,4)]=4

    elif (a,b)==(2,6) and (c,d)==(2,8) and plateau[a][b]==-6 and (c,d) in l:
        plateau[2][8] = -6
        plateau[2][7] = -4
        plateau[2][6] = 0
        plateau[2][9] = 0
        position_B[0]=(2,7)
        position_B[4]=(2,8)
        del dico_position_B[(2,6)]
        del dico_position_B[(2,9)]
        dico_position_B[(2,7)]=0
        dico_position_B[(2,8)]=4
    else :
        if plateau[a][b] == 0:
            return("On ne peut pas jouer avec une case vide !" + str((a,b,c,d)))
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
    #promotion(c,d)
    tour_blanc=not(tour_blanc)

def movetest(a,b,c,d):
    """
        * Same goal as move(a,b,c,d) but doesn't take care about rules (moving positions allowed, tour)
        * Also updates dico_position_W, dico_position_B, position_W, position_B,wonW,wonB
        * Essentially useful for tests
    """
    if plateau[a][b] == 0:
        return("On ne peut pas jouer avec une case vide !")
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

def move_chess(a,b,c,d):
    """
        * Special goal of move(a,b,c,d) useful for chess_mate functions which doesn't take care about taken pieces.
        * Doesn't update wonW,wonB
    """
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

def movebis(a,b,c,d):
    """
        * Moves a piece located on (a,b) to (c,d) if the movement is allowed by changing the values of plateau.
        * Updates dico_position_W, dico_position_B, position_W, position_B,wonW,wonB
        * Reverses the boolean value of tour_blanc to allow next player to play

        :param a: X axis of the piece we want to move
        :param b: Y axis of the piece we want to move
        :param c: X axis of the position we want to move the piece on
        :param d: Y axis of the position we want to move the piece on
        :type a: int
        :type b: int
        :type c: int
        :type d: int
        :return: None
        :rtype: None
    """
    global tour_blanc

    l = valeurs_accessibles(a,b)

    if (a,b)==(9,6) and (c,d)==(9,4) and plateau[a][b]==6 and (c,d) in l:
        plateau[9][4] = 6
        plateau[9][5] = 4
        plateau[9][6] = 0
        plateau[9][2] = 0
        position_W[0]=(9,5)
        position_W[4]=(9,4)
        del dico_position_W[(9,6)]
        del dico_position_W[(9,2)]
        dico_position_W[(9,5)]=0
        dico_position_W[(9,4)]=4

    elif (a,b)==(9,6) and (c,d)==(9,8) and plateau[a][b]==6 and (c,d) in l:
        plateau[9][8] = 6
        plateau[9][7] = 4
        plateau[9][6] = 0
        plateau[9][9] = 0
        position_W[0]=(9,7)
        position_W[4]=(9,8)
        del dico_position_W[(9,6)]
        del dico_position_W[(9,9)]
        dico_position_W[(9,7)]=0
        dico_position_W[(9,8)]=4

    elif (a,b)==(2,6) and (2,d)==(2,4) and plateau[a][b]==-6 and (c,d) in l:
        plateau[2][4] = -6
        plateau[2][5] = -4
        plateau[2][6] = 0
        plateau[2][2] = 0
        position_B[0]=(2,5)
        position_B[4]=(2,4)
        del dico_position_B[(2,6)]
        del dico_position_B[(2,2)]
        dico_position_B[(2,5)]=0
        dico_position_B[(2,4)]=4

    elif (a,b)==(2,6) and (c,d)==(2,8) and plateau[a][b]==-6 and (c,d) in l:
        plateau[2][8] = -6
        plateau[2][7] = -4
        plateau[2][6] = 0
        plateau[2][9] = 0
        position_B[0]=(2,7)
        position_B[4]=(2,8)
        del dico_position_B[(2,6)]
        del dico_position_B[(2,9)]
        dico_position_B[(2,7)]=0
        dico_position_B[(2,8)]=4
    else :
        if plateau[a][b] == 0:
            return("On ne peut pas jouer avec une case vide !" + str((a,b,c,d)))
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
    #promotion(c,d)
    
def board_to_move(board): #permet de retrouver le move à partir du plateau final
    """
        Returns move done on initial board plateau given final board configuration "board"
        :param board: final board configuration
        :type board: numpy array
        :return: move done
        :rtype: tuple
    """
    res=[]
    for k in range(12):
        for l in range(12):
            if plateau[k][l]!= board[k][l]:
                res+=[(k,l)]
    a,b = res[0]
    c,d = res[1]
    if (c,d) in valeurs_accessibles(a,b):
        return (a,b,c,d)
    if (a,b) in valeurs_accessibles(a,b):
        return (c,d,a,b)
    else :
        print("erreur sur board_to_move")

def ensemble_valeurs_accessibles_W():
    """
        Concatenates the accessible values of each white pieces.

        :return: all accessibles values of white pieces
        :rtype: tuple array
    """
    res=[]
    for (k,l) in dico_position_W.keys():
        res+=valeurs_accessibles_test(k,l)
    return res

def ensemble_valeurs_accessibles_B():
    """
        Concatenates the accessible values of each black pieces

        :return: all the accessibles values of black pieces
        :rtype: tuple array
    """
    res=[]
    for (k,l) in dico_position_B.keys():
        res+=valeurs_accessibles_test(k,l)
    return res

def ensemble_move_possible_W():
    """
        Concatenates the possible moves of each white pieces

        :return: all the possible moves of white pieces
        :rtype: tuple array
    """
    if chess_W():
        return mouv_possible_chess_W()
    res=[]
    for (k,l) in dico_position_W.copy().keys():
        for x,y in valeurs_accessibles_test(k,l):
            temp=np.copy(plateau)
            movebis(k,l,x,y)
            if not chess_W():
                res+=[(k,l,x,y)]
            scan(temp)
    return res

def ensemble_move_possible_B():
    """
        Concatenates the possible moves of each black piece

        :return: all the possible moves of black pieces
        :rtype: tuple array
    """
    if chess_B:
        return mouv_possible_chess_B()
    res=[]
    for (k,l) in dico_position_B.copy().keys():
        for x,y in valeurs_accessibles_test(k,l):
            temp=np.copy(plateau)
            movebis(k,l,x,y)
            if not chess_B():
                res+=[(k,l,x,y)]
            scan(temp)
    return res

def valeurs_accessibles_gui(x,y):
    res=[]
    l_W = ensemble_move_possible_W()
    l_B = ensemble_move_possible_B()
    for a,b,c,d in l_W:
        if (x,y)==(a,b):
            res.append((c,d))
    for a,b,c,d in l_B:
        if (x,y)==(a,b):
            res.append((c,d))
    return res

#position du roi en 4ème position dans la liste des positions des pièces blanches
#retour de la fonction : mise en échec ou pas

def chess_W():
    """
        Tells if the white king is in a chess situation

        :return: * True -> Chess situation : the white king belongs to ensemble_move_possible_B
                 * False -> Not a chess situation
        :rtype: boolean
    """
    return (position_W[4] in (ensemble_valeurs_accessibles_B()))

def chess_B():
    """
        Tells if the black king is in a chess situation

        :return: * True -> Chess situation : the black king belongs to ensemble_move_possible_W
                 * False -> Not a chess situation
        :rtype: boolean
    """
    return (position_B[4] in (ensemble_valeurs_accessibles_W()))

def chess_Mate_B():
    """
        Tells if the black king is in a chessmate situation

        :return: True -> White player wins
        :rtype: boolean
    """
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
    """
        Concatenates the possible moves of black piece to avoid a chess situation

        :return: * list of possible moves (x,y,k,l) to avoid chess situation
                 - x,y : initial position of a black piece
                 - k,l : final position that avoid chess situation
        :rtype: tuple array
    """
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
    """
        Tells if the white king is in a chessmate situation

        :return: True -> Black player wins
        :rtype: boolean
    """
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
        poss=valeurs_accessibles_test(x,y)
        for (k,l) in poss:
            move_chess(x,y,k,l)
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
    """
        Concatenates the possible moves of white pieces to avoid a chess situation

        :return: * list of possible moves (x,y,k,l) to avoid chess situation
                 - x,y : initial position of a white piece
                 - k,l : final position that avoid chess situation
        :rtype: tuple array
    """
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
    """
        Tells if piece a is an opponent of piece b.

        :param a: piece a (which could be a relative integer between -6 and 6 and couldn't be 0 , 0=empty piece)
        :param b: piece b (which could be a relative integer between -6 and 6 and couldn't be 0, 0=empty piece)
        :type a: int
        :type b: int
        :return: True -> a is an opponent of b
        :rtype: boolean
    """
    return (a*b<0)

def valide(a):
    """
        Tells if a piece is valid, that is to say belongs to the 8*8 square gamezone.

        :param a: exists x,y -> a=plateau[x][y]
        :type a: int
        :return: True -> piece is valid
        :rtype: boolean
    """
    return a!=-15



def valeurs_accessibles(x,y):
    """
        Returns the array of accessible chessboard positions of a piece located on (x,y).

        :param x: X axis of initial piece's position
        :param y: Y axis of initial piece's position
        :type x: int
        :type y: int
        :return: array of accessible plateau positions of a piece located on (x,y)
        :rtype: tuple array
    """
    res=[]
    piece_depart=plateau[x][y]
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
        if opponent(plateau[x-1][y+1],piece_depart) and valide(plateau[x-1][y+1]):#manger à droite
            res.append((x-1,y+1))
        if opponent(plateau[x-1][y-1],piece_depart) and valide(plateau[x-1][y-1]): #manger à gauche
            res.append((x-1,y-1))

    if (plateau[x][y]==-1): #piece_depart=pion_negatif
        if (plateau[x+1][y]==0) and valide(plateau[x+1][y]): #mouvement basique
            res.append((x+1,y))
        if (x==3) and  (plateau[x+2][y]==0) and valide(plateau[x+2][y]):
            res.append((x+2,y))
        if opponent(plateau[x+1][y+1],piece_depart) and valide(plateau[x+1][y+1]) and (plateau[x+1][y]==0):#manger à droite
            res.append((x+1,y+1))
        if opponent(plateau[x+1][y-1],piece_depart) and valide(plateau[x+1][y-1]): #manger à gauche
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

    res+=roque(x,y)
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
        if opponent(plateau[x-1][y+1],piece_depart) and valide(plateau[x-1][y+1]):#manger à droite
            res.append((x-1,y+1))
        if opponent(plateau[x-1][y-1],piece_depart) and valide(plateau[x-1][y-1]): #manger à gauche
            res.append((x-1,y-1))

    if (plateau[x][y]==-1): #piece_depart=pion_negatif
        if (plateau[x+1][y]==0) and valide(plateau[x+1][y]): #mouvement basique
            res.append((x+1,y))
        if (x==3) and  (plateau[x+2][y]==0) and valide(plateau[x+2][y]):
            res.append((x+2,y))
        if opponent(plateau[x+1][y+1],piece_depart) and valide(plateau[x+1][y+1]):#manger à droite
            res.append((x+1,y+1))
        if opponent(plateau[x+1][y-1],piece_depart) and valide(plateau[x+1][y-1]): #manger à gauche
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


#On adapte les données du plateau pour le modèle

def piece_converter(a):
    """
        Converting function for adapting pieces for neural network model

        :param x: piece to convert
    """
    k=abs(a)
    if k == 0:
        res=0
    if k == 4:
        res=5
    if k == 2:
        res=3
    if k == 3:
        res=3.5
    if k == 5:
        res=9
    if k == 6:
        res=0
    if k == 1:
        res=1
    if a <= 0:
        return(-res)
    return(res)


#def eval_denombrement():
#    global plateau
#    config2=np.array([adapt(plateau)])
#    prediction = knnThomas.predict_class_knn(config2[:])
#    return(prediction[0])

#Création de l'arbre de jeu

root_tree_W=Node((0,0,0,0,0))

def create_tree_W_viz():
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

def create_tree_W(): #arbre non-lisible mais seulement utile pour alpha_beta et min-max
    """
        * If white player has to play, create a 3-height tree of all playing configurations (considering W-B-W)
        * Each one is associated with an evaluation of the chessboard configuration (evaluation function)
        * This tree will then be crossed by minimax and alpha-beta algorithms.

    """
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
        acc=move(a,b,c,d)
        if (type(acc)==str):
            print("prodondeur:1 " + acc)
        node_i=Node((a,b,c,d,0),parent=root_tree_W)
        temp1_2=np.copy(plateau)
        temp2_2=copy(position_W)
        temp3_2=dico_position_W.copy()
        temp4_2=copy(position_B)
        temp5_2=dico_position_B.copy()
        temp6_2=copy(wonW)
        temp7_2=copy(wonB)
        for i,j,k,l in (ensemble_move_possible_B()):
            acc=move(i,j,k,l)
            if (type(acc) == str):
                print("prodondeur:2 " + acc)
            node_i_k=Node((a,b,c,d,0),parent=node_i)
            temp1_3=np.copy(plateau)
            temp2_3=copy(position_W)
            temp3_3=dico_position_W.copy()
            temp4_3=copy(position_B)
            temp5_3=dico_position_B.copy()
            temp6_3=copy(wonW)
            temp7_3=copy(wonB)
            for m,n,o,p in (ensemble_move_possible_W()):
                acc = move(m,n,o,p)
                if type(acc)==str:
                    print("prodondeur:3 " + acc)
                val=eval_denombrement()
                node_i_k_l=Node((a,b,c,d,val),parent=node_i_k)
                plateau=np.copy(temp1_3)
                position_W=copy(temp2_3)
                dico_position_W=temp3_3.copy()
                position_B=copy(temp4_3)
                dico_position_B=temp5_3.copy()
                wonW=copy(temp6_3)
                wonB=copy(temp7_3)
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

#root_tree_B=Node((0,0,0,0,0))

def roque(x,y):
    """
        If king is in castling configuration, returns accessible value for king that we concatenate to valeurs_accessibles(x,y)

        :param x: x axis of piece
        :param y: y axis of piece
        :type x: int
        :type y: int
        :return: array of castling accessible values for king
        :rtype: tuple array
    """
    res=[]
    if (x,y) == (9,6):
        if plateau[9][2]==4 and plateau[9][3]==0 and plateau[9][4]==0 and plateau[9][5]==0 and plateau[9][6]==6:
            res+=[(9,4)]
        if plateau[9][9]==4 and plateau[9][8]==0 and plateau[9][7]==0 and plateau[9][6]==6:
            res+=[(9,8)]
    if (x,y) == (2,6):
        if plateau[2][2]==-4 and plateau[2][3]==0 and plateau[2][4]==0 and plateau[2][5]==0 and plateau[2][6]==-6:
            res+=[(2,4)]
        if plateau[2][9]==-4 and plateau[2][8]==0 and plateau[2][7]==0 and plateau[2][6]==-6:
            res+=[(2,8)]
    return res

#Configuration jeu

def tour_Blanc(x):
    return x

def string_converter(a):
    """
        String move converter for games data parsing.

        :param x: board coordonate char
        :type x: char
        :rtype: int
    """
    if (a=='a'):
        res=2
    if (a=='b'):
        res=3
    if (a=='c'):
        res=4
    if (a=='d'):
        res=5
    if (a=='e'):
        res=6
    if (a=='f'):
        res=7
    if (a=='g'):
        res=8
    if (a=='h'):
        res=9
    return res

def converter(str):
    """
        String move converter for games data parsing.

        :param x: string move
        :type x: string
        :rtype: int tuple
    """
    a=string_converter(str[0])
    b=10-int(str[1])
    c=string_converter(str[2])
    d=10-int(str[3])
    return (b,a,d,c)

initialize()

# tester la promotion
#move(8,5,6,5)
#move(3,5,5,5)
#move(9,3,7,4)
#move(3,6,4,6)
#move(7,4,5,5)
#move(4,6,5,6)
#move(2,5,4,7)
#move(5,5,4,7)
#move(3,8,4,8)
#move(6,5,5,5)
#move(4,7,6,8)
#move(6,5,5,5)
#move(5,5,4,5)
#move(4,5,3,5)
#move(3,5,2,5)
#print(plateau[2][5])
#print(valeurs_accessibles_test(2,5))
#promotion(2,5)

root_tree_B=Node((0,0,0,0,0))

#for pre, fill, node in RenderTree(root_tree_B):
#    print("%s%s" % (pre, node.name))
