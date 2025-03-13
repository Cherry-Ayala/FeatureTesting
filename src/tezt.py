def longestPath(grid):
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    dp = [[-1] * m for _ in range(n)]

    def dfs(x, y):
        if dp[x][y] != -1:
            return dp[x][y]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        max_len = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == grid[x][y] + 1:
                length = 1 + dfs(nx, ny)
                max_len = max(max_len, length)
        dp[x][y] = max_len
        return max_len

    longest = 0
    for i in range(n):
        for j in range(m):
            longest = max(longest, dfs(i, j))
    
    return longest

def findX(path, x):  
    return [i for i, val in enumerate(path) if val == x]

#make a use case for longest path
matrix = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]

print(longestPath(matrix))  # Expected output is 4

#make a function that calls findX to find a location, and then uses longest path to find the longest path from a given starting point
def longestPathFromStart(matrix, start_value):
    positions = findX(sum(matrix, []), start_value)
    longest = 0
    for pos in positions:
        x, y = divmod(pos, len(matrix[0]))
        longest = max(longest, longestPathUtil(matrix, x, y))
    return longest

def longestPathUtil(matrix, x, y):
    n = len(matrix)
    m = len(matrix[0])
    dp = [[-1] * m for _ in range(n)]

    def dfs(nx, ny):
        if dp[nx][ny] != -1:
            return dp[nx][ny]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        max_len = 1
        for dx, dy in directions:
            nnx, nny = nx + dx, ny + dy
            if 0 <= nnx < n and 0 <= nny < m and matrix[nnx][nny] == matrix[nx][ny] + 1:
                length = 1 + dfs(nnx, nny)
                max_len = max(max_len, length)
        dp[nx][ny] = max_len
        return max_len

    return dfs(x, y)

# Usage
start_value = 6
print(longestPathFromStart(matrix, start_value))  # Expected output is 3