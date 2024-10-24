import sys

def choose(i):
    global result

    for j in range(n):

        if sum(visited) == n and j == 0:
            answer.append(board[i][j])
            tmp = sum(answer)
            if result == 0 or result > tmp:
                result = tmp
            answer.pop()
            return

        if board[i][j] != 0 and not visited[j]:
            answer.append(board[i][j])
            visited[j] = 1
            choose(j)
            answer.pop()
            visited[j] = 0

n = int(input())
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
visited = [0]*n
visited[0] = 1
answer = []
result = 0

choose(0)
print(result)