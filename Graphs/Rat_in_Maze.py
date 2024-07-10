def dfs(i, j, grid, visited, move, ans):
    r = len(grid)
    c = len(grid[0])
    if i == r-1 and j == c-1:
        ans.append(move)
        return
    
    if i > 0 and grid[i-1][j] == 1 and visited[i-1][j] == 0:
        visited[i-1][j] = 1
        dfs(i-1, j, grid, visited, move + "u", ans)
        visited[i-1][j] = 0

    if i+1 < r and grid[i+1][j] == 1 and visited[i+1][j] == 0:
        visited[i+1][j] = 1
        dfs(i+1, j, grid, visited, move + "d", ans)
        visited[i+1][j] = 0
        
    if j > 0 and grid[i][j-1] == 1 and visited[i][j-1] == 0:
        visited[i][j-1] = 1
        dfs(i, j-1, grid, visited, move + "l", ans)
        visited[i][j-1] = 0
        
    if j+1 < c and grid[i][j+1] == 1 and visited[i][j+1] == 0:
        visited[i][j+1] = 1
        dfs(i, j+1, grid, visited, move + "r", ans)
        visited[i][j+1] = 0

def numIslands(grid):
    r = len(grid)
    c = len(grid[0])
    visited = [[0 for _ in range(c)] for _ in range(r)]
    ans = []
    if grid[0][0] == 1:
        visited[0][0] = 1
        dfs(0, 0, grid, visited, "", ans)
    return ans

if __name__ == "__main__":
    rows, cols = map(int, input().split())
    
    grid = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)
    
    result = numIslands(grid)
    if len(result)==0:
        print("-1")
    else:
        for i in result:
            for j in i:
                if j=="d":
                    print("down->",end="")
                if j=="l":
                    print("left->",end="")
                if j=="r":
                    print("right->",end="")
                if j=="u":
                    print("up->",end="")
            print()

# Sample Input   # Sample Input 
# 4 4            #1 0 
# 1 0 0 0        #1 0
# 1 1 0 1
# 1 1 0 0
# 0 1 1 1