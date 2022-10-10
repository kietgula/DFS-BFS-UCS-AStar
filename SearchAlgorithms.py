from lib2to3.pgen2 import grammar
from Space import *
from Constants import *
import math
import sys
from operator import itemgetter



"""
def BuildPath(g:Graph, sc:pygame.surface, Node begin, Node end):
    delta_col=end.x-begin.x
    delta_row=end.y-begin.y

    straightPath=True #true la di ngang, false la di doc

    if (delta_col>delta_row):
        straightPath=True
    else: 
        straightPath=False

    currentNode=begin
    nextNode=currentNode

    if straightPath==True: #di ngang
        for i in range(0,delta_col-delta_row):
            g.draw(currentNode,grey)
            nextNode=g.grid_cells[currentNode.x+1+currentNode.y*cols]
            pygame.draw.line(sc, green, (currentNode.x,currentNode.y),(nextNode.x,nextNode.y))
            currentNode=nextNode
    
    elif straightPath==False: #di doc
        for i in range(0,delta_row-delta_col):
            g.draw(currentNode,grey)
            nextNode=g.grid_cells[currentNode.x+(currentNode.y+1)*cols]
            pygame.draw.line(sc, green, (currentNode.x,currentNode.y),(nextNode.x,nextNode.y))
            currentNode=nextNode
        
def DrawLine(g:Graph, sc:pygame.surface, Node begin, Node end):
    value_begin=begin.x+begin.y*rows
    value_end=end.x+end.y*rows

    g.grid_cells[value_end]
"""


def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')

    open_set = [g.start]
    closed_set = []
    father = [-1]*g.get_len()

    while open_set:
        node1=open_set.pop(0)
        node1.set_color(red)
        closed_set.append(node1)

        if g.is_goal(node1):
            return node1

        for node2 in g.get_neighbors_bigger(node1):
            if node2 not in closed_set and node2.value>node1.value:
                open_set.insert(0,node2)
                node2.father=node1
                node2.set_color(blue)

        g.draw(sc)

    open_set = [g.start]
    while open_set:
        node1=open_set.pop(0)
        node1.set_color(red)
        closed_set.append(node1)

        if g.is_goal(node1):
            return node1

        for node2 in g.get_neighbors_smaller(node1):
            if node2 not in closed_set and node2.value<node1.value:
                open_set.insert(0,node2)
                node2.father=node1
                node2.set_color(blue)
        g.draw(sc)


    
        
    #TODO: Implement DFS algorithm using open_set, closed_set, and father
    #raise NotImplementedError('Not implemented')

def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')

    open_set = [g.start]
    closed_set = []
    
    for node1 in open_set:
        node1.set_color(red)

        if g.is_goal(node1):
            return node1

        for node2 in g.get_neighbors_bigger(node1):
            if node2 not in open_set:
                open_set.append(node2)
                node2.father=node1
                node2.set_color(blue)

        g.draw(sc)

    open_set = [g.start]
    closed_set = []
    
    for node1 in open_set:
        node1.set_color(red)

        if g.is_goal(node1):
            return node1

        for node2 in g.get_neighbors_smallar(node1):
            if node2 not in open_set:
                open_set.append(node2)
                node2.father=node1
                node2.set_color(blue)

        g.draw(sc)

    #TODO: Implement BFS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')
def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')


    open_set=[(0,g.start,None)]

    closed_set=[]
    closed=[]
    while open_set:
        node1_tuple=open_set.pop(0)
        node1_tuple[1].set_color(red)
        closed_set.append(node1_tuple) #chứa node đã duyệt qua, ko bao gồm chi phí
        closed.append(node1_tuple[1].value)

        if g.is_goal(node1_tuple[1]):
            for node_tuple in closed_set:
                node_tuple[1].father=node_tuple[2]
            return node1_tuple[1]
            
        for node2 in g.get_neighbors(node1_tuple[1]):
            if node2.value not in closed:
                open_set.append((node2.value+node1_tuple[0],node2,node1_tuple[1]))
                node2.set_color(blue)

        open_set.sort(key=itemgetter(0))
        g.draw(sc)
    #TODO: Implement A* algorithm using open_set, closed_set, and father



    #TODO: Implement UCS algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')

def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')


    heuristic = [0]*g.get_len()

    open_set=[(0,g.start,None)]

    closed_set=[]
    closed=[]
    while open_set:
        node1_tuple=open_set.pop(0)
        node1_tuple[1].set_color(red)
        closed_set.append(node1_tuple) #chứa node đã duyệt qua, ko bao gồm chi phí
        closed.append(node1_tuple[1].value)

        if g.is_goal(node1_tuple[1]):
            for node_tuple in closed_set:
                node_tuple[1].father=node_tuple[2]
            return node_tuple[1]
            
        for node2 in g.get_neighbors(node1_tuple[1]):
            if node2.value not in closed:
                heuristic[node2.value] = math.sqrt((g.goal.x-node2.x)*(g.goal.x-node2.x) + (g.goal.y-node2.y)*(g.goal.y-node2.y))
                open_set.append((1+node1_tuple[0],node2,node1_tuple[1]))
                node2.set_color(blue)


        open_set.sort(key = lambda a: a[0] + heuristic[a[1].value])
        g.draw(sc)
    #TODO: Implement A* algorithm using open_set, closed_set, and father
    raise NotImplementedError('Not implemented')

def value(x:int, y:int):
    return x+y*cols

def NodeWalk(g:Graph, node:Node, ngang:int, doc:int, xien225do:int, xien135do:int):
    new_x=node.x+ngang+xien135do-xien225do
    new_y=node.y+doc+xien225do+xien135do
    
    if new_x>cols or new_y>rows:
        return None

    return g[value(new_x,new_y)]

def DrawPath(g:Graph, sc:pygame.Surface, node:Node):
    if node==None:
        return
    else:
        node.set_color(grey)

        if (node.father!=None):
            pygame.draw.line(sc, green, (node.x,node.y),(node.father.x,node.father.y))

        g.draw(sc)
        
        return(DrawPath(g,sc,node.father))