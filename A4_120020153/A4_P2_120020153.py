from collections import defaultdict, deque

def add_edges(graph, n, k):
    for i in range(1, n + 1):
        neighbors = graph[i]
        for u in neighbors:
            for v in neighbors:
                if u != v and (u * k == v or v * k == u) and v not in graph[u]:
                    graph[u].append(v)

def bfs_traversal(graph, start):
    visited = [False] * (len(graph) + 1)
    queue = deque()

    result = []

    queue.append(start)
    visited[start] = True

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in sorted(graph[current]):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

    return result

def solve(n, m, k, s, edges):
    graph = defaultdict(list)

    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)

    add_edges(graph, n, k)

    bfs_order = bfs_traversal(graph, s)
    
    print(" ".join(map(str, bfs_order)))

n, m, k, s = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

solve(n, m, k, s, edges)