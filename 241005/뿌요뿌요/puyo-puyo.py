import sys
sys.setrecursionlimit(10000)

def in_range(a):
    return 0 <= a[0] < n and 0 <= a[1] < n

def dfs(cur, block):

    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]

    block += 1
    visited[cur[0]][cur[1]] = 1

    for dx, dy in zip(dxs, dys):
        new = [cur[0]+dx, cur[1]+dy]
        if in_range(new) and board[cur[0]][cur[1]] == board[new[0]][new[1]] and not visited[new[0]][new[1]]:
            block = dfs(new, block)

    return block

n = int(sys.stdin.readline())
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
visited = [[0]*n for _ in range(n)]

max_block = 0
num_pop = 0

for r in range(n):
    for c in range(n):
        if not visited[r][c]:
            block = dfs([r, c], 0)

            if max_block < block:
                max_block = block
            if block > 3:
                num_pop += 1

print(f"{num_pop} {max_block}")