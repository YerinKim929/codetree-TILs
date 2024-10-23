import sys 
from collections import deque
from itertools import combinations
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(a):
    return 0 <= a[0] < n and 0 <= a[1] < n

def bfs(start):

    q = deque([start])

    while q:
        cur = q.popleft()

        for dx, dy in zip(dxs, dys):
            nxt = [cur[0]+dx, cur[1]+dy]
            if in_range(nxt) and not board[nxt[0]][nxt[1]] and not visited[nxt[0]][nxt[1]]:
                visited[nxt[0]][nxt[1]] = 1
                q.append(nxt)


n, k, m = map(int, sys.stdin.readline().split())
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
visited = [[0]*n for _ in range(n)]
starts = []
for i in range(k):
    r, c = map(int, sys.stdin.readline().split())
    starts.append([r-1, c-1])

rocks_idx = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            rocks_idx.append([i, j])

rocks_out = list(combinations(rocks_idx, m))
result = 0

for start in starts:
    if not visited[start[0]][start[1]]:
        visited[start[0]][start[1]] = 1
        bfs(start)

for rocks in rocks_out:
    for rock in rocks:
        board[rock[0]][rock[1]] = 0

    for rock in rocks:
        visited[rock[0]][rock[1]] = 1
        bfs(rock)

    tmp = sum(map(sum, visited))
    if result < tmp:
        result = tmp

    for rock in rocks:
        board[rock[0]][rock[1]] = 1
        visited[rock[0]][rock[1]] = 0

print(result)