import echecs
import math
import random
from anytree import Node
import numpy as np
import time

#changement de stratégie : un noeud n'est plus un move mais une configuration de plateau

#node = (plateau,visited{0,1},Q,V)

c=0.1

def tour_B(node):
    return node.depth%2 == 0


def terminal(node):
    """
        Returns if a node is terminal, ie board contained in node is in a chessmate configuration

        :param node: considered node
        :type node: node
        :rtype: boolean
    """
    return echecs.chess_Mate_B() or echecs.chess_Mate_W()

def fully_expanded(node):
    """
        Returns if a node is fully expanded, ie its children have been all visited once

        :param node: considered node
        :type node: node
        :rtype: boolean
    """
    for child in node.children:
        if (child.name[1]==0):
            return False
    return True

def pick_unvisited_child(node):
    """
        Picks an unvisited child of considered node, and actualizes its visit parameter

        :param node: considered node
        :type node: node
        :return: unvisited node's child
        :rtype: node
    """
    if terminal(node):
        return node
    for child in node.children:
        if (child.name[1]==0):
            child.name[1]=1
            return child

def best_uct(node):
    """
        Returns best node child considering uct value
        uct grows : * simulations winning ratio grows (Q/V)
                    * number of visits decreases

        :param node: considered node
        :type node: node
        :return: best uct node
        :rtype: node
    """
    maxi=0
    res=pick_random_child(node)
    for child in node.children:
        Q_vi = child.name[2]
        N_vi = child.name[3]
        N_v = node.name[3]
        uct = (Q_vi/N_vi) + c*math.sqrt(math.log(N_v)/N_vi)
        if uct > maxi:
            maxi = uct
            res = child
    return res

def traverse(node):
    """
        * Recursive function which returns an unvisited node's child if node isn't fully expanded, else picd the best uct node and
        does it again.
        * Then, it traverses deep in the tree to pick most promising and not fully expanded node

        :param node: considered node(always root)
        :type node: node
        :return: most promising and not fully expanded node
        :rtype: node
    """
    while fully_expanded(node):
        node = best_uct(node)
        echecs.scan(node.name[0])
        if tour_B(node):
            l=echecs.ensemble_move_possible_B()
        else:
            l=echecs.ensemble_move_possible_W()
        for a,b,c,d in l:
            echecs.move(a,b,c,d)
            new_node = Node([echecs.plateau,0,0,0],parent=node)
            echecs.scan(node.name[0])
    return pick_unvisited_child(node)

def result(node):
    """
        Returns result of a terminal node

        :param node: considered node
        :type node: node
        :return: * 1 if black won (white king in chessmate configuration)
                 * -1 if white won (black king in chessmate configuration)
        :rtype: int
    """
    if tour_B(node) :
        return 1
    else:
        return -1


def pick_random_child(node):
    """
        Picks a random child of considered node for random simulation process

        :param node: considered node
        :type node: node
        :return: random node's child
        :rtype: node
    """
    l=[]
    for child in node.children:
        l.append(child)
    return(l[random.randint(0,len(l)-1)])



def rollout(node):
    """
        * Simulates a random full play game given initial node until terminal node
        * If number of plays exceeds tmax, considers the game drawn

        :param node: initial node of simulation
        :type node: node
        :return: result of simulation
        :rtype: int
    """
    t=0
    tmax=100
    while not (terminal(node)) and t<tmax:
        t+=1
        node=rollout_policy(node)
    if t == tmax:
        return 0
    else :
        return result(node)

def eval_denombrement_bis():
    """
        Evaluation function that only considers
        taken pieces by each times

        :return: gain of the current chessboard configuration
        :rtype: int

    """
    res = 0
    for k in range(2,10):
        for l in range(2,10):
            res += echecs.piece_converter(echecs.plateau[k][l])
    return res

def rollout_bis(node):
    """
        * Simulates a random full play game given initial node until terminal node
        * If number of plays exceeds tmax, evaluates final board configuration with eval_denombrement to determine whose player is winning the simulation

        :param node: initial node of simulation
        :type node: node
        :return: result of simulation
        :rtype: int
    """
    t=0
    tmax=30
    while not (terminal(node)) and t<tmax:
        t+=1
        node=rollout_policy(node)
    if t == tmax:
        res = eval_denombrement_bis()
        if res > 3:
            return node.name[0],t,-1
        if res < -3 :
            return node.name[0],t,1
        else :
            return node.name[0],t,0
    else :
        return node.name[0],t,result(node)

def rollout_bis_nn(node):
    """
        * Simulates a random full play game given initial node until terminal node
        * If number of plays exceeds tmax, evaluates final board configuration with eval_nn to determine whose player is winning the simulation

        :param node: initial node of simulation
        :type node: node
        :return: result of simulation
        :rtype: int
    """
    t=0
    tmax=30
    while not (terminal(node)) and t<tmax:
        t+=1
        node=rollout_policy(node)
    if t == tmax:
        res = echecs.eval_nn()
        if res > 3:
            return node.name[0],t,-1
        if res < 3:
            return node.name[0],t,1
        else:
            return node.name[0],t,0
    else :
        return node.name[0],t,result(node)

def rollout_policy(node):
    """
        Builds node's children to continue simulation and picks one of them randomly

        :param node: considered node
        :type node: node
        :return: random child of node
        :rtype: node
    """
    if tour_B(node):
        l=echecs.ensemble_move_possible_B()
    else:
        l=echecs.ensemble_move_possible_W()
    for a,b,c,d in l:
        echecs.move(a,b,c,d)
        for child in node.children:
            if (np.array_equal(echecs.plateau,child.name[0])):
                echecs.scan(node.name[0])
        new_node = Node([echecs.plateau,0,0,0],parent=node)
        echecs.scan(node.name[0])
    picked = pick_random_child(node)
    echecs.scan(picked.name[0])
    return picked

def best_child(node):
    """
        Returns most visited child, given many simulations, best_child(root) is the most promising move to do

        :param node: considered node(always root)
        :type node: node
        :return: most visited child
        :rtype: node
    """
    maxi=0
    for child in node.children:
        N_vi = child.name[3]
        if N_vi > maxi:
            maxi = N_vi
            res= child
    return res

def back_propagate(node,result):
    """
        Backpropagate result's data (number of node visits, result of simulation) to node parents after simulation

        :param node: considered node
        :type node: node
        :rtype: None
    """
    if node.is_root:
        node.name[2]+=result
        node.name[3]+=1
    else:
        node.name[2]+=result
        node.name[3]+=1
        back_propagate(node.parent,result)

def monte_carlo_tree_search(root,tmax):
    """
        * Processes the Monte Carlo Tree Search Method during 100 seconds:
            - Picks an unfully expanded node (initially root) and picks one of its unvisited child
            - Calcul random full play simulation's result beginning from this node
            - Backpropagates result's data to picked node's parents
        * At the end of the process, returns the most visited root's child, ie the most promising move to play

        :param root: tree root (initial board configuration)
        :type root: node
        :return: most promising node
        :rtype: node
    """
    debut=time.time()
    fin = time.time()
    while (fin - debut) <= tmax:
        leaf=traverse(root)
        res,t,simulation_result=rollout_bis(leaf)
        back_propagate(leaf,simulation_result)
        fin = time.time()
        echecs.scan(leaf.parent.name[0])
    return best_child(root)
