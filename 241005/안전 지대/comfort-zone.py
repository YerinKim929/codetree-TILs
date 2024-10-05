import sys

def in_range(a):
    return 0 <= a[0] < N and 0 <= a[1] < M

def dfs(cur):
    dxs = [1,-1, 0, 0]
    dys = [0, 0, 1, -1]

    visited[cur[0]][cur[1]] = 1

    for dx, dy in zip(dxs, dys):
        new = [cur[0] + dx, cur[1] + dy]

        if in_range(new) and town[new[0]][new[1]] > K and not visited[new[0]][new[1]]:
            dfs(new)
    
    


N, M = map(int, sys.stdin.readline().split())
town = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(N)
]

K = 1
pre_num = 0
max_k = 1

while True:

    house = 0
    visited = [[0]*M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if town[r][c] > K and not visited[r][c]:
                dfs([r, c])
                house += 1

    if pre_num < house:
        pre_num = house
        max_k = K 
    if not house:
        break

    K += 1


print(f"{max_k} {pre_num}")