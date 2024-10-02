from collections import deque
import sys

def bfs():
    q = deque([[0, 0]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        cur_v = q.popleft()

        for i in range(4):
            nx = cur_v[0]+dx[i]
            ny = cur_v[1]+dy[i]
            if graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])


n, m = map(int, sys.stdin.readline().split())
graph = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

visited = [[0]*m for _ in range(n)]


bfs()
print(visited[-1][-1])