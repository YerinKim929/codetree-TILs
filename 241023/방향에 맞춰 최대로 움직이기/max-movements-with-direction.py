import sys

directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def choose(x, y, num):
    global answer

    nxt_d = direct[x][y]-1

    for j in range(1, n):
        nxt_x, nxt_y = x + directions[nxt_d][0]*j, y + directions[nxt_d][1]*j

        if in_range(nxt_x, nxt_y) and board[x][y] < board[nxt_x][nxt_y]:
            choose(nxt_x, nxt_y, num+1)
        else:
            answer = max(answer, num)

n = int(input())
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
direct = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

start_x, start_y = map(int, sys.stdin.readline().split())
start_x -= 1
start_y -= 1
answer = 0

choose(start_x, start_y, 0)

print(answer)