from graph import *

'''def DFS(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    #print ('Current dfs path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = DFS(graph,node,end,path,shortest)
            if newPath != None:
                return newPath'''
def DFS(digraph,start,end,path=[],routes=[]):
    '''
    return a list of paths leading to end
    '''
    path=path+[start]
    path_copy=path[:]
    #print('path: ',path)
    #print('path_copy:',path_copy)
    if start==end:
        routes.append(path)
        return routes
    for child in digraph.childrenOf(Node(start)):
        path=path_copy[:] #path_copy is the path before recurring for each child
        #print('path inside child loop: ',path)
        if child not in path:
            routes=DFS(digraph,child,end,path,routes)
            #print('routes',routes)
    return routes



'''def DFS_iterative(graph,start,end,path=[],shortest = None):
    stack = []
    stack.append(start)
    visited = []
    dfs = []
    while len(stack)!=0:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for n in graph.childrenOf(v):
                if n not in visited:
                    stack.append(n)
                    #every child node of start will be explored using DFS
                    #and their children as well
                    #if n not in visited:
                    #if n not in visited:
                    result = DFS(graph,n,end)
                    if result != None:
                        dfs.append([v]+result)
        print('stack ',stack)
        print('visited ',visited)
    ret_dfs = []

    for item in dfs:
        if (item[0]==start and item[-1]==end ):
            ret_dfs.append(item)
    #this fixes the shorter paths that also lead to end from start
    #this might not be necessary if a better way of accounting for
    #visited paths can be implemented above
    for item in dfs:
        for item2 in dfs:
            if set(item)<set(item2):
                if item in ret_dfs:
                    ret_dfs.remove(item)
    print(ret_dfs,len(ret_dfs))
    #print(visited)
 '''       

def DFSShortest(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    #print ('Current dfs path:', printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                newPath = DFSShortest(graph,node,end,path,shortest)
                if newPath != None:
                    shortest = newPath
    return shortest


def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    sp = DFS(g, nodes[0], nodes[5])
    print( 'Shortest path found by DFS:', sp)
