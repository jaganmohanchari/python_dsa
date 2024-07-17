from collections import deque

def bfs(start, adj, visited):
    q = deque([start])
    visited[start] = 0
    
    while q:
        cur = q.popleft()
        for k in adj[cur]:
            if visited[k] == -1:
                q.append(k)
                visited[k] = 1 - visited[cur]
            elif visited[k] == visited[cur]:
                return False
    return True

def bipartite(adj):
    n = len(adj)
    visited = [-1] * n
    for i in range(n):
        if visited[i] == -1:
            if not bfs(i, adj, visited):
                return False
    return True

"""
if __name__ == "__main__":
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    print("true" if bipartite(adj) else "false")
"""