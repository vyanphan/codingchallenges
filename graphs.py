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
