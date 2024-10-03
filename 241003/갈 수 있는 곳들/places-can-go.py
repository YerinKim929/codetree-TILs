import sys
from collections import deque

def in_range(a):
    return 0 <= a[0] < n and 0 <= a[1] < n

n, k = map(int, sys.stdin.readline().split())

board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
visited = [[0]*n for _ in range(n)]
starts = []
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    starts.append([r-1, c-1])
    visited[r-1][c-1] = 1


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

M = len(starts)
for m in range(M):
    q = deque([starts[m]])

    while q:
        cur = q.popleft()
        for i in range(4):
            nxt = [cur[0]+dx[i], cur[1]+dy[i]]
            if in_range(nxt) and not board[nxt[0]][nxt[1]] and not visited[nxt[0]][nxt[1]]:
                visited[nxt[0]][nxt[1]] = 1
                q.append(nxt)


print(sum(sum(visited, [])))