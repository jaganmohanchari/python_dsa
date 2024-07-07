def dfs(i, j, image, startingColor, newColor):
    m, n = len(image), len(image[0])
    image[i][j] = newColor
    
    if i > 0 and image[i-1][j] == startingColor:
        dfs(i-1, j, image, startingColor, newColor)
        
    if i+1 < m and image[i+1][j] == startingColor:
        dfs(i+1, j, image, startingColor, newColor)
        
    if j > 0 and image[i][j-1] == startingColor:
        dfs(i, j-1, image, startingColor, newColor)
        
    if j+1 < n and image[i][j+1] == startingColor:
        dfs(i, j+1, image, startingColor, newColor)

def floodFill(image, r, c, newColor):
    startingColor = image[r][c]
    
    if newColor == startingColor:
        return image
        
    dfs(r, c, image, startingColor, newColor)
    return image
    
"""
if __name__ == "__main__":
    m, n, r, c, newColor = map(int, input().split())
    image = [list(map(int, input().split())) for _ in range(m)]
    floodFill(image, r, c, newColor)
    for row in image:
        print(' '.join(map(str, row)))
"""