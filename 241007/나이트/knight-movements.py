import sys
from collections import deque

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

n = int(sys.stdin.readline())

board = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
start = [r1-1, c1-1]
end = [r2-1, c2-1]

dxs = [-2, -1, 1, 2, 2, 1, -1, -2]
dys = [1, 2, 2, 1, -1, -2, -2, -1]

q = deque([start])

while q:
    now = q.popleft()

    for dx, dy in zip(dxs, dys):
        new_x, new_y = now[0]+dx, now[1]+dy
        if in_range(new_x, new_y) and not visited[new_x][new_y]:
            visited[new_x][new_y] = visited[now[0]][now[1]] + 1
            q.append([new_x, new_y])


if start == end:
    print(0)
else:
    print(visited[end[0]][end[1]] if visited[end[0]][end[1]] else -1)