import sys
import copy

def in_range(a):
    return 0<= a[0] < n and 0 <= a[1] < n

def calculate_booms(start, boom, already):
    num = 0
    for x, y in boom:
        nxt = [start[0]+x, start[1]+y]
        if in_range(nxt) and not nxt in already:
            already.append(nxt)
    return already

def what_type_booms(s, already):
    global answer 

    if s == S:
        answer = max(answer, len(already))
        return

    for boom in booms:
        tmp_already = copy.deepcopy(already)
        tmp_already = calculate_booms(starts[s], boom, tmp_already)
        what_type_booms(s+1, tmp_already)


booms = [[[0, 0], [1, 0], [2, 0], [-1, 0], [-2, 0]], [[0, 0], [1, 0], [-1, 0],[0, 1], [0, -1]], [[0, 0], [1, 1], [1, -1], [-1, -1], [-1 ,1]]]
n = int(input())
board = [
    list(map(int, sys.stdin.readline().split()))
    for _ in range(n)
]

starts = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            starts.append([i, j])
S = len(starts)

answer = 0
what_type_booms(0, [])

print(answer)