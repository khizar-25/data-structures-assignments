def dfs_(gph, s_node):
    visited = set()
    stack = [s_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            stack.extend([neighbor for neighbor in gph[node] if neighbor not in visited])

gph = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1], 3: [1]}
s_from = 2
print(f"Depth-First Search starting from node {s_from}:")
dfs_(gph, s_from)
