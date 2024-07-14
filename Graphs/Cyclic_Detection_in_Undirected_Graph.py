from collections import deque

def bfs(start, graph, visited):
    q = deque([(start, -1)])
    visited[start] = True
    
    while q:
        curr, parent = q.popleft()
        for i in graph[curr]:
            if not visited[i]:
                visited[i] = True
                q.append((i, curr))
            elif i != parent:
                return True
    return False

def checkCycle(adj):
    n = len(adj)
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            if bfs(i, adj, visited):
                return True
    return False
    
"""
if __name__ == "__main__":
    n, e = map(int, input().split())
    adj = [[] for _ in range(n)]
    
    for _ in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    if(checkCycle(adj)==True):
        print("true")
    else:
        print("false")
"""