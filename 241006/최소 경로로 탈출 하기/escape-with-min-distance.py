import sys
from collections import deque

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def push(x, y, s):
    step[x][y] = s
    visited[x][y] = 1
    q.append([x, y])

def bfs():
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            
            if in_range(new_x, new_y) and board[new_x][new_y] and not visited[new_x][new_y]:
                push(new_x, new_y, step[x][y] + 1)

n, m = map(int, sys.stdin.readline().split())
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

q = deque()

step = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

push(0, 0, 0)
bfs()

print(step[n-1][m-1])