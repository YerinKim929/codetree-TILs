import sys

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False

    return True

def dfs(x, y):
    global order

    dxs, dys = [1, 0], [0, 1]

    answer[x][y] = 1
    visited[x][y] = 1

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            dfs(new_x, new_y)


n, m = map(int, sys.stdin.readline().split())
grid = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

answer = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dfs(0, 0)
print(answer[n-1][m-1])