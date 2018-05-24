#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import echecs

#Algorithme minimax

def is_max_W(arb):
    """
        * Epecially used by minimax and alpha-beta algorithms
        * Tells if a node is a "max-node"

        :param arb: node
        :type arb: node
        :rtype: boolean
    """
    if arb.is_root:
        return True
    else:
        n=(arb.ancestors[0]).height
        return ((n-arb.height)%2==0)

def is_min_B(arb):
     """
        * Epecially used by minimax and alpha-beta algorithms
        * Tells if a node is a "max-node"

        :param arb: node
        :type arb: node
        :rtype: boolean
    """
     if arb.is_root:
        return True
     else:
        n=(arb.ancestors[0]).height
        return ((n-arb.height)%2==0)

def minimax_W(arb,profondeur): #Minimax pour les arbres à quintuplet-> 4 premières valeurs pour le move
    """
       * Recursive algorithm which is supposed to cross a tree previously constructed by create_tree_W.
       * Represents the best way to modelize zero sum games such as chess.

       :param arb: node algorithm is executing on
       :param profondeur: height of the node algorithm is executing on
       :type arb: node
       :type profondeur: int
       :return: * tuple (x,k,l,g) - (x,y,k,l) is associated to the future move to do
                                  - g is the result of the evaluation function of the chessboard configuration
       :rtype: tuple
    """                                                             #-> 5ème : valeur de la fonction d'éval
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

#Pour les blancs

def get_minimax_W():
    """
       Returns the tuple (x,y,k,l) that corresponds to the best move for white player considering the minimax algorithm

       :return: tuple (x,y,k,l) to implement in the move function which will finally simulate IA
       :rtype: tuple
    """
    return minimax_W(root_tree_W,0)[0:4]

#Pour les noirs

def minimax_B(arb,profondeur): #Minimax pour les arbres à quintuplet-> 4 premières valeurs pour le move
    """
       * Recursive algorithm which is supposed to cross a tree previously constructed by create_tree_W.
       * Represents the best way to modelize zero sum games such as chess.
       :return: * tuple (x,k,l,g) - (x,y,k,l) is associated with the future move to do
                                  - g is the result of the evaluation function of the chessboard configuration
       :rtype: tuple
    """                                                             #-> 5ème : valeur de la fonction d'éval
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
    """
       Returns the tuple (x,y,k,l) that corresponds to the best move for black player considering the minimax algorithm

       :return: tuple (x,y,k,l) to implement in the move function which will finally simulate IA
       :rtype: tuple
    """
    return minimax_B(root_tree_B,0)[0:4]

#Élagage alpha_beta

#Pour les blancs
def alpha_beta_W(arb,profondeur,alpha,beta):
    """
       Optimized minimax reccursive algorithm which doesn't consider useless branchs thanks to alpha and beta parameters

       :param arb: node algorithm is executing on
       :param profondeur: height of the node algorithm is executing on
       :param alpha: inferior value of cutting interval (initially negative infinite)
       :param beta: superior value of cutting interval(initially positive infinite)
       :type arb: node
       :type profondeur: int
       :type alpha: int
       :type beta: int
       :return: * tuple (x,k,l,g) - (x,y,k,l) is associated with the future move to do
                                  - g is the result of the evaluation function of the chessboard configuration
       :rtype: tuple
    """
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
    """
       Returns the tuple (x,y,k,l) that corresponds to the best move for white player considering the minimax algorithm optimized with alpha-beta method

       :return: tuple (x,y,k,l) to implement in the move function which will finally simulate IA
       :rtype: tuple
    """
    return alpha_beta_W(root_tree_W,0,-math.inf,math.inf)[0:4]

#Pour les noirs

def alpha_beta_B(arb,profondeur,alpha,beta):
    """
       Optimized minimax reccursive algorithm which doesn't consider useless branchs thanks to alpha and beta parameters

       :param arb: node algorithm is executing on
       :param profondeur: height of the node algorithm is executing on
       :param alpha: inferior value of cutting interval (initially negative infinite)
       :param beta: superior value of cutting interval(initially positive infinite)
       :type arb: node
       :type profondeur: int
       :type alpha: int
       :type beta: int
       :return: * tuple (x,k,l,g) - (x,y,k,l) is associated with the future move to do
                                  - g is the result of the evaluation function of the chessboard configuration
       :rtype: tuple
    """
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
    """
       Returns the tuple (x,y,k,l) that corresponds to the best move for black player considering the minimax algorithm optimized with alpha-beta method

       :return: tuple (x,y,k,l) to implement in the move function which will finally simulate IA
       :rtype: tuple
    """
    return alpha_beta_B(echecs.root_tree_B,0,-math.inf,math.inf)[0:4]
