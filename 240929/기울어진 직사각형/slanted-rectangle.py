import sys

def is_range(a, b):
    return 0 <= a < n and 0 <= b < n

def how_move(r, c, move_r, move_c):

    line_sum = 0

    dx = [-1, -1, 1, 1]
    dy = [1, -1, -1 ,1]

    for d in range(4):
        N = move_r+1
        if d==0 or d==2:
            N = move_c+1

        for i in range(N):
            if not is_range(r+dx[d], c+dy[d]):
                return -1
            line_sum += board[r+dx[d]][c+dy[d]]
            r += dx[d]
            c += dy[d]

    return line_sum

n = int(sys.stdin.readline())

board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

max_sum = 0

for r in range(2, n):
    for c in range(1, n):
        # 1이 시작하는 위치 r c
        how_r = max(n-r, r)
        for move_r in range(how_r):
            how_c = max(n-c, c)
            for move_c in range(how_c):
                # 얼마나 움직일 지 정하기 
                line_sum = how_move(r, c, move_r, move_c)
                max_sum = max(max_sum, line_sum)


print(max_sum)