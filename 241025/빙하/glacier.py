import sys
from collections import deque

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def bfs(start):
    
    q = deque([start])

    while q:
        cur = q.popleft()

        for dx, dy in zip(dxs, dys):
            nxt_x, nxt_y = [cur[0]+dx, cur[1]+dy]

            if in_range(nxt_x, nxt_y) and board[nxt_x][nxt_y] == 0 and not visited[nxt_x][nxt_y]:
                visited[nxt_x][nxt_y] = 1
                q.append([nxt_x, nxt_y])

            if in_range(nxt_x, nxt_y) and board[nxt_x][nxt_y] == 1 and not melted[nxt_x][nxt_y]:
                melted[nxt_x][nxt_y] = 1


def melt():
    m = 0
    for r in range(N):
        for c in range(M):
            if melted[r][c] == 1:
                board[r][c] = 0
                melted[r][c] = 0
                m += 1
    return m

N, M = map(int, sys.stdin.readline().split())
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(N)
]

melted = [[0]*M for _ in range(N)]

time = 0
num = 0

while True:
    if sum(map(sum, board)) == 0:
        print(time, num)
        break
    visited = [[0]*M for _ in range(N)]
    bfs([0, 0])

    num = melt()
    time += 1