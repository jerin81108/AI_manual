from collections import deque

graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
def bfs(start_node):
    visited = {start_node}
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
# 2. Run it
print("BFS Traversal:")
bfs(2)