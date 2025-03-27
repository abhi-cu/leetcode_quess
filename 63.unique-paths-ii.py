def unique_paths_with_obstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
        return 0

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            elif i == 0 and j == 0:
                continue
            else:
                from_top = dp[i - 1][j] if i > 0 else 0
                from_left = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = from_top + from_left

    return dp[m - 1][n - 1]

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(unique_paths_with_obstacles(obstacleGrid))
