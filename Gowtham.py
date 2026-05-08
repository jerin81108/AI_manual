def astar(start, goal):

    h = {
        "A": 11, "B": 6, "C": 5, "D": 7, "E": 3,
        "F": 6, "G": 5, "H": 3, "I": 1, "J": 0
    }

    graph = {
        "A": [("B", 6), ("F", 3)],
        "B": [("C", 3), ("D", 2)],
        "C": [("E", 5)],
        "D": [("E", 8)],
        "E": [("J", 5)],
        "F": [("G", 1), ("H", 7)],
        "G": [("I", 3)],
        "H": [("I", 2)],
        "I": [("J", 3)]
    }

    open_set = [start]
    g = {start: 0}
    parent = {start: start}

    while open_set:

        n = min(open_set, key=lambda x: g[x] + h[x])

        if n == goal:

            path = []

            while parent[n] != n:
                path.append(n)
                n = parent[n]

            path.append(start)

            print("Path Found :", path[::-1])
            return

        open_set.remove(n)

        for m, cost in graph.get(n, []):

            if m not in g or g[m] > g[n] + cost:

                g[m] = g[n] + cost
                parent[m] = n

                if m not in open_set:
                    open_set.append(m)

astar("A", "J")
