def dfs_recursive(cur, adj, visited, ans):
    ans.append(cur)
    visited[cur] = 1
    for k in adj[cur]:
        if visited[k] == 0:  # If not visited
            dfs_recursive(k, adj, visited, ans)

def dfs(n, adj):
    visited = [0] * n
    ans = []
    dfs_recursive(0, adj, visited, ans)
    return ans
  
"""    
if __name__ == "__main__":
    n, e = map(int, input().split())  
    adj = [[] for _ in range(n)]  
    for _ in range(e):
        f, t = map(int, input().split())  
        adj[f].append(t)
        adj[t].append(f)

    ans = dfs(n, adj)  
    for k in ans:  
        print(k, end=" ")
"""