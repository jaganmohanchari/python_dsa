from collections import deque

def nearestZero(grid):
    m, n = len(grid), len(grid[0])
    ans = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]
    q = deque()
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                q.append(((i, j), 0))
                visited[i][j] = 1
    
    while q:
        ((r, c), d) = q.popleft()
        ans[r][c] = d
        
        if r > 0 and visited[r-1][c] == 0:
            q.append(((r-1, c), d + 1))
            visited[r-1][c] = 1
        if r + 1 < m and visited[r+1][c] == 0:
            q.append(((r+1, c), d + 1))
            visited[r+1][c] = 1
        if c > 0 and visited[r][c-1] == 0:
            q.append(((r, c-1), d + 1))
            visited[r][c-1] = 1
        if c + 1 < n and visited[r][c+1] == 0:
            q.append(((r, c+1), d + 1))
            visited[r][c+1] = 1
    
    return ans

"""
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
ans = nearestZero(grid)
for row in ans:
    print(' '.join(map(str, row)))
"""