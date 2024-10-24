import sys

def choose_jump(i, cur):

    global answer

    if cur >= n-1:
        if answer < 0 or answer > i:
            answer = i
        return 

    if i == n:
        return 

    for j in range(1, jumps[cur]+1):
        choose_jump(i+1, cur+j)

    

n = int(input())
jumps = list(map(int, sys.stdin.readline().split()))
answer = -1

choose_jump(0, 0)
print(answer)