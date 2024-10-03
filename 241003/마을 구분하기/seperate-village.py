import sys

def in_range(a):
    return 0 <= a[0] < n and 0 <= a[1] < n

def dfs(cur, house):
    dxs = [1,-1, 0, 0]
    dys = [0, 0, 1, -1]

    house += 1
    visited[cur[0]][cur[1]] = 1

    for dx, dy in zip(dxs, dys):
        new = [cur[0] + dx, cur[1] + dy]

        if in_range(new) and board[new[0]][new[1]] and not visited[new[0]][new[1]]:
            house = dfs(new, house)

    return house

n = int(sys.stdin.readline())

board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

visited = [[0]*n for _ in range(n)]
houses = []

for r in range(n):
    for c in range(n):
        if board[r][c] and not visited[r][c]:
            house = dfs([r, c], 0)
            houses.append(house)

houses.sort()
print(len(houses))
for house in houses:
    print(house)