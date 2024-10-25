import sys
from collections import deque
from itertools import combinations

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_move(cur, nxt):
    differ = abs(board[cur[0]][cur[1]] - board[nxt[0]][nxt[1]])
    return u <= differ <= d

def bfs(now_cities):
    q = deque([])

    for city in now_cities:
        q.append([city//n, city%n])

    visited = [[0]*n for _ in range(n)]
    result = k

    while q:
        cur = q.popleft()
        visited[cur[0]][cur[1]] = 1

        for dx, dy in zip(dxs, dys):
            nxt_x, nxt_y = cur[0]+dx, cur[1]+dy

            if in_range(nxt_x, nxt_y) and can_move(cur, [nxt_x, nxt_y]):
         
                if not visited[nxt_x][nxt_y]:
                    visited[nxt_x][nxt_y] =  1
                    result += 1
                    q.append([nxt_x, nxt_y])

    return result


n, k, u, d = map(int, sys.stdin.readline().split())
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

answer = 0
cities = [i for i in range(n*n)]
pick_cities = combinations(cities, k)

for now_cities in pick_cities:
    answer = max(answer, bfs(now_cities))

print(answer)