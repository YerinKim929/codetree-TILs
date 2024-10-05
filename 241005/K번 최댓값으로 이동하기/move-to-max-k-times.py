import sys 
from collections import deque

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def bfs(cur_r, cur_c):

    visited = [[0]*n for _ in range(n)]

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    q = deque([[cur_c, cur_r]])
    nxt_r, nxt_c = -1, -1
    max_num = 0

    while q:
        now = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_r, new_c = now[0]+dx, now[1]+dy
            if in_range(new_r, new_c) and not visited[new_r][new_c] and board[new_r][new_c] < board[cur_r][cur_c]:
                visited[new_r][new_c] = 1
                q.append([new_r, new_c])
                
                if max_num < board[new_r][new_c]:
                    max_num = board[new_r][new_c]
                    nxt_r, nxt_c = new_r, new_c
                elif max_num == board[new_r][new_c]:
                    if nxt_r > new_r or (new_r == new_r and nxt_c > new_c):
                        nxt_r, nxt_c = new_r, new_c

    return nxt_r, nxt_c

n, k = map(int, sys.stdin.readline().split())
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

start_r, start_c = list(map(int, sys.stdin.readline().split()))
cur_r = start_r-1
cur_c = start_c-1

for i in range(k):

    if cur_r == -1:
        break

    cur_r, cur_c = bfs(cur_r, cur_c)

if cur_r == -1:
    print(start_r, start_c)
else:
    print(cur_r+1, cur_c+1)