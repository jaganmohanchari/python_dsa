from collections import deque

class solution:
    def rottenOranges(self,matrix):
        m=len(matrix)
        n=len(matrix[0])
        visited=[[0]*n for _ in range(m)]
        q=deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==2 and visited[i][j]==0:
                    q.append(((i,j),0))
                    visited[i][j]=1
        ans=0
        while q:
            (r,c),t=q.popleft()
            ans=max(ans,t)
            if r-1>=0 and matrix[r-1][c]==1 and visited[r-1][c]==0:
                q.append(((r-1,c),t+1))
                visited[r-1][c]=1
            if r+1<m and matrix[r+1][c]==1 and visited[r+1][c]==0:
                q.append(((r+1,c),t+1))
                visited[r+1][c]=1
            if c-1>=0 and matrix[r][c-1]==1 and visited[r][c-1]==0:
                q.append(((r,c-1),t+1))
                visited[r][c-1]=1 
            if c+1<n and matrix[r][c+1]==1 and visited[r][c+1]==0:
                q.append(((r,c+1),t+1))
                visited[r][c+1]=1
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1 and visited[i][j]==0:
                    return -1 
        return ans