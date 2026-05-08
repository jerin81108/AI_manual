import heapq

graph = {
    'A': [('B',1),('C',4)],
    'B': [('D',2),('E',5)],
    'C': [('F',3)],
    'D': [('G',1)],
    'E': [('G',2)],
    'F': [('G',4)],
    'G': []
}

h = {'A':7,'B':6,'C':5,'D':4,'E':2,'F':3,'G':0}

def sma_star(start, goal, limit=5):
    queue = [(h[start], 0, start, [start])]
    visited = set()
    while queue:
        if len(queue) > limit:
            queue.sort()
            queue.pop()
        f, g, node, path = heapq.heappop(queue)
        if node == goal:
            return path, g
        if node in visited:
            continue
        visited.add(node)
        for nb, cost in graph[node]:
            if nb not in visited:
                heapq.heappush(queue, (g+cost+h[nb], g+cost, nb, path+[nb]))
    return None, -1

path, cost = sma_star('A', 'G')
print("Path:", " -> ".join(path))
print("Cost:", cost)
