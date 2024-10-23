import sys

def check_already(line, already):
    for al in already:
        if not(line[1] < al[0] or al[1] <= line[0]):
            return 0
    return 1

def how_many_lines(k, already):
    global answer 

    if k == n:
        answer = max(answer, len(already))
        return

    how_many_lines(k+1, already)

    if check_already(lines[k], already):
        how_many_lines(k+1, already+[lines[k]])



n = int(input())
lines = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]
answer = 0
how_many_lines(0, [])

print(answer)