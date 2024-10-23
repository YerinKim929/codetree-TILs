import sys

def check_already(line, already):
    for al in already:
        for i in range(al[0], al[1]+1):
            if line[0] <= i <= line[1]:
                return 0
    return 1

def how_many_lines(k, already):
    global answer 

    if k == n:
        answer = max(answer, len(already))
        return

    for i in range(k, n):
        if check_already(lines[i], already):
            how_many_lines(k+1, already+[lines[i]])

    how_many_lines(k+1, already)

n = int(input())
lines = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
answer = 0
how_many_lines(0, [])

print(answer)