import sys

def choose(i, r):

    global result

    if i == n:
        result = max(result, sum(answer))
        return

    
    if not visited_r[r]:
        for c in range(n):
            if not visited_c[c]:
                answer.append(board[r][c])
                visited_r[r] = 1
                visited_c[c] = 1

                choose(i+1, r+1)

                answer.pop()
                visited_r[r] = 0
                visited_c[c] = 0
    

n = int(input())
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
visited_r = [0]*n
visited_c = [0]*n
answer = []
result = 0

choose(0, 0)
print(result)