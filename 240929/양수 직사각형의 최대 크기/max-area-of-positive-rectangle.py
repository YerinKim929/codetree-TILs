import sys 

def is_all_positive(start_r, end_r, start_c, end_c):

    for r in range(start_r, end_r+1):
        for c in range(start_c, end_c+1):
            if board[r][c] < 0:
                return 0

    return 1 

n, m = map(int, sys.stdin.readline().split())

board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

max_size = -1

for start_r in range(n):
    for end_r in range(start_r, n):
        for start_c in range(m):
            for end_c in range(start_c, m):
                if is_all_positive(start_r, end_r, start_c, end_c):
                    size = (end_r-start_r+1) * (end_c-start_c+1)
                    max_size = max(max_size, size)

print(max_size)