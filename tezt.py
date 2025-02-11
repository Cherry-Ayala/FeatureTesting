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