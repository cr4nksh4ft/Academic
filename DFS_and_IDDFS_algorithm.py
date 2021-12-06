from typing import DefaultDict

def generateGraph():
    '''
    GENERATES GRAPH FROM INPUT
    RETURNS ADJACENCY LIST AND DEPTH
    '''
    adjacency_list = DefaultDict(list)
    no_of_nodes = int(input('Enter no. of nodes: '))
    max_depth=no_of_nodes
    for _ in range(no_of_nodes):
        node = input('Enter node label: ')
        adj_nodes = input('Enter space separated adjacent nodes: ')
        if(adj_nodes!=""):
            adjacency_list[f'{node}'].extend(adj_nodes.split(" "))
        else:
            adjacency_list[f'{node}']=[]
            max_depth-=1
    return adjacency_list,max_depth

def DFS(graphAdjacencyList,source,goal,visited):
    found=False
    
    def recursiveDFS(source,visited):
        nonlocal found
        if(found):
            return
        print('Visited',source,sep=" ")
        if(source==goal):
            found=True
        if source not in visited:
            visited.add(source)
            for neighbour in graphAdjacencyList[source]:
                recursiveDFS(neighbour,visited)
    #DRIVER
    recursiveDFS(source,visited)
    print(f'GOAL NODE {goal} FOUND' if found else f'GOAL NODE {goal} NOT FOUND')
    return

def IDDFS(graphAdjacencyList,max_depth,root,goal):
    
    def recursiveDLS(node,depth):
        print('     Visited',node,sep=" ")
        if depth == 0:
            if(node==goal):
                return (node,True)
            else:
                return (None,True)
        else:
            any_rem = False
            for child in graphAdjacencyList[f'{node}']:
                fnd, rem = recursiveDLS(child,depth-1)
                if(fnd!=None):
                    return (fnd,True)
                if(rem):
                    any_rem = True
            return (None,any_rem)
    #DRIVER
    for depth in range(max_depth+1):
        print(f'MAX DEPTH = {depth}')
        found,remaining = recursiveDLS(root,depth)
        if(found!=None):
            print(f'FOUND {goal} AT DEPTH {depth}')
            return
        elif(not remaining or depth==max_depth):
            print(f"GOAL NODE {goal} NOT FOUND")
            return

#DFS & IDDFS
def search():
    #MENU
    opt = input('Search techniques\n1.DFS\n2.IDDFS\nSelect operation:')
    graph,max_depth = generateGraph()
    src = input('Enter source node label:')
    goal = input('Enter goal node label:')
    if(opt=='1'):
        DFS(graph,src,goal,set())
    elif(opt=='2'):
        IDDFS(graph,max_depth,src,goal)

#START
search()
