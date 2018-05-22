#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import echecs
from anytree import Node
import numpy as np

#description fonction d'évaluation dénombrement des pièces

def eval_denombrement():
    """
        Part of the evaluation function useful for minimax and alpha-beta, that only considers
        taken pieces by each times (stored in wonB and wonW)

        :return: gain of the current chessboard configuration
        :rtype: int

    """
    res=0
    for k in range(len(echecs.wonW)):
        if (echecs.wonW[k]==1):
            res+=1
        if (echecs.wonW[k]==2) or (echecs.wonW[k]==3):
            res+=3
        if (echecs.wonW[k]==4):
            res+=5
        if (echecs.wonW[k]==5):
            res+=9
        if (echecs.wonW[k]==6):
            res+=0 #à vérifier, les sources ne sont pas concordantes (0 ou +infini)

    for k in range(len(echecs.wonB)):
        if (echecs.wonB[k]==1):
            res+=-1
        if (echecs.wonB[k]==2) or (echecs.wonB[k]==3):
            res+=-3
        if (echecs.wonB[k]==4):
            res+=-5
        if (echecs.wonB[k]==5):
            res+=-9
        if (echecs.wonB[k]==6):
            res+=0 #à vérifier, les sources ne sont pas concordantes (0 ou +infini)
    return res

def create_tree_B(): #arbre non-lisible mais seulement utile pour alpha_beta et min-max
    """
        * If black player has to play, create a 3-height tree of all playing configurations (considering B-W-B)
        * Each one is associated with an evaluation of the final chessboard configuration (evaluation function)
        * This tree will then be crossed by minimax and alpha-beta algorithms.
    """
    global plateau
    global position_B
    global dico_position_B
    global position_W
    global dico_position_W
    global wonW
    global wonB
    temp1=np.copy(echecs.plateau)
    temp2=echecs.copy(echecs.position_W)
    temp3=echecs.dico_position_W.copy()
    temp4=echecs.copy(echecs.position_B)
    temp5=echecs.dico_position_B.copy()
    temp6=echecs.copy(echecs.wonW)
    temp7=echecs.copy(echecs.wonB)
    l=echecs.ensemble_move_possible_B()
    for a,b,c,d in (echecs.ensemble_move_possible_B()):
        acc = echecs.move(a,b,c,d)
        if (type(acc)==str):
            print("profondeur : 1" + acc)
        node_i= Node((a,b,c,d,0),parent=echecs.root_tree_B)
        temp1_2=np.copy(echecs.plateau)
        temp2_2=echecs.copy(echecs.position_W)
        temp3_2=echecs.dico_position_W.copy()
        temp4_2=echecs.copy(echecs.position_B)
        temp5_2=echecs.dico_position_B.copy()
        temp6_2=echecs.copy(echecs.wonW)
        temp7_2=echecs.copy(echecs.wonB)
        for i,j,k,l in (echecs.ensemble_move_possible_W()):
            acc=echecs. move(i,j,k,l)
            if (type(acc)==str):
                print("profondeur : 2" + acc)
            node_i_k=Node((a,b,c,d,0),parent=node_i)
            temp1_3=np.copy(echecs.plateau)
            temp2_3=echecs.copy(echecs.position_W)
            temp3_3=echecs.dico_position_W.copy()
            temp4_3=echecs.copy(echecs.position_B)
            temp5_3=echecs.dico_position_B.copy()
            temp6_3=echecs.copy(echecs.wonW)
            temp7_3=echecs.copy(echecs.wonB)
            for m,n,o,p in (echecs.ensemble_move_possible_B()):
                acc = echecs.move(m,n,o,p)
                if (type(acc)==str):
                    print("profondeur : 3" + acc)
               # print(m,n,o,p)
                val=eval_denombrement()
                node_i_k_l = Node((a,b,c,d,val),parent=node_i_k)
                echecs.plateau=np.copy(temp1_3)
                echecs.position_W=echecs.copy(temp2_3)
                echecs.dico_position_W=temp3_3.copy()
                echecs.position_B=echecs.copy(temp4_3)
                echecs.dico_position_B=temp5_3.copy()
                echecs.wonW=echecs.copy(temp6_3)
                echecs.wonB=echecs.copy(temp7_3)
                #t+=1
            echecs.plateau=np.copy(temp1_2)
            echecs.position_W=echecs.copy(temp2_2)
            echecs.dico_position_W=temp3_2.copy()
            echecs.position_B=echecs.copy(temp4_2)
            echecs.dico_position_B=temp5_2.copy()
            echecs.wonW=echecs.copy(temp6_2)
            echecs.wonB=echecs.copy(temp7_2)
        echecs.plateau=np.copy(temp1)
        echecs.position_W=echecs.copy(temp2)
        echecs.dico_position_W=temp3.copy()
        echecs.position_B=echecs.copy(temp4)
        echecs.dico_position_B=temp5.copy()
        echecs.wonW=echecs.copy(temp6)
        echecs.wonB=echecs.copy(temp7)

def create_tree_W(): #arbre non-lisible mais seulement utile pour alpha_beta et min-max
    """
        * If black player has to play, create a 3-height tree of all playing configurations (considering B-W-B)
        * Each one is associated with an evaluation of the final chessboard configuration (evaluation function)
        * This tree will then be crossed by minimax and alpha-beta algorithms.
    """
    global plateau
    global position_B
    global dico_position_B
    global position_W
    global dico_position_W
    global wonW
    global wonB
    temp1=np.copy(echecs.plateau)
    temp2=echecs.copy(echecs.position_W)
    temp3=echecs.dico_position_W.copy()
    temp4=echecs.copy(echecs.position_B)
    temp5=echecs.dico_position_B.copy()
    temp6=echecs.copy(echecs.wonW)
    temp7=echecs.copy(echecs.wonB)
    l=echecs.ensemble_move_possible_B()
    for a,b,c,d in (echecs.ensemble_move_possible_W()):
        acc = echecs.move(a,b,c,d)
        if (type(acc)==str):
            print("profondeur : 1" + acc)
        node_i= Node((a,b,c,d,0),parent=echecs.root_tree_W)
        temp1_2=np.copy(echecs.plateau)
        temp2_2=echecs.copy(echecs.position_W)
        temp3_2=echecs.dico_position_W.copy()
        temp4_2=echecs.copy(echecs.position_B)
        temp5_2=echecs.dico_position_B.copy()
        temp6_2=echecs.copy(wonW)
        temp7_2=echecs.copy(wonB)
        for i,j,k,l in (echecs.ensemble_move_possible_B()):
            acc=echecs. move(i,j,k,l)
            if (type(acc)==str):
                print("profondeur : 2" + acc)
            node_i_k=Node((a,b,c,d,0),parent=node_i)
            temp1_3=np.copy(echecs.plateau)
            temp2_3=echecs.copy(echecs.position_W)
            temp3_3=echecs.dico_position_W.copy()
            temp4_3=echecs.copy(echecs.position_B)
            temp5_3=echecs.dico_position_B.copy()
            temp6_3=echecs.copy(echecs.wonW)
            temp7_3=echecs.copy(echecs.wonB)
            for m,n,o,p in (echecs.ensemble_move_possible_W()):
                acc = echecs.move(m,n,o,p)
                if (type(acc)==str):
                    print("profondeur : 3" + acc)
               # print(m,n,o,p)
                val=eval_denombrement()
                node_i_k_l = Node((a,b,c,d,val),parent=node_i_k)
                echecs.plateau=np.copy(temp1_3)
                echecs.position_W=echecs.copy(temp2_3)
                echecs.dico_position_W=temp3_3.copy()
                echecs.position_B=echecs.copy(temp4_3)
                echecs.dico_position_B=temp5_3.copy()
                echecs.wonW=echecs.copy(temp6_3)
                echecs.wonB=echecs.copy(temp7_3)
                #t+=1
            echecs.plateau=np.copy(temp1_2)
            echecs.position_W=echecs.copy(temp2_2)
            echecs.dico_position_W=temp3_2.copy()
            echecs.position_B=echecs.copy(temp4_2)
            echecs.dico_position_B=temp5_2.copy()
            echecs.wonW=echecs.copy(temp6_2)
            echecs.wonB=echecs.copy(temp7_2)
        echecs.plateau=np.copy(temp1)
        echecs.position_W=echecs.copy(temp2)
        echecs.dico_position_W=temp3.copy()
        echecs.position_B=echecs.copy(temp4)
        echecs.dico_position_B=temp5.copy()
        echecs.wonW=echecs.copy(temp6)
        echecs.wonB=echecs.copy(temp7)
