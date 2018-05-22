#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import echecs
import numpy
import IA_denombrement
import IA_nn
import IA_knn
import IA_mcts
import alphabeta
from anytree import Node,RenderTree

def move_IA_denombrement_black():
    """
        * Complete IA black player game turn simulation
                                                        - Create black tree ready to be crossed
                                                        - Execution of alpha-beta algorithm
        * Used by Graphical User Interface

        :return: best move parameters (x,y,k,l) for black player considering alpha-beta algorithm
        :rtype: tuple
    """
    global root_tree_B
    del echecs.root_tree_B
    echecs.root_tree_B=Node((0,0,0,0,0))
    IA_denombrement.create_tree_B()
    return alphabeta.get_alpha_beta_B()

def move_IA_nn_black():
    """
        * Complete IA black player game turn simulation
                                                        - Create black tree ready to be crossed
                                                        - Execution of alpha-beta algorithm
        * Used by Graphical User Interface

        :return: best move parameters (x,y,k,l) for black player considering alpha-beta algorithm
        :rtype: tuple
    """
    global root_tree_B
    del echecs.root_tree_B
    echecs.root_tree_B=Node((0,0,0,0,0))
    IA_nn.create_tree_B()
    return alphabeta.get_alpha_beta_B()

def move_IA_knn_black():
    """
        * Complete IA black player game turn simulation
                                                        - Create black tree ready to be crossed
                                                        - Execution of alpha-beta algorithm
        * Used by Graphical User Interface

        :return: best move parameters (x,y,k,l) for black player considering alpha-beta algorithm
        :rtype: tuple
    """
    global root_tree_B
    del echecs.root_tree_B
    echecs.root_tree_B=Node((0,0,0,0,0))
    IA_knn.create_tree_B()
    return alphabeta.get_alpha_beta_B()

def move_IA_mcts_black(tmax):
    global root_tree_B
    del echecs.root_tree_B
    root_plateau=numpy.copy(echecs.plateau)
    echecs.root_tree_B = Node([root_plateau,0,0,0])
    l = echecs.ensemble_move_possible_B()
    for a,b,c,d in l:
        echecs.move(a,b,c,d)
        child = Node([echecs.plateau,0,0,0],parent=echecs.root_tree_B)
        echecs.scan(echecs.root_tree_B.name[0])
    plateaufinal = numpy.copy(IA_mcts.monte_carlo_tree_search(echecs.root_tree_B,tmax).name[0])
    echecs.plateau = numpy.copy(root_plateau)
    return echecs.board_to_move(plateaufinal)
