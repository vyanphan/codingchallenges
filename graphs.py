from heapq import *

example_graph = {
    'A': {'C': 1, 'B': 1, 'D': 3, 'S': 3},
    'B': {'S': 1, 'A': 1, 'C': 1, 'D': 1},
    'S': {'E': 5, 'A': 3, 'B': 1, 'D': 3},
    'C': {'A': 1, 'D': 3, 'B': 1, 'E': 1},
    'D': {'F': 4, 'S': 3, 'B': 1, 'A': 3, 'C': 3, 'E': 2},
    'E': {'D': 2, 'C': 1, 'F': 2, 'S': 5},
    'F': {'D': 4, 'E': 2}
}



### Dijkstra's Algorithm
def dijkstra(graph, s):
    dist = {v: float('inf') for v in graph}
    dist[s] = 0

    unvisited = []
    unvisited_dict = {}
    for v, d in dist.items():
        entry = [d, v, None]
        unvisited_dict[v] = entry
        heappush(unvisited, entry)

    while unvisited:
        u = heappop(unvisited)[1]
        for n, nd in graph[u].items():
            d = dist[u] + nd
            if d < dist[n]:
                dist[n] = d
                unvisited_dict[n][0] = d
                unvisited_dict[n][2] = u

    return dist, unvisited_dict

a, b = dijkstra(example_graph, 'S')
print(a)
for k in b:
    print(k, b[k])



# A* search
def a_star_search(graph, s, e, heuristic):
    border = []
    heappush(border, [0, s])
    dist_dict = {s: [0, None]}
    
    while border:
        u = heappop(border)[1]
        if u == e:
            break
        
        for n, nd in graph[u].items():
            new_cost = dist_dict[u][0] + nd
            if n not in dist_dict or new_cost < dist_dict[n][0]:
                dist_dict[n] = [new_cost, u]
                heappush(border, [new_cost + heuristic(n, e), n])
    
    return dist_dict

print(a_star_search(example_graph, 'S', 'F', lambda x,y: 1))



# Breadth-First Search
def BFS(graph, s):
    visited = {s}
    ans = []
    queue = [s]

    while queue:
        u = queue.pop(0)
        ans += [u]
        for n in graph[u]:
            if n not in visited:
                visited.add(n)
                queue += [n]
    return ans

print(BFS(example_graph, 'S'))



# Depth-First Search
visited = set()

def DFS_helper(graph, v):
    visited.add(v)
    ans = [v]
    for n in graph[v]:
        if n not in visited:
            ans += DFS_helper(graph, n)
    return ans

def DFS(graph, s):
    return DFS_helper(graph, s)

print(DFS(example_graph, 'S'))





# Graph Colouring Problem
class Graph(): 
    def __init__(self, graph): 
        self.graph = graph 
        self.V = len(graph)
  
    def isSafe(self, v, colour, c): # neighbors not same colour
        for i in range(self.V): 
            if self.graph[v][i] == 1 and colour[i] == c: 
                return False
        return True

    def graphColourUtil(self, m, colour, v): 
        if v == self.V: # reached last vertex successfully
            return True
        for c in range(1, m+1): # try first colour that works
            if self.isSafe(v, colour, c): 
                colour[v] = c 
                if self.graphColourUtil(m, colour, v+1): 
                    return True
                colour[v] = -1
        return False


    def graphColouring(self, m): 
        colour = [-1] * self.V 
        self.graphColourUtil(m, colour, 0)
        return colour
  
# Driver Code 
graph = [[0,1,0,1,1,0],
         [1,0,1,0,1,1],
         [0,1,0,0,0,1],
         [1,0,0,0,1,0],
         [1,1,0,1,0,1],
         [0,1,1,0,1,0]] 
g = Graph(graph) 
print(g.graphColouring(3))



'''
Topographic sort.
We can come up with another system for marking 
visited/done nodes.
'''
def visit(n, visited, done, ans):
    if n in done:
        return
    if n in visited:
        return 'cycle'
    visited.add(n)
    for m in n.neighbors:
        ans = visit(m, visited, done, ans)
    done.add(n)
    return [L] + ans

def topographic_sort(graph):
    visited = set()
    done = set()
    V = graph.vertices
    ans = []
    while not V.empty():
        n = V.pop()
        ans = visit(n, visited, done, ans)
    return ans
        

